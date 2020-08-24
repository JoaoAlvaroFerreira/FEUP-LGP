import React from 'react';
import Page from '../../templates/Page';
import FinishButton from '../../templates/button/FinishButton';
import MultiButton, {
	PhoneIcon,
	ArrowIcon,
	EmailIcon,
	MapIcon,
	FileIcon,
	ScheduleIcon,
} from '../../templates/button/MultiButton';
import {MainNavProps} from '../../../routes/MainParamList';
import { Physiotherapist } from '../../../store/physiotherapists/types';


const PhysiotherapistInfo: React.FC<MainNavProps<'PhysiotherapistInfo'>> = ({navigation, route}) => {
	//const physiotherapist = route.params.physiotherapist;
	
	const physiotherapist: Physiotherapist = {
		name: 'Physiotherapist Name',
		email: "email",
		id: "1",
		professional_certificate: '12456789',
		state: 'Busy'
	};

	return (
		<Page title={physiotherapist.name} hasBack={true} hasMargin={true}>
			<MultiButton
				primaryText="+123 456 789"
				secondaryText='Mobile'
				leftIcon={PhoneIcon}
				rightIcon={ArrowIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>
			<MultiButton
				primaryText={physiotherapist.email}
				secondaryText='Email'
				leftIcon={EmailIcon}
				rightIcon={ArrowIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>
			<MultiButton
				primaryText="Placeholder Street"
				secondaryText='Address'
				leftIcon={MapIcon}
				rightIcon={ArrowIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>
			<MultiButton
				primaryText="1234567890"
				secondaryText='NIF'
				leftIcon={ScheduleIcon}
				rightIcon={ArrowIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>
			<MultiButton
				primaryText='Curriculo'
				secondaryText='PDF'
				leftIcon={FileIcon}
				rightIcon={ArrowIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>
			<MultiButton
				primaryText={physiotherapist.professional_certificate}
				secondaryText='Cedula Profissional'
				rightIcon={ArrowIcon}
				onPressRight={() => console.log('TODO: implement')}
			/>
			<MultiButton
				primaryText={physiotherapist.state}
				secondaryText='Estado'
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

export default PhysiotherapistInfo;
