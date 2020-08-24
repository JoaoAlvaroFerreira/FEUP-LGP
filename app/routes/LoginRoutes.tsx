import React from 'react';
import {createStackNavigator} from '@react-navigation/stack';
import Login from '../components/screens/loginScreens/Login';
import RecoverPw from '../components/screens/loginScreens/RecoverPw';
import {LoginStackParamList} from './LoginStackParamList';

export const LoginRoutes: React.FC = () => {
	const Stack = createStackNavigator<LoginStackParamList>();
	const options = {
		headerMode: 'none',
		headerShown: false,
		// ...MyTransition
	};

	return (
		<Stack.Navigator screenOptions={options} initialRouteName='Login'>
			<Stack.Screen name='Login' component={Login} />
			<Stack.Screen name='Recover' component={RecoverPw} />
		</Stack.Navigator>
	);
};
