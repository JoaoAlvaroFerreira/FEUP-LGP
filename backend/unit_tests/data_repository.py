"""
Repository of test data
"""
from rest_framework.test import APIRequestFactory

class GoniometryDataRepository:
    """
    Repository of goniometries requests examples
    """

    @staticmethod
    def get_valid_goniometry():
        """
        Valid goniometry request
        """

        return {'body_zone': 'fcf1a46e-352a-468d-ada2-358464154b76', 'min_abduction': 100,
                'max_abduction': 115, 'min_adduction': 80, 'max_adduction': 120, 'min_flexion': 50,
                'max_flexion': 140, 'min_rotation': 57, 'max_rotation': 170, 'min_extension': 20,
                'max_extension': 134}

    @staticmethod
    def get_missing_member_goniometry():
        """
        Goniometry request with a missing member field
        """

        return {'body_zone': 'fcf1a46e-352a-468d-ada2-358464154b76', 'min_abduction': 100,
                'max_abduction': 115, 'min_adduction': 80, 'max_adduction': 120, 'min_flexion': 50,
                'max_flexion': 140, 'min_rotation': 57, 'max_rotation': 170, 'min_extension': 20,
                'max_extension': 134}

    @staticmethod
    def get_missing_body_zone_goniometry():
        """
        Goniometry request with a missing body zone field
        """

        return {'min_abduction': 100,
                'max_abduction': 115, 'min_adduction': 80, 'max_adduction': 120, 'min_flexion': 50,
                'max_flexion': 140, 'min_rotation': 57, 'max_rotation': 170, 'min_extension': 20,
                'max_extension': 134}

    @staticmethod
    def get_invalid_values_goniometry():
        """
       Goniometry request with a value outside the allowed range
       """

        return {'body_zone': 'fcf1a46e-352a-468d-ada2-358464154b76', 'min_abduction': 100,
                'max_abduction': 115, 'min_adduction': 190, 'max_adduction': 120, 'min_flexion': 50,
                'max_flexion': 140, 'min_rotation': 57, 'max_rotation': 170, 'min_extension': 20,
                'max_extension': 134}

    @staticmethod
    def get_invalid_minmax_goniometry():
        """
        Goniometry request with a minimum value greater than the respective maximum
        """

        return {'body_zone': 'fcf1a46e-352a-468d-ada2-358464154b76', 'min_abduction': 100,
                'max_abduction': 115, 'min_adduction': 80, 'max_adduction': 120, 'min_flexion': 150,
                'max_flexion': 140, 'min_rotation': 57, 'max_rotation': 170, 'min_extension': 20,
                'max_extension': 134}


class MuscleTestDataRepository:
    """
    Repository of muscle tests requests examples
    """

    @staticmethod
    def get_valid_muscle_test():
        """
        Valid muscle test request
        """

        return {'body_zone': 'fcf1a46e-352a-468d-ada2-358464154b76', 'strength': 3}

    @staticmethod
    def get_missing_member_muscle_test():
        """
        Muscle test request with a missing member field
        """

        return {'body_zone': 'fcf1a46e-352a-468d-ada2-358464154b76', 'strength': 3}

    @staticmethod
    def get_missing_body_zone_muscle_test():
        """
        Muscle test request with a missing body zone field
        """

        return {'strength': 3}

    @staticmethod
    def get_missing_strength_muscle_test():
        """
        Muscle test request with a missing strength field
        """

        return {'body_zone': 'Test Body Zone'}

    @staticmethod
    def get_invalid_strength_muscle_test():
        """
        Muscle test request with a strength value outside the allowed range
        """

        return {'body_zone': 'fcf1a46e-352a-468d-ada2-358464154b76', 'strength': 6}


class PerimetryDataRepository:
    """
    Repository of perimetry requests examples
    """

    @staticmethod
    def get_valid_perimetry():
        """
        Valid perimetry request
        """

        return {'body_zone': 'fcf1a46e-352a-468d-ada2-358464154b76', 'size': 150}

    @staticmethod
    def get_missing_member_perimetry():
        """
        Perimetry request with a missing member field
        """

        return {'body_zone': 'fcf1a46e-352a-468d-ada2-358464154b76', 'size': 150}

    @staticmethod
    def get_missing_body_zone_perimetry():
        """
        Perimetry request with a missing body zone field
        """

        return {'size': 150}

    @staticmethod
    def get_missing_size_perimetry():
        """
        Perimetry request with a missing strength field
        """

        return {'member': 'Test Member', 'body_zone': 'Test Body Zone'}

    @staticmethod
    def get_invalid_size_perimetry():
        """
        Perimetry request with a size value outside the allowed range
        """

        return {'body_zone': 'fcf1a46e-352a-468d-ada2-358464154b76', 'strength': 350}


