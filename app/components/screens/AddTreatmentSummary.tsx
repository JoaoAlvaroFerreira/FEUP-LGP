import React, {useState} from 'react';
import Page from '../templates/Page';
import Bigtext from '../templates/input/Bigtext';
import SliderInput from '../templates/slider/SliderInput';
import FinishButton from '../templates/button/FinishButton';
import {MainNavProps} from '../../routes/MainParamList';
import {Summary} from '../../store/treatment/types';

const AddTreatmentSummary = ({
	navigation,
	route,
}: MainNavProps<'AddTreatmentSummary'>) => {
	const [summary, setSummary] = useState(route.params.summary.description);
	const [pain, setPain] = useState(route.params.summary.pain);

	const save = () => {
		const resultSummary: Summary = {description: summary, pain: pain};
		route.params.onSave(resultSummary);
		navigation.goBack();
	};

	return (
		<Page title='Sumário' hasBack={true} hasMargin={true}>
			<Bigtext
				placeholder='Insira aqui a informaçao...'
				value={summary}
				onChange={setSummary}
			/>
			<SliderInput
				label='Intensidade da dor'
				min={0}
				max={10}
				unit='dor moderada'
				value={pain}
				onChange={setPain}
			/>
			<FinishButton onPress={save} />
		</Page>
	);
};

export default AddTreatmentSummary;
