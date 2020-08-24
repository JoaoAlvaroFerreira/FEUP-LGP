import React from 'react';
import {View, Image, Text, StyleSheet, TouchableOpacity} from 'react-native';
import {AntDesign} from '@expo/vector-icons';

interface Props {
	onPress?: any;
	hasBack?: boolean;
}

const LogoHeader: React.FC<Props> = ({onPress, hasBack}) => {
	return (
		<View style={styles.TopDivision}>
			{hasBack && (
				<View style={styles.ReturnButton}>
					<TouchableOpacity style={styles.ReturnButton} onPress={onPress}>
						<AntDesign name='arrowleft' size={25} color='white' />
					</TouchableOpacity>
				</View>
			)}
			<Image style={styles.MartinLogo} source={require('./logo.png')} />
			<View>
				<Text style={{fontSize: 45, fontWeight: 'bold', color: 'white'}}>
					Bem Vindo
				</Text>
			</View>
		</View>
	);
};

export default LogoHeader;

const styles = StyleSheet.create({
	MartinLogo: {
		width: '70%',
		height: '50%',
		marginTop: '5%',
		resizeMode: 'center',
		aspectRatio: 1,
	},
	TopDivision: {
		backgroundColor: '#17224D',
		flex: 4,
		alignItems: 'center',
		justifyContent: 'center',
	},
	ReturnButton: {
		backgroundColor: 'red',
		alignSelf: 'flex-start',
		paddingLeft: '2%',
	},
});