class TreatmentDataRepository:
    """
    Repository of treatment requests examples
    """

    @staticmethod
    def get_valid_treatment():
        """
        Valid treatment request
        """

        return {'start_date': '2020-03-21 18:47:15.000000', 'end_date': '2020-03-21 18:57:15.000000',
                'summary': 'This is a summary', 'pain_level': 2,
                'medication': 'This is the medication', 'treatment': 'This is the treatment',
                'periodic_evaluation': 'This is the weekly evaluation', 'perimetries': [],
                'muscle_tests': [], 'goniometries': []}

    @staticmethod
    def get_missing_start_date_treatment():
        """
        Treatment request with a missing start date field
        """

        return {'end_date': '2020-03-21 18:57:15.000000',
                'summary': 'This is a summary', 'pain_level': 2,
                'medication': 'This is the medication', 'treatment': 'This is the treatment',
                'periodic_evaluation': 'This is the weekly evaluation', 'perimetries': [],
                'muscle_tests': [], 'goniometries': []}

    @staticmethod
    def get_invalid_end_date_treatment():
        """
        Treatment request with a end date before the start date
        """

        return {'start_date': '2020-03-21 19:47:15.000000', 'end_date': '2020-03-21 18:57:15.000000',
                'summary': 'This is a summary', 'pain_level': 2,
                'medication': 'This is the medication', 'treatment': 'This is the treatment',
                'periodic_evaluation': 'This is the weekly evaluation', 'perimetries': [],
                'muscle_tests': [], 'goniometries': []}

    @staticmethod
    def get_invalid_pain_level_treatment():
        """
        Treatment request with a pain level value outside the allowed range
        """

        return {'start_date': '2020-03-21 19:47:15.000000', 'end_date': '2020-03-21 18:57:15.000000',
                'summary': 'This is a summary', 'pain_level': 12,
                'medication': 'This is the medication', 'treatment': 'This is the treatment',
                'periodic_evaluation': 'This is the weekly evaluation', 'perimetries': [],
                'muscle_tests': [], 'goniometries': []}


class DoctorDataRepository:
    """
    Repository of doctor requests examples
    """

    @staticmethod
    def get_valid_doctor_request():
        """
        Valid doctor request
        """

        return {'name': 'Test Doctor', 'professional_certificate': 'fkri3wajo7et4od', 'email': 'doctor@test.com',
                'state_id': 'fcf1a46e-352a-468d-ada2-358464154b76'}

    @staticmethod
    def get_missing_name_doctor_request():
        """
        Doctor request with a missing name field
        """

        return {'professional_certificate': 'fkri3wajo7et4od', 'email': 'doctor@test.com',
                'state_id': 'fcf1a46e-352a-468d-ada2-358464154b76'}

    @staticmethod
    def get_missing_professional_certificate_doctor_request():
        """
        Doctor request with a missing professional certificate field
        """

        return {'name': 'Test Doctor', 'email': 'doctor@test.com',
                'state_id': 'fcf1a46e-352a-468d-ada2-358464154b76'}

    @staticmethod
    def get_too_long_professional_certificate_doctor_request():
        """
        Doctor request with a professional certificate field too long
        """

        return {'name': 'Test Doctor', 'professional_certificate': 'fkri3wajo7et4odff', 'email': 'doctor@test.com',
                'state_id': 'fcf1a46e-352a-468d-ada2-358464154b76'}

    @staticmethod
    def get_missing_email_doctor_request():
        """
        Doctor request with a missing email field
        """

        return {'name': 'Test Doctor', 'professional_certificate': 'fkri3wajo7et4od',
                'state_id': 'fcf1a46e-352a-468d-ada2-358464154b76'}

    @staticmethod
    def get_invalid_email_doctor_request():
        """
        Doctor request with a invalid email field
        """

        return {'name': 'Test Doctor', 'professional_certificate': 'fkri3wajo7et4od', 'email': 'doctor@test',
                'state_id': 'fcf1a46e-352a-468d-ada2-358464154b76'}

    @staticmethod
    def get_missing_state_doctor_request():
        """
        Doctor request with a missing state field
        """

        return {'name': 'Test Doctor', 'professional_certificate': 'fkri3wajo7et4od', 'email': 'doctor@test.com'}


