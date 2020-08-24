"""
Tests related to Treatment view class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.treatment_view import TreatmentView
from unit_tests.data_repository import TreatmentDataRepository


class TreatmentViewTestCase(TestCase):
    """
    Test case related to Treatment View class
    """

    @staticmethod
    def test_true_validate_treatment_request():
        """
        Tests if the method validates a valid treatment request
        """

        TreatmentView.validate_treatment_request(TreatmentDataRepository.get_valid_treatment())

    def test_missing_start_date_validate_perimetry_request(self):
        """
        Tests if the method detects a treatment request with a missing start date field
        """

        self.assertRaises(ValidationError,
                          TreatmentView.validate_treatment_request,
                          TreatmentDataRepository.get_missing_start_date_treatment())

    def test_invalid_end_date_validate_treatment_request(self):
        """
        Tests if the method detects a treatment request with an end date before the start date
        """

        self.assertRaises(ValidationError,
                          TreatmentView.validate_treatment_request,
                          TreatmentDataRepository.get_invalid_end_date_treatment())

    def test_invalid_pain_level_validate_treatment_request(self):
        """
        Tests if the method detects a treatment request with a pain level value outside the allowed range
        """

        self.assertRaises(ValidationError,
                          TreatmentView.validate_treatment_request,
                          TreatmentDataRepository.get_invalid_pain_level_treatment())
