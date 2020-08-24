import React, {useEffect} from 'react';
import {useDispatch} from 'react-redux';
import {createStackNavigator} from '@react-navigation/stack';
import {MainStackParamList} from './MainParamList';
import MuscleTest from '../components/screens/MuscleTest';
import Perimetry from '../components/screens/Perimetry';
import Profile from '../components/screens/Profile';
import Treatment from '../components/screens/Treatment';
import OtherAnnotationsList from '../components/screens/OtherAnnotationsList';
import OtherAnnotations from '../components/screens/OtherAnnotations';
import MuscleTestList from '../components/screens/MuscleTestList';
import PerimetryList from '../components/screens/PerimetryList';
import AddTreatmentSummary from '../components/screens/AddTreatmentSummary';
import Goniometry from '../components/screens/Goniometry';
import GoniometryList from '../components/screens/GoniometryList';
import TermsAndConditions from '../components/screens/TermsAndConditions';
import Patients from '../components/screens/Patients';
import AddDate from '../components/screens/AddDate';
import {
	fetchBodyParts,
	fetchFreshTreatments,
	fetchFreshPatients,
} from '../store/api/actions';
import ListPreviousTreatments from '../components/screens/ListPreviousTreatments';
import SearchBodyPart from '../components/screens/SearchBodyPart';

export const Routes: React.FC = () => {
	const Stack = createStackNavigator<MainStackParamList>();
	const dispatch = useDispatch();
	const options = {
		headerMode: 'none',
		headerShown: false,
	};
	useEffect(() => {
		dispatch(fetchFreshTreatments());
		dispatch(fetchFreshPatients());
		dispatch(fetchBodyParts());
	}, []);

	return (
		<Stack.Navigator
			screenOptions={options}
			initialRouteName='ListPreviousTreatments'>
			<Stack.Screen name='Profile' component={Profile} />
			<Stack.Screen name='Patients' component={Patients} />
			<Stack.Screen name='Treatment' component={Treatment} />
			<Stack.Screen name='OtherAnnotations' component={OtherAnnotations} />
			<Stack.Screen
				name='OtherAnnotationsList'
				component={OtherAnnotationsList}
			/>
			<Stack.Screen name={'MuscleTestList'} component={MuscleTestList} />
			<Stack.Screen name={'MuscleTest'} component={MuscleTest} />
			<Stack.Screen name={'PerimetryList'} component={PerimetryList} />
			<Stack.Screen name={'Perimetry'} component={Perimetry} />
			<Stack.Screen
				name='AddTreatmentSummary'
				component={AddTreatmentSummary}
			/>
			<Stack.Screen name='Goniometry' component={Goniometry} />
			<Stack.Screen name='GoniometryList' component={GoniometryList} />
			<Stack.Screen name='TermsAndConditions' component={TermsAndConditions} />
			<Stack.Screen
				name='ListPreviousTreatments'
				component={ListPreviousTreatments}
			/>
			<Stack.Screen name='AddDate' component={AddDate} />
			<Stack.Screen name='SearchBodyPart' component={SearchBodyPart} />
		</Stack.Navigator>
	);
};
