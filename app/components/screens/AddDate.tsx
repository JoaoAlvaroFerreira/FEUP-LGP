import React, { useState } from 'react';
import Page from '../templates/Page';
import { Platform } from 'react-native';
import FinishButton from '../templates/button/FinishButton';
import DateTimePicker from '@react-native-community/datetimepicker';
import { MainNavProps } from '../../routes/MainParamList';
import { useDispatch } from 'react-redux';
import { saveTreatment } from '../../store/treatment/actions';
import { Treatment as TreatmentType } from '../../store/treatment/types';
import MultiButton, {
  CalendarIcon,
  ScheduleIcon
} from '../templates/button/MultiButton';

const AddDate = ({
  navigation,
  route
}: MainNavProps<'AddDate'>) => {
  const dispatch = useDispatch();
  const optionsDate = {weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'};

  const [treatment, setTreatment] = useState<TreatmentType>(route.params?.treatment);

  const [date, setDate] = useState(new Date());
  const [currentTimeType, setCurrentTimeType] = useState('initial');
  const [mode, setMode] = useState('date');
  const [show, setShow] = useState(false);

  const handleChange = (event: any, selectedValue: Date) => {
    setShow(Platform.OS === 'ios');
    setDate(selectedValue);

    if (mode == 'date') {
      const startDate = treatment.startDate, endDate = treatment.endDate;

      startDate?.setDate(selectedValue.getDate());
      startDate?.setMonth(selectedValue.getMonth());
      startDate?.setFullYear(selectedValue.getFullYear());

      endDate?.setDate(selectedValue.getDate());
      endDate?.setMonth(selectedValue.getMonth());
      endDate?.setFullYear(selectedValue.getFullYear());

      setTreatment({ ...treatment, startDate: startDate });
      setTreatment({ ...treatment, endDate: endDate });
    } else {
      if (currentTimeType == 'initial') {
        setTreatment({ ...treatment, startDate: selectedValue });
      } else {
        setTreatment({ ...treatment, endDate: selectedValue });
      }
    }
  };

  const showMode = (currentMode: React.SetStateAction<string>) => {
    setShow(true);
    setMode(currentMode);
  };

  const showDatePicker = () => {
    showMode("date");
  };

  const showTimePicker = (currentTimeType: string) => {
    showMode("time");
    setCurrentTimeType(currentTimeType);
  };

  const save = () => {
    dispatch(saveTreatment(treatment));
  };

  return (
    <Page title="Data do Tratamento" hasBack={true} hasMargin={true}>


      <MultiButton
        primaryText='Data'
        secondaryText={date.toLocaleDateString(undefined,optionsDate)}
        rightIcon={CalendarIcon}
        onPressRight={() => showDatePicker()}
      />

      <MultiButton
        primaryText='Início do Tratamento'
        secondaryText={treatment.startDate?.getHours() + ':' + (treatment.startDate?.getMinutes()<10?'0':'') + treatment.startDate?.getMinutes()}
        rightIcon={ScheduleIcon}
        onPressRight={() => showTimePicker('initial')}
      />

      <MultiButton
        primaryText='Fim do Tratamento'
        secondaryText={treatment.endDate?.getHours() + ':' + (treatment.endDate?.getMinutes()<10?'0':'') + treatment.endDate?.getMinutes()}
        rightIcon={ScheduleIcon}
        onPressRight={() => showTimePicker('final')}
      />

      {show && (
        <DateTimePicker
          testID="dateTimePicker"
          timeZoneOffsetInMinutes={60}
          value={currentTimeType == "initial" ? treatment.startDate
          : treatment.endDate}
          mode={mode}
          is24Hour={true}
          display="spinner"
          onChange={handleChange}
        />
      )}

      <FinishButton
        label='Termos e Condições'
        icon='next'
        onPress={() => navigation.navigate('TermsAndConditions', { onSave: save })}
      />
    </Page>
  );
};

export default AddDate;
