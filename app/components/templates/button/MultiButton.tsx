import React, { ReactElement } from 'react';
import { View, StyleSheet, Text } from 'react-native';
import {
	Ionicons,
	MaterialIcons,
	MaterialCommunityIcons,
	Entypo,
	Feather,
} from '@expo/vector-icons';
import { TouchableHighlight } from 'react-native-gesture-handler';

interface Props {
	primaryText: string;
	onPressRight: () => void;
	rightIcon: ReactElement;
	onPressLeft?: () => void;
	secondaryText?: string;
	leftIcon?: ReactElement;
}

const MultiButton: React.FC<Props> = ({
	primaryText,
	secondaryText,
	onPressRight,
	onPressLeft,
	rightIcon,
	leftIcon,
}) => (
	<View style={styles.MultiButton}>
		<View style={styles.RightSide}>
			<View style={{marginRight: 10}}>
				{leftIcon &&
					(onPressLeft ? (
						<TouchableHighlight onPress={onPressLeft}>
							{leftIcon}
						</TouchableHighlight>
					) : (
						leftIcon
					))}
			</View>

			{secondaryText == null ? (
				<Text style={{fontSize: 20}}>{primaryText}</Text>
			) : (
				<View style={styles.Column}>
					<Text style={{fontSize: 20}}>{primaryText}</Text>
					<Text style={{color: '#808080', fontSize: 15}}>{secondaryText}</Text>
				</View>
			)}
		</View>

		<View>
			<TouchableHighlight onPress={onPressRight} underlayColor='transparent'>
				{rightIcon}
			</TouchableHighlight>
		</View>
		</View>
	);

const styles = StyleSheet.create({
	MultiButton: {
		height: 80,
		padding: 20,
		marginBottom: 20,
		flexDirection: 'row',
		alignItems: 'center',
		justifyContent: 'space-between',
		backgroundColor: '#fff',
		borderRadius: 50,
		shadowColor: '#000',
		shadowOffset: { width: 1, height: 4 },
		shadowOpacity: 0.3,
		shadowRadius: 4,
		elevation: 5,
	},
	RightSide: {
		flexDirection: 'row',
		alignItems: 'center',
	},
	CheckBoxIcon: {
		marginRight: 10,
	},
	Column: {
		flexDirection: 'column',
	},
});

export const ArrowIcon = (
	<Ionicons name='ios-arrow-forward' size={35} color='#17224D' />
);
export const EditIcon = <MaterialIcons name='edit' size={35} color='#17224D' />;
export const CheckBoxIcon = (
	<MaterialCommunityIcons
		name='checkbox-blank-outline'
		size={35}
		color='#17224D'
		style={styles.CheckBoxIcon}
	/>
);
export const CalendarIcon = (
	<MaterialIcons name='today' size={35} color='#17224D' />
);
export const ScheduleIcon = (
	<MaterialIcons name='schedule' size={35} color='#17224D' />
);
export const PhoneIcon = <Entypo name='phone' size={35} color='#17224D' />;
export const EmailIcon = <Entypo name='mail' size={35} color='#17224D' />;
export const MapIcon = <Feather name='map-pin' size={35} color='#17224D' />;
export const FileIcon = (
	<MaterialCommunityIcons name='file-pdf' size={35} color='#17224D' />
);

export default MultiButton;
