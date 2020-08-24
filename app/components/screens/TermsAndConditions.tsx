import React from 'react';
import {StyleSheet, Text, View, FlatList} from 'react-native';
import Page from '../templates/Page';
import FinishButton from '../templates/button/FinishButton';
import {MainNavProps} from '../../routes/MainParamList';

const TermsAndConditions = ({
	navigation,
	route,
}: MainNavProps<'TermsAndConditions'>) => {
	const termsAndConditionsText =
		'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ornare nunc ac nunc porta, eu tincidunt quam hendrerit. Nulla turpis mauris, venenatis in tellus sed, sollicitudin accumsan turpis. Praesent aliquet risus in urna sodales aliquet. Proin hendrerit convallis tempus. Nam a egestas sapien. Nulla pharetra, metus nec fringilla accumsan, ante nulla ultricies nisl, varius ultricies sapien mauris vel tellus. Nulla molestie lorem venenatis, hendrerit odio in, ornare erat. Etiam sagittis erat vehicula est tincidunt iaculis. Integer ac ullamcorper nunc. Sed pellentesque vel metus vitae feugiat. Nam non erat vulputate, porttitor libero vel, suscipit magna. Etiam nec convallis libero, vel dignissim elit. Sed nibh neque, rutrum blandit nisi id, dictum ornare nunc. Maecenas semper risus id sodales consectetur. Phasellus venenatis tempor ullamcorper. Proin lectus ipsum, sagittis id varius eget, iaculis et ex. Nulla vitae tortor sed erat sagittis congue. In congue posuere quam in egestas. Aenean id felis tincidunt, cursus est scelerisque, varius diam. Vivamus id vestibulum massa, ut porta sapien. Aenean bibendum pellentesque risus eu blandit. Phasellus libero quam, finibus sit amet semper id, pretium sit amet justo. Mauris nec nisi a metus vehicula ullamcorper. Vestibulum pharetra nibh velit, ultrices commodo lectus varius at. Donec vulputate ultrices tellus, in molestie massa consequat et. Proin et lobortis purus. Nullam vulputate tincidunt justo et rutrum. In quis tellus libero. In tincidunt id velit et fermentum. Nullam sagittis nunc a velit euismod, quis gravida elit accumsan. Aenean et tellus aliquet, ornare augue a, gravida dolor. ';

	const accept = () => {
		route.params?.onSave();
		navigation.navigate('Profile'); //change it to "Mark Appointment as over"
	};

	const _renderItem = () => (
		<Text style={styles.Text}>{termsAndConditionsText}</Text>
	);

	return (
		<Page
			title='Termos de Responsabilidade'
			hasBack={true}
			hasMargin={true}>
			<View style={styles.Box}>
				<FlatList
				data={[{styleText: styles.Text}]}
				renderItem={_renderItem}
				keyExtractor={(item, index) => index.toString()}
				/>
			</View>

			<FinishButton label='Aceito' onPress={accept} />
		</Page>
	);
};

export default TermsAndConditions;

const styles = StyleSheet.create({
	Box: {
		marginHorizontal: 15,
		marginVertical: 15,
		paddingVertical: 15,
		paddingHorizontal: 15,
		backgroundColor: '#fff',
		borderRadius: 20,
		elevation: 5,
		flex: 1,
		flexDirection: 'row',
		alignItems: 'stretch',
	},
	Text: {
		lineHeight: 30,
		textAlign: 'justify',
	},
});
