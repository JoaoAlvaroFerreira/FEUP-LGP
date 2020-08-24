import React, {useState} from 'react';
import Page from '../templates/Page';
import FinishButton from '../templates/button/FinishButton';
import MultiButton, {
	ArrowIcon,
	EditIcon,
} from '../templates/button/MultiButton';
import {MainNavProps} from '../../routes/MainParamList';
import {Perimetry as PerimetryType} from '../../store/treatment/types';

const PerimetryList = ({
	navigation,
	route,
}: MainNavProps<'PerimetryList'>) => {
	const [perimetries, setPerimetries] = useState<PerimetryType[]>(
		route.params?.tests ? route.params.tests : []
	);

	const editPerimetry = (test: PerimetryType) => {
		if (test.index) {
			setPerimetries(
				perimetries.map((t) => (t.index === test.index ? test : t))
			);
		} else {
			setPerimetries([
				...perimetries,
				{...test, index: perimetries.length + 1},
			]);
		}
	};

	const finish = () => {
		route.params.onSave(perimetries);
		navigation.goBack();
	};
	return (
		<Page title={'Perimetria'} hasBack={true} hasMargin={true}>
			{perimetries.map((test, index) => (
				<MultiButton
					key={index}
					primaryText={test.muscle}
					rightIcon={EditIcon}
					onPressRight={() =>
						navigation.navigate('Perimetry', {test, onSave: editPerimetry})
					}
				/>
			))}

			<MultiButton
				primaryText='Adicionar Membro'
				onPressRight={() =>
					navigation.navigate('Perimetry', {onSave: editPerimetry})
				}
				rightIcon={ArrowIcon}
			/>

			{perimetries.length > 0 && <FinishButton onPress={finish} />}
		</Page>
	);
};

export default PerimetryList;
