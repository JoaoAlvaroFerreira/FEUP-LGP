import React, {useState} from 'react';
import Page from '../templates/Page';
import FinishButton from '../templates/button/FinishButton';
import MultiButton, {
	ArrowIcon,
	EditIcon,
} from '../templates/button/MultiButton';
import {MainNavProps} from '../../routes/MainParamList';
import {MuscleTest as MuscleTestType} from '../../store/treatment/types';

const MuscleTestList = ({
	navigation,
	route,
}: MainNavProps<'MuscleTestList'>) => {
	const [muscleTests, setMuscleTests] = useState<MuscleTestType[]>(
		route.params?.tests ? route.params.tests : []
	);

	const editMuscleTest = (test: MuscleTestType) => {
		if (test.index) {
			setMuscleTests(
				muscleTests.map((t) => (t.index === test.index ? test : t))
			);
		} else {
			setMuscleTests([
				...muscleTests,
				{...test, index: muscleTests.length + 1},
			]);
		}
	};

	const finish = () => {
		route.params.onSave(muscleTests);
		navigation.goBack();
	};
	return (
		<Page title={'Teste Muscular'} hasBack={true} hasMargin={true}>
			{muscleTests.map((test, index) => (
				<MultiButton
					key={index}
					primaryText={test.name}
					rightIcon={EditIcon}
					onPressRight={() =>
						navigation.navigate('MuscleTest', {test, onSave: editMuscleTest})
					}
				/>
			))}

			<MultiButton
				primaryText='Adicionar Membro'
				onPressRight={() =>
					navigation.navigate('MuscleTest', {onSave: editMuscleTest})
				}
				rightIcon={ArrowIcon}
			/>

			{muscleTests.length > 0 && <FinishButton onPress={finish} />}
		</Page>
	);
};

export default MuscleTestList;
