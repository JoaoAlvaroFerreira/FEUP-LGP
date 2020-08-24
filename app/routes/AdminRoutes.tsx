import React from 'react';
import {createStackNavigator} from '@react-navigation/stack';
import { AdminStackParamList } from './AdminParamList';
import AddDoctor from '../components/screens/adminScreens/AddDoctor';
import PhysiotherapistInfo from '../components/screens/adminScreens/PhysiotherapistInfo';

export const AdminRoutes: React.FC = () => {
	const Stack = createStackNavigator<AdminStackParamList>();
	const options = {
		headerMode: 'none',
		headerShown: false,
		// ...MyTransition
	};

	return (
		<Stack.Navigator screenOptions={options} initialRouteName='PhysiotherapistInfo'>
			<Stack.Screen name='PhysiotherapistInfo' component={PhysiotherapistInfo} />
			<Stack.Screen name='AddDoctor' component={AddDoctor} />
		</Stack.Navigator>
	);
};
