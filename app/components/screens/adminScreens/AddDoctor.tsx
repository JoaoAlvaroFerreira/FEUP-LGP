import React from 'react';
import {Formik} from 'formik';
import CustomTextInput from '../../templates/input/CustomTextInput';
import Page from '../../templates/Page';
import {useNavigation} from '@react-navigation/native';
import FinishButton from '../../templates/button/FinishButton';

interface FormValues {
	name: string;
	email: string;
	cp: string;
	status: string;
}

const AddDoctor: React.FC = () => {
	const navigation = useNavigation();
	const initialValues: FormValues = {name: '', email: '', cp: '', status: ''};

	return (
		<Formik // TODO rewite all forms that use Formik to use withFormik
			initialValues={initialValues}
			onSubmit={(values) => {
				console.log(values);
			}} // TODO dispatch action
		>
			{({handleChange, handleSubmit, values}) => (
				<Page title='Médicos' hasBack={true} hasMargin={true}>
					<CustomTextInput
						label='Nome'
						onChange={handleChange('name')}
						value={values.name}
					/>
					<CustomTextInput
						label='E-mail'
						onChange={handleChange('email')}
						value={values.email}
					/>
					<CustomTextInput
						label='Cédula Profissional'
						onChange={handleChange('cp')}
						value={values.cp}
					/>
					<CustomTextInput
						label='Estado'
						onChange={handleChange('status')}
						value={values.status}
					/>

					<FinishButton label='' onPress={handleSubmit} />
				</Page>
			)}
		</Formik>
	);
};

export default AddDoctor;
