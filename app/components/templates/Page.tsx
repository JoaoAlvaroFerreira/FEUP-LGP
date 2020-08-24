import React, { useState } from 'react';
import { StyleSheet, Text, View, FlatList } from 'react-native';
import { TouchableOpacity } from 'react-native';
import Navbar from './Navbar';
import CustomTextInput from '../templates/input/CustomTextInput';
import { Feather, AntDesign } from '@expo/vector-icons';
import { useNavigation } from '@react-navigation/native';
import { useDispatch } from 'react-redux';
import { logOut } from '../../store/user/actions';


interface Props {
	title?: string;
	hasBack?: boolean;
	search?: (text: string) => void;
	hasMargin?: boolean;
	hasLogout?: boolean
}

const Page: React.FC<Props> = ({
	title,
	hasBack,
	hasLogout,
	hasMargin,
	search,
	children,
}) => {
	const navigation = useNavigation();
	const [showSearch, setShowSearch] = useState(false);
	const dispatch = useDispatch();

	const goBack = () => navigation.goBack();

	const displaySearch = () => setShowSearch(!showSearch);

	const _renderItem = () => (
		<View>
			{search && showSearch && (
				<View style={{ marginHorizontal: 20, marginBottom: 20 }}>
					<CustomTextInput onChange={search} placeholder='Pesquisar' />
				</View>
			)}

			{/* Custom content */}
			{hasMargin ? <View style={{ margin: 20 }}>{children}</View> : children}
		</View>
	);

	return (
		<View style={styles.Page}>
			{/* Title */}
			<View
				style={{
					display: 'flex',
					flexDirection: 'row',
					alignItems: 'center',
					marginTop: 25,
					marginBottom: 20,
					marginLeft: 20,
				}}>
				{hasBack && (
					<TouchableOpacity style={{ marginRight: 20 }} onPress={goBack}>
						<AntDesign name='arrowleft' size={25} color='#17224D' />
					</TouchableOpacity>
				)}

				<Text style={styles.Title}> {title ? title : ''}</Text>
				{search && (
					<TouchableOpacity
						style={{ marginRight: 20, marginLeft: 'auto' }}
						onPress={displaySearch}>
						<Feather name='search' size={25} color='#17224D' />
					</TouchableOpacity>
				)}

				{hasLogout && (
					<TouchableOpacity style={{ marginRight: 20 }} onPress={() => dispatch(logOut())}>
						<AntDesign name="poweroff" size={24} color="#17224D" />
					</TouchableOpacity>
				)}
			</View>

			{/* Content */}
			<FlatList
				style={{ marginBottom: 70 }}
				data={[{ search: search, showSearch: showSearch, hasMargin: hasMargin, children: children }]}
				renderItem={_renderItem}
				keyExtractor={(item, index) => index.toString()}
			/>

			{/* Bottom navbar */}
			<Navbar />
		</View>
	);
};

const styles = StyleSheet.create({
	Page: {
		backgroundColor: 'white',
		flex: 1,
		marginTop: 40,
	},
	Title: {
		flex: 1,
		flexWrap: 'wrap',
		color: '#17224D',
		fontSize: 25,
	},
});

export default Page;
