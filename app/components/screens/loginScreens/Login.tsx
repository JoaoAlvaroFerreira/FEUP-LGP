import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { View, Text, TouchableHighlight } from 'react-native';
import LoginTextInput from '../../templates/input/LoginTextInput';
import LogoHeader from './LogoHeader';
import { LoginNavProps } from '../../../routes/LoginStackParamList';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import styles from './styles';
import { postLogIn } from '../../../store/api/actions';

const Login = ({ navigation }: LoginNavProps<'Login'>) => {
	const dispatch = useDispatch();
	const [email, setEmail] = useState('');
	const [password, setPw] = useState('');

	const forgotPassword = () => {
		navigation.navigate('Recover');
	};

	return (
		<View style={{ flex: 1 }}>
			<LogoHeader />
			<View style={styles.InputDivision}>
				<KeyboardAwareScrollView
					contentContainerStyle={{ flex: 1 }}
					extraScrollHeight={10}>
					<LoginTextInput
						placeholder='Email'
						value={email}
						onChange={(user) => setEmail(user)}
						autoCapitalize='none'
						textContentType={'username'}
					/>
					<LoginTextInput
						placeholder='Password'
						value={password}
						onChange={(password) => setPw(password)}
						autoCapitalize='none'
						textContentType={'password'}
						secureTextEntry={true}
					/>
					<View
						style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
						<TouchableHighlight
							style={styles.AuthButtons}
							onPress={() => {
								dispatch(postLogIn(email, password));
							}}
							underlayColor='#338DFF'>
							<Text style={{ color: 'white', fontSize: 20 }}>Login</Text>
						</TouchableHighlight>
					</View>
					<View style={{ flex: 0.5, alignItems: 'center', marginTop: '5%' }}>
						<TouchableHighlight
							onPress={forgotPassword}
							underlayColor='#E4FCFC'>
							<Text style={{ fontSize: 15, color: '#0059FF' }}>
								Esqueci-me da Password
							</Text>
						</TouchableHighlight>
					</View>
				</KeyboardAwareScrollView>
			</View>
		</View>
	);
};

export default Login;
