"""
Tests related to Perimetry view class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.perimetry_view import PerimetryView
from unit_tests.data_repository import PerimetryDataRepository


class PerimetryViewTestCase(TestCase):
    """
    Test case related to Perimetry View class
    """

    @staticmethod
    def test_true_validate_perimetry_request():
        """
        Tests if the method validates a valid goniometry request
        """

        PerimetryView.validate_perimetry_request(PerimetryDataRepository.get_valid_perimetry())

    def test_missing_body_zone_validate_perimetry_request(self):
        """
        Tests if the method detects a perimetry request with a missing body zone field
        """

        self.assertRaises(ValidationError,
                          PerimetryView.validate_perimetry_request,
                          PerimetryDataRepository.get_missing_body_zone_perimetry())

    def test_missing_size_validate_perimetry_request(self):
        """
        Tests if the method detects a perimetry request with a missing size field
        """

        self.assertRaises(ValidationError,
                          PerimetryView.validate_perimetry_request,
                          PerimetryDataRepository.get_missing_size_perimetry())

    def test_invalid_size_validate_perimetry_request(self):
        """
        Tests if the method detects a perimetry request with a size value outside the allowed range
        """

        self.assertRaises(ValidationError,
                          PerimetryView.validate_perimetry_request,
                          PerimetryDataRepository.get_invalid_size_perimetry())
