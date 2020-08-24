"""
Tests related to Muscle Test view class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.muscle_test_view import MuscleTestView
from unit_tests.data_repository import MuscleTestDataRepository


class GoniometryViewTestCase(TestCase):
    """
    Test case related to Muscle Test View class
    """

    @staticmethod
    def test_true_validate_muscle_test_request():
        """
        Tests if the method validates a valid muscle test request
        """

        MuscleTestView.validate_muscle_test_request(MuscleTestDataRepository.get_valid_muscle_test())

    def test_missing_body_zone_validate_muscle_test_request(self):
        """
        Tests if the method detects a muscle test request with a missing body zone field
        """

        self.assertRaises(ValidationError,
                          MuscleTestView.validate_muscle_test_request,
                          MuscleTestDataRepository.get_missing_body_zone_muscle_test())

    def test_missing_strength_validate_muscle_test_request(self):
        """
        Tests if the method detects a muscle test request with a missing strength field
        """

        self.assertRaises(ValidationError,
                          MuscleTestView.validate_muscle_test_request,
                          MuscleTestDataRepository.get_missing_strength_muscle_test())

    def test_invalid_strength_validate_muscle_test_request(self):
        """
        Tests if the method detects a muscle test request with a strength value outside the allowed range
        """

        self.assertRaises(ValidationError,
                          MuscleTestView.validate_muscle_test_request,
                          MuscleTestDataRepository.get_invalid_strength_muscle_test())
