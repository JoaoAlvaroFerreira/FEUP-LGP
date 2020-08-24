import React, {useState} from 'react';
import Page from '../templates/Page';
import RangeSliderInput from '../templates/slider/RangeSliderInput';
import FinishButton from '../templates/button/FinishButton';
import {MainNavProps} from '../../routes/MainParamList';
import {Goniometry as GoniometryType} from '../../store/treatment/types';
import ButtonInput from '../templates/input/ButtonInput';
import {BodyPart} from '../../store/body_parts/types';

const Goniometry = ({navigation, route}: MainNavProps<'Goniometry'>) => {
	const [goniometry, setGoniometry] = useState<GoniometryType>(
		route.params?.test
			? route.params.test
			: {
					muscleId: '',
					muscleName: '',
					abductionRange: [],
					adductionRange: [],
					flexionRange: [],
					rotationRange: [],
					extentRange: [],
			  }
	);

	const setMuscle = (muscle: BodyPart) => {
		setGoniometry({
			...goniometry,
			muscleId: muscle.id,
			muscleName: muscle.name,
		});
	};

	const setAbductionRange = (abductionRange: number[]) => {
		setGoniometry({...goniometry, abductionRange: abductionRange});
	};

	const setAdductionRange = (adductionRange: number[]) => {
		setGoniometry({...goniometry, adductionRange: adductionRange});
	};

	const setFlexionRange = (flexionRange: number[]) => {
		setGoniometry({...goniometry, flexionRange: flexionRange});
	};

	const setRotationRange = (rotationRange: number[]) => {
		setGoniometry({...goniometry, rotationRange: rotationRange});
	};

	const setExtentRange = (extentRange: number[]) => {
		setGoniometry({...goniometry, extentRange: extentRange});
	};

	const finish = () => {
		route.params.onSave(goniometry, route.params?.index);
		navigation.goBack();
	};

	return (
		<Page title={'Goniometria'} hasBack={true} hasMargin={true}>
			<ButtonInput
				label='Nome do músculo'
				value={goniometry.muscleName}
				onPress={() =>
					navigation.navigate('SearchBodyPart', {
						muscle: goniometry.muscleName,
						onSave: setMuscle,
					})
				}
			/>

			<RangeSliderInput
				label='Abdução'
				min={0}
				max={180}
				interval={5}
				unit='º'
				value={goniometry.abductionRange}
				onChange={setAbductionRange}
			/>

			<RangeSliderInput
				label='Adução'
				min={0}
				max={180}
				interval={5}
				unit='º'
				value={goniometry.adductionRange}
				onChange={setAdductionRange}
			/>

			<RangeSliderInput
				label='Flexão'
				min={0}
				max={180}
				interval={5}
				unit='º'
				value={goniometry.flexionRange}
				onChange={setFlexionRange}
			/>

			<RangeSliderInput
				label='Rotação'
				min={0}
				max={180}
				interval={5}
				unit='º'
				value={goniometry.rotationRange}
				onChange={setRotationRange}
			/>

			<RangeSliderInput
				label='Extensão'
				min={0}
				max={180}
				interval={5}
				unit='º'
				value={goniometry.extentRange}
				onChange={setExtentRange}
			/>

			<FinishButton icon='next' onPress={finish} />
		</Page>
	);
};

export default Goniometry;
