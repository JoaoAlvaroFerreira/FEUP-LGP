import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { TouchableOpacity } from 'react-native';
import Page from '../templates/Page';
import TreatmentHistory from '../templates/TreatmentHistory';
import { AppState } from '../../store';
import { useSelector } from 'react-redux';
import { MainNavProps } from '../../routes/MainParamList';

const ListPreviousTreatments: React.FC<MainNavProps<'ListPreviousTreatments'>> = ({ navigation }) => {
	const treatments = useSelector(
		(state: AppState) => state.treatmentStore.treatments
	);
	const userName = useSelector((state: AppState) => state.userStore.lastName);

	return (
		<Page title={`Bom dia, ${userName}!`} hasLogout>
			<View>
				<View style={styles.Navbar}>
					<TouchableOpacity style={styles.Button}>
						<Text
							style={{
								color: 'white',
								textAlign: 'center',
								marginTop: 5,
								fontSize: 15,
								fontWeight: 'bold',
							}}>
							Cronologia
						</Text>
					</TouchableOpacity>
					<TouchableOpacity style={styles.Button}>
						<Text
							style={{
								color: 'white',
								textAlign: 'center',
								marginTop: 5,
								fontSize: 15,
							}}>
							Informações
						</Text>
					</TouchableOpacity>
				</View>

				<View style={styles.Content}>
					{treatments.map((t, index) => (
						<TreatmentHistory
							key={index}
							treatment={t}
							navigate={() => navigation.navigate('Treatment', { treatment: t })}
							last={!(index < treatments.length - 1)}
						/>
					))}
				</View>
			</View>
		</Page>
	);
};

const styles = StyleSheet.create({
	Navbar: {
		height: 70,
		flexDirection: 'row',
		borderBottomColor: '#FFFFFF',
		borderBottomWidth: 1,
	},
	Button: {
		flex: 1,
		justifyContent: 'center',
		backgroundColor: '#17224D',
		alignItems: 'center',
	},
	Content: {
		backgroundColor: '#17224D',
		height: '300%',
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
	CardWrapper: {
		paddingLeft: 50,
		paddingRight: 10,
		paddingTop: 30,
		position: 'relative',
	},
});

export default ListPreviousTreatments;
