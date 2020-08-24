import React, { useState } from 'react';
import Page from '../templates/Page';
import FinishButton from '../templates/button/FinishButton';
import MultiButton, { CheckBoxIcon, ArrowIcon } from '../templates/button/MultiButton';
import { MainNavProps } from '../../routes/MainParamList';
import { OtherAnnotations } from '../../store/treatment/types';

const OtherAnnotationsList = ({
  navigation,
  route,
}: MainNavProps<'OtherAnnotationsList'>) => {
  const [otherAnnotations, setOtherAnnotations] = useState(route.params.otherAnnotations);
  const MedicationType = 'Medicação', TreatmentType = 'Tratamento', WeeklyEvaluationType = 'Avaliação Semanal';

  const save = () => {
    const resultOtherAnnotations: OtherAnnotations = otherAnnotations;
    route.params.onSave(resultOtherAnnotations);
    navigation.goBack();
  };

  const updateOtherAnnotations = (otherAnnotations: OtherAnnotations) => {
    setOtherAnnotations({ ...otherAnnotations });
  };


  const onPressAnnotation = (annotationType: string) => {
    navigation.navigate('OtherAnnotations', { annotationType, otherAnnotations, onSave: updateOtherAnnotations });
  };

  return (
    <Page title="Outras Anotações" hasBack={true} hasMargin={true}>
      <MultiButton
        primaryText={MedicationType}
        leftIcon={CheckBoxIcon}
        rightIcon={ArrowIcon}
        onPressRight={() => onPressAnnotation(MedicationType)}
      />
      <MultiButton
        primaryText={TreatmentType}
        leftIcon={CheckBoxIcon}
        rightIcon={ArrowIcon}
        onPressRight={() => onPressAnnotation(TreatmentType)}
      />
      <MultiButton
        primaryText={WeeklyEvaluationType}
        leftIcon={CheckBoxIcon}
        rightIcon={ArrowIcon}
        onPressRight={() => onPressAnnotation(WeeklyEvaluationType)}
      />

      <FinishButton label="Concluir" onPress={save} />

    </Page>
  );
};

export default OtherAnnotationsList;