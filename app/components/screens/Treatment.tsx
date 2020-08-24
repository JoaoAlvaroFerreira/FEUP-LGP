import React, {useState} from 'react';
import Page from '../templates/Page';
import FinishButton from '../templates/button/FinishButton';
import MultiButton, {
	ArrowIcon,
	CheckBoxIcon,
} from '../templates/button/MultiButton';
import {MainNavProps} from '../../routes/MainParamList';
import {
	Treatment as TreatmentType,
	Summary,
	MuscleTest,
	Perimetry,
	Goniometry,
	OtherAnnotations,
} from '../../store/treatment/types';

const Treatment: React.FC<MainNavProps<'Treatment'>> = ({
	navigation,
	route,
}) => {
	const [treatment, setTreatment] = useState<TreatmentType>(
		route.params?.treatment ? route.params.treatment : defaultTreatment
	);

	const updateSummary = (summary: Summary) => {
		setTreatment({...treatment, summary: summary});
	};

	const updateMuscleTests = (tests: MuscleTest[]) => {
		setTreatment({...treatment, muscleTests: tests});
	};

	const updatePerimetries = (tests: Perimetry[]) => {
		setTreatment({...treatment, perimetries: tests});
	};

	const updateGoniometries = (tests: Goniometry[]) => {
		setTreatment({...treatment, goniometries: tests});
	};

	const updateOtherAnnotations = (otherAnnotations: OtherAnnotations) => {
		setTreatment({...treatment, otherAnnotations: otherAnnotations});
	};

	return (
		<Page title='Tratamento' hasBack={true} hasMargin={true}>
			<MultiButton
				primaryText='Sumário'
				onPressRight={() =>
					navigation.navigate('AddTreatmentSummary', {
						summary: treatment.summary,
						onSave: updateSummary,
					})
				}
				rightIcon={ArrowIcon}
				leftIcon={CheckBoxIcon}
			/>
			<MultiButton
				primaryText='Goniometria'
				onPressRight={() =>
					navigation.navigate('GoniometryList', {
						tests: treatment.goniometries,
						onSave: updateGoniometries,
					})
				}
				rightIcon={ArrowIcon}
				leftIcon={CheckBoxIcon}
			/>
			<MultiButton
				primaryText='Teste Muscular'
				onPressRight={() =>
					navigation.navigate('MuscleTestList', {
						tests: treatment.muscleTests,
						onSave: updateMuscleTests,
					})
				}
				rightIcon={ArrowIcon}
				leftIcon={CheckBoxIcon}
			/>
			<MultiButton
				primaryText='Perimetria'
				onPressRight={() =>
					navigation.navigate('PerimetryList', {
						tests: treatment.perimetries,
						onSave: updatePerimetries,
					})
				}
				rightIcon={ArrowIcon}
				leftIcon={CheckBoxIcon}
			/>
			<MultiButton
				primaryText='Outras Anotações'
				onPressRight={() =>
					navigation.navigate('OtherAnnotationsList', {
						otherAnnotations: treatment.otherAnnotations,
						onSave: updateOtherAnnotations,
					})
				}
				rightIcon={ArrowIcon}
				leftIcon={CheckBoxIcon}
			/>

			<FinishButton
				label='Definir data'
				icon='next'
				onPress={() => navigation.navigate('AddDate', {treatment: treatment})}
			/>
		</Page>
	);
};

const defaultTreatment: TreatmentType = {
	patientName: '',
	summary: {description: '', pain: 0},
	muscleTests: [],
	perimetries: [],
	goniometries: [],
	otherAnnotations: {medication: '', treatment: '', weeklyEvaluation: ''},
	checkBoxes: [...Array(5)].map(() => false),
	startDate: new Date(),
	endDate: new Date(),
	isOpen: true,
};

export default Treatment;