class PatientDataRepository:
    """
    Repository of patient request examples
    """

    @staticmethod
    def get_valid_patient():
        """
        Valid patient request
        """

        return {
            'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
            "nif": "1336663",
            "first_name": "Pedro",
            "last_name": "Roxo",
            "birth_date": "1950-03-21",
            "telephone_number": "960234567",
            "email": "ttJz@maiil.com",
            "gender": "m",
            "profession": "Officer",
            "clinical_history": "We used some ointments on her.",
            "diagnostic": "Bad elbow"
        }

    @staticmethod
    def get_missing_profession_person():
        """
        Patient request missing profession
        """

        return {
            'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
            "nif": "1396163",
            "first_name": "Pedro",
            "last_name": "Roxo",
            "birth_date": "1950-03-21",
            "telephone_number": "960234567",
            "email": "ttJzz@maiil.com",
            "gender": "m",
            "clinical_history": "We used some ointments on her.",
            "diagnostic": "Bad elbow"
        }

    @staticmethod
    def get_missing_diagnostic_person():
        """
        Patient request missing diagnostic
        """

        return {
            'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
            "nif": "1330660",
            "first_name": "Pedro",
            "last_name": "Roxo",
            "birth_date": "1950-03-21",
            "telephone_number": "960234567",
            "email": "moic@maiil.com",
            "gender": "m",
            "profession": "Officer",
            "clinical_history": "We used some ointments on her."
        }

    @staticmethod
    def get_missing_clinical_history_person():
        """
        Patient request missing clinical_history
        """

        return {
            'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
            "nif": "000000",
            "first_name": "Pedro",
            "last_name": "Roxo",
            "birth_date": "1950-03-21",
            "telephone_number": "960234567",
            "email": "ttJz@completemail.com",
            "gender": "m",
            "profession": "Officer",
            "diagnostic": "Bad elbow"
        }


