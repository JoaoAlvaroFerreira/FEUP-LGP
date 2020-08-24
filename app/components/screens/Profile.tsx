import React from 'react';
import Page from '../templates/Page';
import FinishButton from '../templates/button/FinishButton';
import {useDispatch} from 'react-redux';
import {useNavigation} from '@react-navigation/native';
import MultiButton, {
	PhoneIcon,
	ArrowIcon,
	EmailIcon,
	MapIcon,
	FileIcon,
} from '../templates/button/MultiButton';
import {MainNavProps} from '../../routes/MainParamList';
import SplitMultiButton, {
	MobileIcon,
	SplitPhoneIcon,
} from '../templates/button/SplitMultiButton';

const Profile: React.FC<MainNavProps<'Profile'>> = ({navigation, route}) => {
	const patient = route.params.patient;

	return (
		<Page title='Perfil' hasBack={true} hasMargin={true}>
			<MultiButton
				primaryText={patient.phone}
				secondaryText='Mobile'
				leftIcon={PhoneIcon}
				rightIcon={ArrowIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>
			<MultiButton
				primaryText={patient.email}
				secondaryText='Email'
				leftIcon={EmailIcon}
				rightIcon={ArrowIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>
			<SplitMultiButton
				leftText='+123 456 789'
				leftSubtitle='Casa'
				rightText='+987 654 321'
				rightSubtitle='Responsável'
				leftIcon={MobileIcon}
				rightIcon={SplitPhoneIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>
			<MultiButton
				primaryText={patient.address.houseNumber + ' ' + patient.address.street}
				secondaryText='Home Address'
				leftIcon={MapIcon}
				rightIcon={ArrowIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>
			<MultiButton
				primaryText='Therapy History'
				secondaryText='PDF'
				leftIcon={FileIcon}
				rightIcon={ArrowIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>

			<FinishButton
				label='Começar tratamento'
				icon='next'
				onPress={() => navigation.navigate('Treatment')}
			/>
		</Page>
	);
};

export default Profile;
