"""
Tests related to Treatment Service class
"""
import uuid
from unittest import mock
from unittest.mock import patch, Mock

from django.core.paginator import Paginator
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.models import Treatment
from martin_helder.services.patient_service import PatientService
from martin_helder.services.physiotherapist_service import PhysiotherapistService
from martin_helder.services.treatment_service import TreatmentService
from martin_helder.models.serializers.treatment import TreatmentListSerializer
from martin_helder.services.pagination_service import PaginationService

from unit_tests.data_repository import TreatmentDataRepository

from unit_tests.data_repository import PaginationDataRepository


class TreatmentServiceTestCase(TestCase):
    """
    Treatment service test cases
    """

    def setUp(self):
        self.treatment_request = TreatmentDataRepository.get_valid_treatment()
        self.id_patient = str(uuid.uuid4())
        self.id_treatment_cycle = str(uuid.uuid4())
        self.new_treatment = str(uuid.uuid4())
        self.id_physiotherapist = str(uuid.uuid4())

    @patch.object(PatientService, 'is_valid_patient')
    @patch.object(PhysiotherapistService, 'is_physiotherapist_attributed_patient')
    @patch.object(TreatmentService, 'is_valid_treatment_cycle')
    @patch.object(TreatmentService, 'has_treatment_cycle_remaining_sessions')
    def test_treat_patient(self, mock_treatment_service_2, mock_treatment_service_1,
                           mock_physiotherapist_service, mock_patient_service):
        """
        Tests if method saves treatment successfully

        :param mock_patient_service: Mock of the patient service
        :param mock_physiotherapist_service: Mock of the physiotherapist service
        :param mock_treatment_service: Mock of the treatment service
        :param mock_treatment: Mock of the treatment model
        """

        with patch.object(Treatment.objects, 'create', return_value=Mock(id=str(uuid.uuid4()))) as mock_treatment:
            mock_new_model = mock_treatment.return_value

            return_value = TreatmentService.treat_patient(self.treatment_request, self.id_patient,
                                                          self.id_treatment_cycle, self.id_physiotherapist)
            mock_patient_service.assert_called_once_with(self.id_patient)
            mock_physiotherapist_service.assert_called_once_with(self.id_patient, self.id_physiotherapist)
            mock_treatment_service_1.assert_called_once_with(self.id_treatment_cycle, self.id_patient)
            mock_treatment_service_2.assert_called_once_with(self.id_treatment_cycle)

            mock_treatment.assert_called_once_with(start_date=self.treatment_request['start_date'],
                                                   end_date=self.treatment_request['end_date'],
                                                   summary=self.treatment_request['summary'],
                                                   pain_level=self.treatment_request['pain_level'],
                                                   medication=self.treatment_request['medication'],
                                                   treatment=self.treatment_request['treatment'],
                                                   periodic_evaluation=self.treatment_request['periodic_evaluation'],
                                                   treatment_cycle_id=self.id_treatment_cycle)

            mock_new_model.save.assert_called_once_with()

            self.assertIn(mock_new_model.id, str(return_value))

    @patch.object(Treatment.objects, 'filter', return_value=Mock())
    @patch.object(TreatmentListSerializer, 'many_init', return_value=Mock())
    @patch.object(PaginationService, 'get_paginated_results', return_value=Mock())
    @patch.object(PaginationService, 'is_valid_page_number')
    def test_list_all_treatments(self, mock_pag_service_valid_page, mock_pag_service_get_results,
                                 mock_treatment_list_serializer, mock_filter_treatments):
        """
        Tests if method returns all treatments successfully

        :param mock_pag_service_valid_page: Mock of page number validation method
        :param mock_pag_service_get_results: Mock of paginated results method
        :param mock_treatment_list_serializer: Mock of treatment list serializer
        :param mock_filter_treatments: Mock of list of filtered treatments
        """

        with patch.object(Paginator, '__init__', return_value=None) as mock_paginator:
            with patch.object(Paginator, 'page', return_value=Mock()) as mock_paginator_page:
                with patch.object(PatientService, 'is_valid_patient', return_value=Mock()) as mock_patient_service:
                    with patch.object(TreatmentService, 'is_valid_treatment_cycle') as mock_treatment_service:
                        pagination_args = PaginationDataRepository.get_valid_pagination()

                        mock_results = mock_pag_service_get_results.return_value
                        mock_all_treatment_list = mock_filter_treatments.return_value

                        return_value = TreatmentService.list_all_treatments(self.id_patient, self.id_treatment_cycle,
                                                                            pagination_args.GET['page_num'],
                                                                            pagination_args.GET['page_size'],
                                                                            pagination_args.build_absolute_uri())

                        mock_patient_service.assert_called_once_with(self.id_patient)
                        mock_treatment_service.assert_called_once_with(self.id_treatment_cycle, self.id_patient)

                        mock_filter_treatments.assert_called_once_with(treatment_cycle_id=self.id_treatment_cycle)
                        mock_paginator.assert_called_once_with(mock_all_treatment_list,
                                                               pagination_args.GET['page_size'])
                        mock_pag_service_valid_page.assert_called_once_with(mock.ANY,
                                                                            int(pagination_args.GET['page_num']))
                        mock_treatment_list_serializer.assert_called_once_with(mock_paginator_page(
                            pagination_args.GET['page_num']))

                        self.assertEqual(return_value, mock_results)

    @patch('martin_helder.models.TreatmentCycle.objects')
    def test_true_is_valid_treatment_cycle(self, mock_treatment_cycle_objects):
        """
        Tests if the method is successful when the treatment cycle from the database is valid

        :param mock_treatment_cycle_objects: Mock of the treatment cycle model
        """

        mock_treatment_cycle_objects.filter.return_value.exists.return_value = True

        TreatmentService.is_valid_treatment_cycle(self.id_treatment_cycle, self.id_patient)
        mock_treatment_cycle_objects.filter.assert_called_once_with(id=self.id_treatment_cycle,
                                                                    patient_id=self.id_patient)
        mock_treatment_cycle_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.TreatmentCycle.objects')
    def test_false_is_valid_treatment_cycle(self, mock_treatment_cycle_objects):
        """
        Tests if the method raises a validation error when the treatment cycle doesn't exist

        :param mock_treatment_cycle_objects: Mock of the treatment cycle model
        """

        mock_treatment_cycle_objects.filter.return_value.exists.return_value = False

        self.assertRaises(ValidationError,
                          TreatmentService.is_valid_treatment_cycle, self.id_treatment_cycle, self.id_patient)
        mock_treatment_cycle_objects.filter.assert_called_once_with(id=self.id_treatment_cycle,
                                                                    patient_id=self.id_patient)
        mock_treatment_cycle_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.TreatmentCycle.objects')
    def test_true_has_treatment_cycle_remaining_sessions(self, mock_treatment_cycle_objects):
        """
        Tests if the method is successful when the patient hasn't still reached the session limit of the treatment cycle

        :param mock_treatment_cycle_objects: Mock of the treatment cycle model
        """

        mock_treatment_cycle = mock_treatment_cycle_objects.get.return_value
        mock_treatment_cycle.number_of_sessions = 2
        mock_treatment_cycle.completed_sessions = 1

        TreatmentService.has_treatment_cycle_remaining_sessions(self.id_treatment_cycle)
        mock_treatment_cycle_objects.get.assert_called_once_with(id=self.id_treatment_cycle)

    @patch('martin_helder.models.TreatmentCycle.objects')
    def test_false_has_treatment_cycle_remaining_sessions(self, mock_treatment_cycle_objects):
        """
        Tests if the method raises a validation error when the patient has already completed all treatment cycle
        sessions

        :param mock_treatment_cycle_objects: Mock of the treatment cycle model
        """

        mock_treatment_cycle = mock_treatment_cycle_objects.get.return_value
        mock_treatment_cycle.number_of_sessions = 2
        mock_treatment_cycle.completed_sessions = 2

        self.assertRaises(ValidationError,
                          TreatmentService.has_treatment_cycle_remaining_sessions, self.id_treatment_cycle)
        mock_treatment_cycle_objects.get.assert_called_once_with(id=self.id_treatment_cycle)
