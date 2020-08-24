import React from 'react';
import {StyleSheet, Text, View} from 'react-native';
import {TouchableOpacity} from 'react-native';
import {MaterialIcons, MaterialCommunityIcons} from '@expo/vector-icons';
import {Patient} from '../../store/patients/types';

interface Props {
	patient: Patient;
	onPress: () => void;
}

const PatientInfo: React.FC<Props> = ({patient, onPress}) => (
	<TouchableOpacity style={styles.PatientInfo} onPress={onPress}>
		<View style={styles.Info}>
			<Text style={styles.Name}>
				{patient.firstName + ' ' + patient.lastName}
			</Text>
			<Text style={styles.Sessions}>
				{patient.completedSession} sessões de {patient.numberOfSessions}
			</Text>
		</View>
		<View style={styles.Icons}>
			<View style={styles.IconsWrapper}>
				<TouchableOpacity>
					<MaterialCommunityIcons name='map-marker' size={25} color='#17224D' />
				</TouchableOpacity>
				<TouchableOpacity>
					<MaterialIcons name='call' size={25} color='#17224D' />
				</TouchableOpacity>
			</View>
		</View>
	</TouchableOpacity>
);

const styles = StyleSheet.create({
	PatientInfo: {
		flex: 1,
		flexDirection: 'row',
		marginTop: 20,
		marginLeft: 20,
		marginBottom: 20,
	},
	Info: {
		width: '70%',
		flex: 1,
		flexDirection: 'column',
	},
	Icons: {
		width: '30%',
	},
	IconsWrapper: {
		flex: 1,
		flexDirection: 'row',
		justifyContent: 'space-around',
		alignItems: 'center',
	},
	Name: {
		fontSize: 22,
		marginBottom: 5,
		color: '#17224D',
	},
	Sessions: {
		color: '#73bbfc',
	},
});

export default PatientInfo;
