import React from 'react';
import {StyleSheet, Text, View, ViewStyle} from 'react-native';
import {TouchableOpacity} from 'react-native';
import {AntDesign} from '@expo/vector-icons';

interface Props {
	label?: string;
	onPress: () => void;
	icon?: string;
	style?: ViewStyle;
}

const FinishButton: React.FC<Props> = ({label, onPress, icon, style}) => (
	<View style={[styles.FinishButton, style]}>
		<Text style={styles.TextLabel}>{label}</Text>
		<TouchableOpacity style={styles.ButtonComplete} onPress={onPress}>
			<Text style={{color: 'white', textAlign: 'center'}}>
				{icon == 'next' ? (
					<AntDesign name='arrowright' size={25} color='white' />
				) : (
					<AntDesign name='check' size={25} color='white' />
				)}
			</Text>
		</TouchableOpacity>
	</View>
);

const styles = StyleSheet.create({
	FinishButton: {
		display: 'flex',
		flexDirection: 'row',
		alignItems: "center",
		alignSelf: "flex-end",
		marginTop: 20,
		marginRight: 20
	},
	ButtonComplete: {
		backgroundColor: '#842E76',
		width: 50,
		height: 50,
		borderRadius: 50,
		justifyContent: 'center'
	},
	TextLabel: {
		marginRight: 10,
		color: '#842E76',
		fontSize: 20,
		fontWeight: "bold"
	},
});

export default FinishButton;
