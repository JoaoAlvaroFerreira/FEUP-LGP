"""
Tests related to Address view class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.address_view import AddressView
from unit_tests.data_repository import AddressDataRepository


class AddressViewTestCase(TestCase):
    """
    Test case related to Address View class
    """

    @staticmethod
    def test_true_validate_address_request():
        """
        Tests if the method validates a valid address request
        """

        AddressView.validate_address_request(AddressDataRepository.get_valid_address())

    def test_missing_street_validate_address_request(self):
        """
        Tests if the method detects a address request with a missing street field
        """

        self.assertRaises(ValidationError,
                          AddressView.validate_address_request,
                          AddressDataRepository.get_missing_street_address())

    def test_missing_zip_code_validate_address_request(self):
        """
        Tests if the method detects a address request with a missing zip code field
        """

        self.assertRaises(ValidationError,
                          AddressView.validate_address_request,
                          AddressDataRepository.get_missing_zip_code_address())

    def test_missing_city_validate_address_request(self):
        """
        Tests if the method detects a address request with a missing city field
        """

        self.assertRaises(ValidationError,
                          AddressView.validate_address_request,
                          AddressDataRepository.get_missing_city_address())
