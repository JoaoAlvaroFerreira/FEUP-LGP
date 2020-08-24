"""
Tests related to Administrator view class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.administrator_view import AdministratorView
from unit_tests.data_repository import AdministratorDataRepository


class AdministratorViewTestCase(TestCase):
    """
    Test case related to Administrator View class
    """

    @staticmethod
    def test_true_validate_add_administrator_request():
        """
        Tests if the method validates a valid administrator request
        """

        AdministratorView.validate_add_administrator_request(AdministratorDataRepository.get_valid_administrator())

    def test_missing_street_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a missing street field
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_missing_street_administrator())

    def test_missing_city_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a missing city field
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_missing_city_administrator())

    def test_missing_nif_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a missing nif field
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_missing_nif_administrator())

    def test_missing_first_name_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a missing first name field
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_missing_first_name_administrator())

    def test_missing_last_name_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a missing last name field
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_missing_last_name_administrator())

    def test_missing_birth_date_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a missing birth date field
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_missing_birth_date_administrator())

    def test_missing_telephone_number_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a missing telephone number field
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_missing_telephone_number_administrator())

    def test_missing_email_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a missing email field
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_missing_email_administrator())

    def test_missing_gender_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a missing gender field
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_missing_gender_administrator())

    def test_missing_zip_code_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a missing zip code field
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_missing_zip_code_administrator())

    def test_invalid_email_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a invalid email
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_invalid_email_administrator())

    def test_invalid_gender_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a gender type different from "m" or "f"
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_invalid_gender_administrator())

    def test_invalid_birth_date_validate_add_administrator_request(self):
        """
        Tests if the method detects a administrator request with a birth date after current date
        """

        self.assertRaises(ValidationError,
                          AdministratorView.validate_add_administrator_request,
                          AdministratorDataRepository.get_invalid_birth_date_administrator())
