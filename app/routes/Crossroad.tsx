import React from 'react';
import {useSelector} from 'react-redux';
import {AppState} from '../store';
import {NavigationContainer} from '@react-navigation/native';
import {Routes} from './Routes';
import {LoginRoutes} from './LoginRoutes';
import {AdminRoutes} from './AdminRoutes';

export const Crossroad: React.FC = () => {
	const isLogged = useSelector((state: AppState) => state.userStore.isLogged);
	const isAdmin = useSelector((state: AppState) => state.userStore.isAdmin);

	return (
		<NavigationContainer>
			{isLogged ? isAdmin ? <AdminRoutes /> : <Routes /> : <LoginRoutes />}
		</NavigationContainer>
	);
};
