"""
Tests related to Doctor view class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.doctor_view import DoctorView
from unit_tests.data_repository import DoctorDataRepository


class DoctorViewTestCase(TestCase):
    """
    Test case related to Doctor View class
    """

    @staticmethod
    def test_true_validate_new_doctor_request():
        """
        Tests if the method validates a valid new doctor request
        """

        DoctorView.validate_new_doctor_request(DoctorDataRepository.get_valid_doctor_request())

    def test_missing_name_validate_new_doctor_request(self):
        """
        Tests if the method detects a new doctor request with a missing name field
        """

        self.assertRaises(ValidationError,
                          DoctorView.validate_new_doctor_request,
                          DoctorDataRepository.get_missing_name_doctor_request())

    def test_missing_professional_certificate_validate_new_doctor_request(self):
        """
        Tests if the method detects a new doctor request with a missing professional certificate field
        """

        self.assertRaises(ValidationError,
                          DoctorView.validate_new_doctor_request,
                          DoctorDataRepository.get_missing_professional_certificate_doctor_request())

    def test_too_long_professional_certificate_validate_new_doctor_request(self):
        """
        Tests if the method detects a new doctor request with a professional certificate field too long
        """

        self.assertRaises(ValidationError,
                          DoctorView.validate_new_doctor_request,
                          DoctorDataRepository.get_too_long_professional_certificate_doctor_request())

    def test_missing_email_validate_new_doctor_request(self):
        """
        Tests if the method detects a new doctor request with a missing email field
        """

        self.assertRaises(ValidationError,
                          DoctorView.validate_new_doctor_request,
                          DoctorDataRepository.get_invalid_email_doctor_request())

    def test_invalid_email_validate_new_doctor_request(self):
        """
        Tests if the method detects a new doctor request with an invalid email field
        """

        self.assertRaises(ValidationError,
                          DoctorView.validate_new_doctor_request,
                          DoctorDataRepository.get_invalid_email_doctor_request())

    def test_missing_state_validate_new_doctor_request(self):
        """
        Tests if the method detects a new doctor request with a missing state field
        """

        self.assertRaises(ValidationError,
                          DoctorView.validate_new_doctor_request,
                          DoctorDataRepository.get_missing_state_doctor_request())
