"""
Tests related to Goniometry view class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.goniometry_view import GoniometryView
from unit_tests.data_repository import GoniometryDataRepository


class GoniometryViewTestCase(TestCase):
    """
    Test case related to Goniometry View class
    """

    @staticmethod
    def test_true_validate_goniometry_request():
        """
        Tests if the method validates a valid goniometry request
        """

        GoniometryView.validate_goniometry_request(GoniometryDataRepository.get_valid_goniometry())

    def test_missing_body_zone_validate_goniometry_request(self):
        """
        Tests if the method detects a goniometry request with a missing body zone field
        """

        self.assertRaises(ValidationError,
                          GoniometryView.validate_goniometry_request,
                          GoniometryDataRepository.get_missing_body_zone_goniometry())

    def test_invalid_values_validate_goniometry_request(self):
        """
        Tests if the method detects a goniometry request with a value outside the allowed value range
        """

        self.assertRaises(ValidationError,
                          GoniometryView.validate_goniometry_request,
                          GoniometryDataRepository.get_invalid_values_goniometry())

    def test_invalid_minmax_validate_goniometry_request(self):
        """
        Tests if the method detects a goniometry request with a minimum value greater than the maximum
        """

        self.assertRaises(ValidationError,
                          GoniometryView.validate_goniometry_request,
                          GoniometryDataRepository.get_invalid_minmax_goniometry())
