import React from 'react';
import {StyleSheet, Text, View} from 'react-native';
import {TouchableOpacity} from 'react-native';
import {MaterialIcons, Zocial} from '@expo/vector-icons';
import {Treatment} from '../../store/treatment/types';

type HistoryProps = {
	treatment: Treatment;
	last: boolean;
	navigate: () => void;
};

const TreatmentHistory: React.FC<HistoryProps> = ({
	treatment,
	last,
	navigate,
}) => {
	const optionsDate = {
		weekday: 'long',
		year: 'numeric',
		month: 'long',
		day: 'numeric',
	};
	return (
		<View style={styles.CardWrapper}>
			<View style={styles.BulletPoint}></View>
			{!last && <View style={styles.BulletLine}></View>}

			<View style={treatment.isOpen ? styles.Card : styles.CardFixed}>
				<View style={{flex: 4}}>
					<Text style={styles.PatientName}> {treatment.patientName} </Text>
					<Text>
						{' '}
						{treatment.startDate.toLocaleDateString(
							undefined,
							optionsDate
						)}{' '}
					</Text>
				</View>

				<View style={{flex: 1, justifyContent: 'center', marginRight: 0}}>
					<Text>
						{treatment.startDate.getHours() +
							':' +
							(treatment.startDate?.getMinutes() < 10 ? '0' : '') +
							treatment.startDate?.getMinutes()}
					</Text>
				</View>

				<View style={{flex: 1, justifyContent: 'center'}}>
					<TouchableOpacity onPress={navigate}>
						{treatment.isOpen ? (
							<MaterialIcons name='edit' size={25} color='#17224D' />
						) : (
							<Zocial name='acrobat' size={20} color='#17224D' />
						)}
					</TouchableOpacity>
				</View>
			</View>
		</View>
	);
};

const styles = StyleSheet.create({
	CardWrapper: {
		paddingLeft: 50,
		paddingRight: 10,
		paddingTop: 30,
		position: 'relative',
	},
	Card: {
		width: '100%',
		backgroundColor: '#FFFFFF',
		borderRadius: 50,
		paddingLeft: 25,
		paddingTop: 10,
		paddingBottom: 10,
		flexDirection: 'row',
	},
	CardFixed: {
		width: '100%',
		backgroundColor: '#5581BB',
		borderRadius: 50,
		paddingLeft: 25,
		paddingTop: 10,
		paddingBottom: 10,
		flexDirection: 'row',
	},
	BulletPoint: {
		position: 'absolute',
		top: 53,
		left: 18,
		backgroundColor: '#FFFFFF',
		width: 15,
		height: 15,
		borderRadius: 50,
	},
	BulletLine: {
		borderLeftColor: '#FFFFFF',
		borderLeftWidth: 1,
		height: '150%',
		position: 'absolute',
		top: 60,
		left: 25,
	},
	PatientName: {
		fontWeight: 'bold',
		paddingBottom: 10,
	},
});

export default TreatmentHistory;
