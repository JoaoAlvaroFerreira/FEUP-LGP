"""
Tests related to Doctor Service class
"""
import uuid
from unittest.mock import patch, Mock
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.models import Doctor
from martin_helder.services.state_service import StateService
from martin_helder.services.doctor_service import DoctorService

from unit_tests.data_repository import DoctorDataRepository


class DoctorServiceTestCase(TestCase):
    """
    Doctor service test cases
    """

    def setUp(self):
        self.new_doctor_request = DoctorDataRepository.get_valid_doctor_request()
        self.new_doctor = str(uuid.uuid4())

    @patch.object(StateService, 'is_valid_state')
    @patch.object(DoctorService, 'is_unique_professional_certificate')
    @patch.object(DoctorService, 'is_unique_email')
    def test_add_doctor(self, mock_doctor_service_unq_email, mock_doctor_service_unq_prof_cert, mock_state_service):
        """
        Tests if method saves new doctor successfully

        :param mock_doctor_service_unq_email: Mock of the unique email check in doctor service
        :param mock_doctor_service_unq_prof_cert: Mock of the unique professional certificate check in doctor service
        :param mock_state_service: Mock of the state service
        """

        with patch.object(Doctor.objects, 'create', return_value=Mock(id=str(uuid.uuid4()))) as mock_new_doctor:
            mock_new_model = mock_new_doctor.return_value

            return_value = DoctorService.add_doctor(self.new_doctor_request)
            mock_state_service.assert_called_once_with(self.new_doctor_request['state_id'])
            mock_doctor_service_unq_prof_cert.assert_called_once_with(
                self.new_doctor_request['professional_certificate'])
            mock_doctor_service_unq_email.assert_called_once_with(
                self.new_doctor_request['email'])

            mock_new_doctor.assert_called_once_with(name=self.new_doctor_request['name'],
                                                    professional_certificate=self.new_doctor_request[
                                                        'professional_certificate'],
                                                    email=self.new_doctor_request['email'],
                                                    state_id=self.new_doctor_request['state_id'])

            mock_new_model.save.assert_called_once_with()

            self.assertIn(mock_new_model.id, str(return_value))

    @patch('martin_helder.models.Doctor.objects')
    def test_true_is_unique_professional_certificate(self, mock_doctor_objects):
        """
        Tests if the method is successful when the new doctor professional certificate is not yet registered

        :param mock_doctor_objects: Mock of the doctor model
        """

        mock_doctor_objects.filter.return_value.exists.return_value = False

        DoctorService.is_unique_professional_certificate(self.new_doctor_request['professional_certificate'])
        mock_doctor_objects.filter.assert_called_once_with(professional_certificate=self.new_doctor_request[
            'professional_certificate'])
        mock_doctor_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.Doctor.objects')
    def test_false_is_unique_professional_certificate(self, mock_doctor_objects):
        """
        Tests if the method raises a validation error when the new doctor professional certificate is already registered

        :param mock_doctor_objects: Mock of the doctor model
        """

        mock_doctor_objects.filter.return_value.exists.return_value = True

        self.assertRaises(ValidationError,
                          DoctorService.is_unique_professional_certificate, self.new_doctor_request[
                              'professional_certificate'])
        mock_doctor_objects.filter.assert_called_once_with(professional_certificate=self.new_doctor_request[
            'professional_certificate'])
        mock_doctor_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.Doctor.objects')
    def test_true_is_unique_email(self, mock_doctor_objects):
        """
        Tests if the method is successful when the new doctor email is not yet registered

        :param mock_doctor_objects: Mock of the doctor model
        """

        mock_doctor_objects.filter.return_value.exists.return_value = False

        DoctorService.is_unique_email(self.new_doctor_request['email'])
        mock_doctor_objects.filter.assert_called_once_with(email=self.new_doctor_request['email'])
        mock_doctor_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.Doctor.objects')
    def test_false_is_unique_email(self, mock_doctor_objects):
        """
        Tests if the method raises a validation error when the new doctor email is already registered

        :param mock_doctor_objects: Mock of the doctor model
        """

        mock_doctor_objects.filter.return_value.exists.return_value = True

        self.assertRaises(ValidationError,
                          DoctorService.is_unique_email, self.new_doctor_request['email'])
        mock_doctor_objects.filter.assert_called_once_with(email=self.new_doctor_request['email'])
        mock_doctor_objects.filter.return_value.exists.assert_called_once()
