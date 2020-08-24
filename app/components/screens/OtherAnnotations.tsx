import React, { useState } from 'react';
import Bigtext from '../templates/input/Bigtext';
import Page from '../templates/Page';
import FinishButton from '../templates/button/FinishButton';
import { OtherAnnotations as OtherAnnotationsType } from '../../store/treatment/types';
import { MainNavProps } from '../../routes/MainParamList';

const OtherAnnotations = ({ navigation, route }: MainNavProps<'OtherAnnotations'>) => {
    const [otherAnnotations, setOtherAnnotations] = useState<OtherAnnotationsType>(
        route.params?.otherAnnotations ? route.params.otherAnnotations : { medication: '', treatment: '', weeklyEvaluation: '' }
    );

    const [input, setInput] = useState(
        route.params.annotationType == 'Medicação' ? otherAnnotations.medication
            : route.params.annotationType == 'Tratamento' ? otherAnnotations.treatment
                : otherAnnotations.weeklyEvaluation
    );

    const finish = () => {
        if (route.params.annotationType == 'Medicação') {
            otherAnnotations.medication = input;
        } else if (route.params.annotationType == 'Tratamento') {
            otherAnnotations.treatment = input;
        } else {
            otherAnnotations.weeklyEvaluation = input;
        }

        route.params.onSave(otherAnnotations);
        navigation.goBack();
    };

    return (
        <Page title={route.params.annotationType}
            hasBack={true}
            hasMargin={true}>
            <Bigtext placeholder='Insira aqui a informaçao...' value={input} onChange={setInput} />
            <FinishButton onPress={finish} />
        </Page>
    );
};

export default OtherAnnotations;