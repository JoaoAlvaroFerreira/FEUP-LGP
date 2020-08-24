import React from 'react';
import { View, StyleSheet, TextInput, TouchableWithoutFeedback, Keyboard } from 'react-native';

interface Props {
	value: string;
	placeholder?: string;
	onChange: (text: string) => void;
	autoCapitalize?: any;
	textContentType?: any;
	secureTextEntry?: boolean;
}

const LoginTextInput: React.FC<Props> = ({
	value,
	onChange,
	placeholder,
	autoCapitalize,
	textContentType,
	secureTextEntry
}) => (
		<TouchableWithoutFeedback onPress={Keyboard.dismiss}>
			<View
				style={styles.View}>
				<TextInput
					style={styles.Textinput}
					placeholder={placeholder}
					value={value}
					onChangeText={onChange}
					autoCapitalize={autoCapitalize}
					textContentType={textContentType}
					secureTextEntry={secureTextEntry}
				/>
			</View>
		</TouchableWithoutFeedback>
	);

const styles = StyleSheet.create({
	View: {
		flex: 1,
		alignItems: "center",
		justifyContent: "center"
	},
	Textinput: {
		color: 'black',
		borderRadius: 50,
		height: "50%",
		width: "85%",
		paddingLeft: 15,
		borderColor: 'grey',
		borderWidth: StyleSheet.hairlineWidth,
	},
});

export default LoginTextInput;
