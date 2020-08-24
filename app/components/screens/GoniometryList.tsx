import React, {useState} from 'react';
import Page from '../templates/Page';
import FinishButton from '../templates/button/FinishButton';
import MultiButton, {
	ArrowIcon,
	EditIcon,
} from '../templates/button/MultiButton';
import {MainNavProps} from '../../routes/MainParamList';
import {Goniometry as GoniometryType} from '../../store/treatment/types';

const GoniometryList = ({
	navigation,
	route,
}: MainNavProps<'GoniometryList'>) => {
	const [goniometries, setGoniometries] = useState(route.params.tests);

	const editGoniometry = (test: GoniometryType, index?: number) => {
		if (index !== undefined) {
			setGoniometries([
				...goniometries.slice(0, index),
				test,
				...goniometries.slice(index + 1, goniometries.length),
			]);
		} else {
			setGoniometries([...goniometries, test]);
		}
	};

	const finish = () => {
		route.params.onSave(goniometries);
		navigation.goBack();
	};
	return (
		<Page title={'Goniometria'} hasBack={true} hasMargin={true}>
			{goniometries.map((test, index) => (
				<MultiButton
					key={index}
					primaryText={test.muscleName}
					rightIcon={EditIcon}
					onPressRight={() =>
						navigation.navigate('Goniometry', {
							test,
							onSave: editGoniometry,
							index,
						})
					}
				/>
			))}

			<MultiButton
				primaryText='Adicionar Membro'
				onPressRight={() =>
					navigation.navigate('Goniometry', {onSave: editGoniometry})
				}
				rightIcon={ArrowIcon}
			/>

			{goniometries.length > 0 && <FinishButton onPress={finish} />}
		</Page>
	);
};

export default GoniometryList;
