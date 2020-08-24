import React, {useState} from 'react';
import Page from '../templates/Page';
import SliderInput from '../templates/slider/SliderInput';
import FinishButton from '../templates/button/FinishButton';
import {MainNavProps} from '../../routes/MainParamList';
import {MuscleTest as MuscleTestType} from '../../store/treatment/types';
import ButtonInput from '../templates/input/ButtonInput';

const MuscleTest = ({navigation, route}: MainNavProps<'MuscleTest'>) => {
	const [muscleTest, setMuscleTest] = useState<MuscleTestType>(
		route.params?.test ? route.params.test : {name: '', pain: 0}
	);

	let searchContent = '';

	const setName = (name: string) => {
		setMuscleTest({...muscleTest, name: name});
	};

	const setPain = (pain: number) => {
		setMuscleTest({...muscleTest, pain: pain});
	};

	const finish = () => {
		route.params.onSave(muscleTest);
		navigation.goBack();
	};

	return (
		<Page
			title={'Teste Muscular'}
			hasBack={true}
			search={(text) => {searchContent = text; }}
			hasMargin={true}>

			<ButtonInput 
                label='Nome do músculo'
				value={muscleTest.name}
                onPress={()=>navigation.navigate('SearchBodyPart', { muscle: muscleTest.name, onSave: setName })} />

			<SliderInput
				label={'Intensidade da dor'}
				min={0}
				max={10}
				unit={''}
				value={muscleTest.pain}
				onChange={setPain}
			/>

			<FinishButton icon='next' onPress={finish} />
		</Page>
	);
};

export default MuscleTest;
