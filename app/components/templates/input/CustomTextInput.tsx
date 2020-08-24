import React from 'react';
import {View, StyleSheet, Text, TextInput} from 'react-native';

interface Props {
	label?: string;
	value?: string;
	placeholder?: string;
	onChange: (text: string) => void;
}

const CustomTextInput: React.FC<Props> = ({
	label,
	value,
	onChange,
	placeholder,
}) => (
	<View style={styles.View}>
		<Text style={styles.Label}>{label}</Text>
		<TextInput
			style={styles.Textinput}
			placeholder={placeholder}
			value={value}
			onChangeText={onChange}
		/>
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
		color: 'black',
		borderRadius: 50,
		height: 35,
		paddingLeft: 15,
		paddingRight: 15,
		borderColor: 'grey',
		borderWidth: StyleSheet.hairlineWidth,
		marginTop: 0,
	},
});

export default CustomTextInput;
