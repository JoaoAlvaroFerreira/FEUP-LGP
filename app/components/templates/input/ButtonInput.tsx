import React from 'react';
import {View, StyleSheet, Text, TouchableHighlight} from 'react-native';

interface Props {
	label?: string;
	value?: string;
	onPress?: ()=>void;
}

const ButtonInput: React.FC<Props> = ({
	label,
	value,
	onPress
}) => (
	<View style={styles.View}>
		<Text style={styles.Label}>{label}</Text>
		<TouchableHighlight style={styles.Textinput} onPress={onPress}>
			<Text>{value? value: "Adicionar músculo..."}</Text>
        </TouchableHighlight>
	</View>
);

const styles = StyleSheet.create({
	View: {
		marginTop: 20,
	},
	Label: {
		color: '#17224D',
		marginBottom: 10,
	},
	Textinput: {
		borderRadius: 50,
		height: 35,
		paddingLeft: 15,
		paddingRight: 15,
		borderColor: 'grey',
		borderWidth: StyleSheet.hairlineWidth,
		marginTop: 0,
		flex: 1,
    	justifyContent: 'center',
	}
});

export default ButtonInput;
