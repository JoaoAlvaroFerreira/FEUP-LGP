import React, {useState} from 'react';
import {
	StyleSheet,
	Text,
	View,
	TextInput,
	FlatList,
	TouchableHighlight,
} from 'react-native';
import {MainNavProps} from '../../routes/MainParamList';
import FinishButton from '../templates/button/FinishButton';
import {useDispatch, useSelector} from 'react-redux';
import {filterBodyParts} from '../../store/body_parts/actions';
import {AppState} from '../../store';
import Page from '../templates/Page';
import {BodyPart} from '../../store/body_parts/types';

const SearchBodyPart: React.FC<MainNavProps<'SearchBodyPart'>> = ({
	navigation,
	route,
}) => {
	const dispatch = useDispatch();
	const filteredBodyParts = useSelector(
		(state: AppState) => state.bodyPartsStore.filteredBodyParts
	);

	const [searchInput, setSearchInput] = useState(route.params.muscle);
	const [selectedMuscle, setSelectedMuscle] = useState<BodyPart>();

	const save = () => {
		if (selectedMuscle) route.params.onSave(selectedMuscle);
		navigation.goBack();
	};
	const handleSearchChange = (text: string) => {
		setSearchInput(text);
		dispatch(filterBodyParts(text));
	};

	const chooseMuscle = (bodyPart: BodyPart) => {
		setSearchInput(bodyPart.name);
		setSelectedMuscle(bodyPart);
	};

	return (
		<Page title={'Músculo'} hasBack={true} hasMargin={true}>
			<Text>Pesquisar</Text>
			<View>
				<TextInput
					placeholder={'Insira aqui o nome...'}
					value={searchInput}
					onChangeText={handleSearchChange}
				/>
				<FlatList
					data={filteredBodyParts}
					keyExtractor={(item) => item.id}
					renderItem={({item}) => (
						<TouchableHighlight onPress={() => chooseMuscle(item)}>
							<Text>{item.name}</Text>
						</TouchableHighlight>
					)}
				/>
			</View>

			<FinishButton onPress={save} />
		</Page>
	);
};

const styles = StyleSheet.create({});

export default SearchBodyPart;
