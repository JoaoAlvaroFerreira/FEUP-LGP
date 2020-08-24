"""
Tests related to Patient Service class
"""

import uuid
from unittest import mock
from unittest.mock import patch, Mock

from django.core.paginator import Paginator
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.models import Patient
from martin_helder.services.patient_service import PatientService
from martin_helder.services.person_service import PersonService
from martin_helder.services.pagination_service import PaginationService
from martin_helder.models.serializers.patient import PatientListSerializer
from martin_helder.services.query_service import QueryService
from unit_tests.data_repository import PatientDataRepository, PaginationDataRepository


class PatientServiceTestCase(TestCase):
    """
    Patient service test cases
    """

    def setUp(self):
        self.patient_request = PatientDataRepository.get_valid_patient()
        self.id_patient = str(uuid.uuid4())
        self.id_person = str(uuid.uuid4())
        self.query = "test"

    @patch('martin_helder.models.Patient.objects')
    def test_true_is_valid_patient(self, mock_patient_objects):
        """
        Tests if the method is successful when the patient from the database is valid

        :param mock_patient_objects: Mock of the patient model
        """

        mock_patient_objects.filter.return_value.exists.return_value = True

        PatientService.is_valid_patient(self.id_patient)
        mock_patient_objects.filter.assert_called_once_with(id=self.id_patient)
        mock_patient_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.Patient.objects')
    def test_false_is_valid_patient(self, mock_patient_objects):
        """
        Tests if the method raises a validation error when the patient doesn't exist

        :param mock_patient_objects: Mock of the patient model
        """

        mock_patient_objects.filter.return_value.exists.return_value = False

        self.assertRaises(ValidationError,
                          PatientService.is_valid_patient, self.id_patient)
        mock_patient_objects.filter.assert_called_once_with(id=self.id_patient)
        mock_patient_objects.filter.return_value.exists.assert_called_once()


    @patch.object(Patient.objects, 'create', return_value=Mock(id=str(uuid.uuid4())))
    @patch.object(PersonService, 'add_person', return_value=Mock(id=str(uuid.uuid4())))
    def test_add_patient(self, mock_person_service, mock_patient):
        """
        Tests if the method saves the patient successfully

        :param mock_person_service: Mock of the person service
        :param mock_patient: Mock of the patient service
        """

        mock_new_model = mock_patient.return_value
        return_value = PatientService.add_patient(self.patient_request)

        mock_person_service.assert_called_once_with({'street': self.patient_request['address']['street'],
                                                     'zip_code': self.patient_request['address']['zip_code'],
                                                     'city': self.patient_request['address']['city']},
                                                    {'nif': self.patient_request['nif'],
                                                     'first_name': self.patient_request['first_name'],
                                                     'last_name': self.patient_request['last_name'],
                                                     'birth_date': self.patient_request['birth_date'],
                                                     'telephone_number': self.patient_request['telephone_number'],
                                                     'email': self.patient_request['email'],
                                                     'gender': self.patient_request['gender']}
                                                    )


        mock_patient.assert_called_once_with(profession=self.patient_request['profession'],
                                             diagnostic=self.patient_request['diagnostic'],
                                             clinical_history=self.patient_request['clinical_history'],
                                             person_id=mock_person_service.return_value
                                             )

        mock_new_model.save.assert_called_once_with()

        self.assertIn(mock_new_model.id, str(return_value))

    @patch.object(QueryService, 'get_query_results', return_value=Mock())
    @patch.object(PatientListSerializer, 'many_init', return_value=Mock())
    @patch.object(PaginationService, 'get_paginated_results', return_value=Mock())
    @patch.object(PaginationService, 'is_valid_page_number')
    def test_list_patients(self, mock_pag_service_valid_page, mock_pag_service_get_results,
                           mock_patient_list_serializer, mock_query_patients):
        """
        Tests if method returns all patients successfully

        :param mock_pag_service_valid_page: Mock of page number validation method
        :param mock_pag_service_get_results: Mock of paginated results method
        :param mock_patient_list_serializer: Mock of patient list serializer
        :param mock_query_patients: Mock of list of searched patients
        """

        with patch.object(Paginator, '__init__', return_value=None) as mock_paginator:
            with patch.object(Paginator, 'page', return_value=Mock()) as mock_paginator_page:

                pagination_args = PaginationDataRepository.get_valid_pagination()

                mock_results = mock_pag_service_get_results.return_value
                mock_patients_list = mock_query_patients.return_value

                return_value = PatientService.list_patients(pagination_args.GET['page_num'],
                                                            pagination_args.GET['page_size'],
                                                            pagination_args.build_absolute_uri(),
                                                            self.query)

                mock_query_patients.assert_called_once_with(Patient.objects, self.query, mock.ANY)
                mock_paginator.assert_called_once_with(mock_patients_list, pagination_args.GET['page_size'])
                mock_pag_service_valid_page.assert_called_once_with(mock.ANY, int(pagination_args.GET['page_num']))
                mock_patient_list_serializer.assert_called_once_with(mock_paginator_page(
                    pagination_args.GET['page_num']))

                self.assertEqual(return_value, mock_results)
