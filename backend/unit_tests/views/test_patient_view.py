"""
Tests related to Patient view class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.patient_view import PatientView
from unit_tests.data_repository import PatientDataRepository


class PatientViewTestCase(TestCase):
    """
    Test case related to Patient View class
    """

    @staticmethod
    def test_true_validate_patient_request():
        """
        Tests if the method validates a valid patient request
        """

        PatientView.validate_patient_request(PatientDataRepository.get_valid_patient())

    def test_missing_profession_validate_patient_request(self):
        """
        Tests if the method detects a patient request with a missing profession field
        """

        self.assertRaises(ValidationError,
                          PatientView.validate_patient_request,
                          PatientDataRepository.get_missing_profession_person())

    def test_missing_diagnostic_validate_patient_request(self):
        """
        Tests if the method detects a patient request with a missing diagnostic field
        """

        self.assertRaises(ValidationError,
                          PatientView.validate_patient_request,
                          PatientDataRepository.get_missing_diagnostic_person())

    def test_missing_clinical_history_validate_patient_request(self):
        """
        Tests if the method detects a patient request with a missing clinical_history field
        """

        self.assertRaises(ValidationError,
                          PatientView.validate_patient_request,
                          PatientDataRepository.get_missing_clinical_history_person())
