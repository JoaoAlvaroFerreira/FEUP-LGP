import React, {useState} from 'react';
import Page from '../templates/Page';
import SliderInput from '../templates/slider/SliderInput';
import FinishButton from '../templates/button/FinishButton';
import {MainNavProps} from '../../routes/MainParamList';
import {Perimetry as PerimetryType} from '../../store/treatment/types';
import ButtonInput from '../templates/input/ButtonInput';

const Perimetry = ({navigation, route}: MainNavProps<'Perimetry'>) => {
	const [perimetry, setPerimetry] = useState<PerimetryType>(
		route.params?.test ? route.params.test : {muscle: '', measure: 0}
	);

	let searchContent = '';

	const setMuscle = (muscle: string) => {
		setPerimetry({...perimetry, muscle: muscle});
	};

	const setMeasure = (measure: number) => {
		setPerimetry({...perimetry, measure: measure});
	};

	const finish = () => {
		route.params.onSave(perimetry);
		navigation.goBack();
	};

	return (
		<Page
			title={'Perimetria'}
			hasBack={true}
			search={(text) => {searchContent = text; }}
			hasMargin={true}>

			<ButtonInput 
                label='Nome do músculo'
				value={perimetry.muscle}
                onPress={()=>navigation.navigate('SearchBodyPart', { muscle: perimetry.muscle, onSave: setMuscle })} />

			<SliderInput
				label={'Medida'}
				min={0}
				max={200}
				unit={'cm'}
				value={perimetry.measure}
				onChange={setMeasure}
			/>
			<FinishButton icon='next' onPress={finish} />
		</Page>
	);
};

export default Perimetry;
