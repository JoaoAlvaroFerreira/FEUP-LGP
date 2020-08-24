import React from 'react';
import {StyleSheet, Text, View, FlatList} from 'react-native';
import {useSelector, useDispatch} from 'react-redux';
import accents from 'remove-accents';
import Page from '../templates/Page';
import PatientInfo from '../templates/PatientInfo';
import {AppState} from '../../store';
import {MainNavProps} from '../../routes/MainParamList';
import {Patient} from '../../store/patients/types';
import {fetchPatients, fetchFreshPatients} from '../../store/api/actions';

const Patients = ({navigation}: MainNavProps<'Patients'>) => {
	const patientStore = useSelector((state: AppState) => state.patientsStore);
	const firstLetter = (patient: Patient): string =>
		accents.remove(patient.firstName.charAt(0).toUpperCase());
	const dispatch = useDispatch();

	return (
		<Page
			title='Os Meus Pacientes'
			hasBack={true}
			search={(text: string) => {
				console.log('Searching: ' + text);
			}} // TODO: This has to go to redux
		>
			<FlatList
				data={patientStore.patients}
				renderItem={({item: patient, index}) => (
					<View>
						{(index == 0 ||
							firstLetter(patient) !==
								firstLetter(patientStore.patients[index - 1])) && (
							<Text key={`letter_${index}`} style={styles.letter}>
								{firstLetter(patient)}
							</Text>
						)}

						<PatientInfo
							key={`patient_${index}`}
							patient={patient}
							onPress={() => navigation.navigate('Profile', {patient})}
						/>
					</View>
				)}
				keyExtractor={(patient) => patient.id}
				refreshing={patientStore.isFetching}
				onRefresh={() => dispatch(fetchFreshPatients())}
				onEndReached={() => dispatch(fetchPatients())}
				onEndReachedThreshold={2}
			/>
		</Page>
	);
};

const styles = StyleSheet.create({
	letter: {
		backgroundColor: '#17224D',
		marginRight: -20,
		color: 'white',
		paddingLeft: 20,
		paddingTop: 8,
		paddingBottom: 8,
		fontWeight: 'bold',
	},
});

export default Patients;