class AdministratorDataRepository:
    """
    Repository of administrator requests examples
    """

    @staticmethod
    def get_valid_administrator():
        """
        Valid administrator request
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'nif': '111222333', 'first_name': 'Pedro',
                'last_name': 'Antunes', 'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test1@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_street_administrator():
        """
        Administrator request with a missing street field
        """

        return {'address':{'city': 'Porto', 'zip_code': '4465-123'}, 'nif': '211222333', 'first_name': 'Pedro',
                'last_name': 'Antunes', 'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test2@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_city_administrator():
        """
        Administrator request with a missing city field
        """

        return {'address':{'street': 'Rua Oliveira Gaio', 'zip_code': '4465-123'}, 'nif': '311222333',
                'first_name': 'Pedro', 'last_name': 'Antunes', 'birth_date': '2000-03-21',
                'telephone_number': '961234567', 'email': 'test3@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_nif_administrator():
        """
        Administrator request with a missing nif field
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'first_name': 'Pedro', 'last_name': 'Antunes', 'birth_date': '2000-03-21',
                'telephone_number': '961234567', 'email': 'test4@email.com',
                'gender': 'm', 'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_first_name_administrator():
        """
        Administrator request with a missing first name field
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'nif': '511222333', 'last_name': 'Antunes', 'birth_date': '2000-03-21',
                'telephone_number': '961234567', 'email': 'test5@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_last_name_administrator():
        """
        Administrator request with a missing last name field
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'nif': '611222333', 'first_name': 'Pedro',
                'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test6@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_birth_date_administrator():
        """
        Administrator request with a missing birth date field
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'nif': '711222333', 'first_name': 'Pedro',
                'last_name': 'Antunes', 'telephone_number': '961234567',
                'email': 'test7@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_telephone_number_administrator():
        """
        Administrator request with a missing telephone number field
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'nif': '811222333', 'first_name': 'Pedro',
                'last_name': 'Antunes', 'birth_date': '2000-03-21',
                'email': 'test8@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_email_administrator():
        """
        Administrator request with a missing email field
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'nif': '911222333', 'first_name': 'Pedro',
                'last_name': 'Antunes', 'birth_date': '2000-03-21',
                'telephone_number': '961234567', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_gender_administrator():
        """
        Administrator request with a missing gender field
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'nif': '121222333', 'first_name': 'Pedro',
                'last_name': 'Antunes', 'birth_date': '2000-03-21',
                'telephone_number': '961234567', 'email': 'test10@email.com',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_zip_code_administrator():
        """
        Administrator request with a missing zip code field
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto'},
                'nif': '141222333', 'first_name': 'Pedro',
                'last_name': 'Antunes', 'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test12@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_invalid_email_administrator():
        """
        Administrator request with a invalid email value
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'nif': '151222333', 'first_name': 'Pedro',
                'last_name': 'Antunes', 'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test13email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_invalid_gender_administrator():
        """
        Administrator request with a invalid gender
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'nif': '161222333', 'first_name': 'Pedro',
                'last_name': 'Antunes', 'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test14@email.com', 'gender': 'z',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_invalid_birth_date_administrator():
        """
        Administrator request with a birth date after current date
        """

        return {'address': {'street': 'Rua Oliveira Gaio', 'city': 'Porto', 'zip_code': '4465-123'},
                'nif': '171222333', 'first_name': 'Pedro',
                'last_name': 'Antunes', 'birth_date': '2999-01-01', 'telephone_number': '961234567',
                'email': 'test15@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}


class AddressDataRepository:
    """
    Repository of addresses requests examples
    """

    @staticmethod
    def get_valid_address():
        """
        Valid address request
        """

        return {'street': 'Rua cidade', 'zip_code': '1234-123', 'city': 'Porto'}

    @staticmethod
    def get_missing_street_address():
        """
        Address request with a missing street field
        """

        return {'zip_code': '1234-123', 'city': 'Porto'}

    @staticmethod
    def get_missing_zip_code_address():
        """
        Address request with a missing zip code field
        """

        return {'street': 'Rua cidade', 'city': 'Porto'}

    @staticmethod
    def get_missing_city_address():
        """
       Address request with a missing city field
       """

        return {'street': 'Rua cidade', 'zip_code': '1234-123'}


class CredentialDataRepository:
    """
    Repository of credentials requests examples
    """

    @staticmethod
    def get_valid_credential():
        """
        Valid credential request
        """

        return {'email': 'email@gmail.com', 'password': 'secure_password'}

    @staticmethod
    def get_missing_email_credential():
        """
        Credential request with a missing password field
        """

        return {}


class PersonDataRepository:
    """
    Repository of person requests examples
    """

    @staticmethod
    def get_valid_person():
        """
        Valid person request
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'nif': '111222333', 'first_name': 'Pedro', 'last_name': 'Antunes',
                'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test1@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_nif_person():
        """
        Person request with a missing nif field
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'first_name': 'Pedro', 'last_name': 'Antunes',
                'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test1@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_first_name_person():
        """
        Person request with a missing first name field
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'nif': '111222333', 'last_name': 'Antunes',
                'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test1@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_last_name_person():
        """
        Person request with a missing last name field
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'nif': '111222333', 'first_name': 'Pedro',
                'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test1@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_birth_date_person():
        """
        Person request with a missing birth date field
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'nif': '111222333', 'first_name': 'Pedro', 'last_name': 'Antunes',
                'telephone_number': '961234567',
                'email': 'test1@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_telephone_number_person():
        """
        Person request with a missing telephone number field
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'nif': '111222333', 'first_name': 'Pedro', 'last_name': 'Antunes',
                'birth_date': '2000-03-21',
                'email': 'test1@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_email_person():
        """
        Person request with a missing email field
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'nif': '111222333', 'first_name': 'Pedro', 'last_name': 'Antunes',
                'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_missing_gender_person():
        """
        Person request with a missing gender field
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'nif': '111222333', 'first_name': 'Pedro', 'last_name': 'Antunes',
                'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test1@email.com',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_invalid_email_person():
        """
        Person request with a invalid email value
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'nif': '111222333', 'first_name': 'Pedro', 'last_name': 'Antunes',
                'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test1email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_invalid_gender_person():
        """
        Person request with a invalid gender
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'nif': '111222333', 'first_name': 'Pedro', 'last_name': 'Antunes',
                'birth_date': '2000-03-21', 'telephone_number': '961234567',
                'email': 'test1@email.com', 'gender': 'z',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}

    @staticmethod
    def get_invalid_birth_date_person():
        """
        Person request with a birth date after current date
        """

        return {'address': {'street': 'Rua Gaio Pauletti', 'city': 'Valongo', 'zip_code': '4405-123'},
                'nif': '111222333', 'first_name': 'Pedro', 'last_name': 'Antunes',
                'birth_date': '2999-03-21', 'telephone_number': '961234567',
                'email': 'test1@email.com', 'gender': 'm',
                'state': 'ff286781-dd58-4b90-9582-95f62d06451c'}


class StateDataRepository:
    """
    Repository of state requests examples
    """

    @staticmethod
    def get_valid_state():
        """
        Valid state request
        """

        return {'name': 'Active',
                'description': 'For people'}


class PaginationDataRepository:
    """
    Repository of pagination requests examples
    """

    @staticmethod
    def get_valid_pagination():
        """
        Valid pagination request
        """

        factory = APIRequestFactory()

        return factory.get('/', {'page_num': 2, 'page_size': 15})

    @staticmethod
    def get_missing_page_num_pagination():
        """
        Pagination request with a missing page number field
        """

        factory = APIRequestFactory()

        return factory.get('/', {'page_size': 15})

    @staticmethod
    def get_missing_page_size_pagination():
        """
        Pagination request with a missing page size field
        """

        factory = APIRequestFactory()

        return factory.get('/', {'page_num': 2})

    @staticmethod
    def get_invalid_page_num_pagination():
        """
        Pagination request with an invalid page number field
        """

        factory = APIRequestFactory()

        return factory.get('/', {'page_num': -1, 'page_size': 15})

    @staticmethod
    def get_non_numeric_page_num_pagination():
        """
        Pagination request with a non numeric page number field
        """

        factory = APIRequestFactory()

        return factory.get('/', {'page_num': 'a', 'page_size': 15})

    @staticmethod
    def get_invalid_page_size_pagination():
        """
        Pagination request with an invalid page size field
        """

        factory = APIRequestFactory()

        return factory.get('/', {'page_num': 2, 'page_size': -1})

    @staticmethod
    def get_non_numeric_page_size_pagination():
        """
        Pagination request with a non numeric page size field
        """

        factory = APIRequestFactory()

        return factory.get('/', {'page_num': 2, 'page_size': 'a'})


class PaginationLinksDataRepository:
    """
    Repository of pagination links examples
    """

    @staticmethod
    def get_all_pagination_links(page_num, page_size, paginator, host):
        """
        Valid pagination request
        """

        return {'first': host+'?page_num=1&page_size='+str(page_size),
                'previous': host+'?page_num='+str(page_num-1)+'&page_size='+str(page_size),
                'next': host + '?page_num=' + str(page_num+1) + '&page_size='+str(page_size),
                'last': host+'?page_num=' + str(paginator.num_pages) + '&page_size='+str(page_size)}

    @staticmethod
    def get_last_pagination_links(page_num, page_size, paginator, host):
        """
        Valid pagination request
        """

        return {'first': host+'?page_num=1&page_size='+str(page_size),
                'previous': host+'?page_num='+str(page_num-1)+'&page_size='+str(page_size),
                'last': host+'?page_num=' + str(paginator.num_pages) + '&page_size='+str(page_size)}

    @staticmethod
    def get_first_pagination_links(page_num, page_size, paginator, host):
        """
        Valid pagination request
        """

        return {'first': host + '?page_num=1&page_size=' + str(page_size),
                'next': host + '?page_num=' + str(page_num+1) + '&page_size='+str(page_size),
                'last': host + '?page_num=' + str(paginator.num_pages) + '&page_size=' + str(page_size)}

class UtilsDataRepository:
    """
    Repository of pagination links examples
    """
    @staticmethod
    def get_valid_uuid():
        """
        Valid uuid

        :return: returns a valid uuid as a string
        """

        return 'd16698de-7efe-11ea-bc55-0242ac130003'

    @staticmethod
    def get_invalid_uuid():
        """
        Valid uuid

        :return: returns an invalid uuid as a string
        """

        return 'd16698de7efe1eabc550242ac130003'

class SearchStructureDataRepository:
    """
    Repository of search structure examples
    """

    @staticmethod
    def get_valid_search_structure():
        """
        Valid search structure
        """

        return {'firstColumn': 'A',
                'secondColumn': 'B',
                'thirdColumn': 'C',
                'fourthColumn': 'D'}
