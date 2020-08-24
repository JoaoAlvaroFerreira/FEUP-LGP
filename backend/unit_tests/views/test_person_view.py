"""
Tests related to Person view class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.person_view import PersonView
from unit_tests.data_repository import PersonDataRepository


class PersonViewTestCase(TestCase):
    """
    Test case related to Person View class
    """

    @staticmethod
    def test_true_validate_person_request():
        """
        Tests if the method validates a valid person request
        """

        PersonView.validate_person_request(PersonDataRepository.get_valid_person())

    def test_missing_nif_validate_person_request(self):
        """
        Tests if the method detects a person request with a missing nif field
        """

        self.assertRaises(ValidationError,
                          PersonView.validate_person_request,
                          PersonDataRepository.get_missing_nif_person())

    def test_missing_first_name_validate_person_request(self):
        """
        Tests if the method detects a person request with a missing first name field
        """

        self.assertRaises(ValidationError,
                          PersonView.validate_person_request,
                          PersonDataRepository.get_missing_first_name_person())

    def test_missing_last_name_validate_person_request(self):
        """
        Tests if the method detects a person request with a missing last name field
        """

        self.assertRaises(ValidationError,
                          PersonView.validate_person_request,
                          PersonDataRepository.get_missing_last_name_person())

    def test_missing_birth_date_validate_person_request(self):
        """
        Tests if the method detects a person request with a missing birth date field
        """

        self.assertRaises(ValidationError,
                          PersonView.validate_person_request,
                          PersonDataRepository.get_missing_birth_date_person())

    def test_missing_telephone_number_validate_person_request(self):
        """
        Tests if the method detects a person request with a missing telephone number field
        """

        self.assertRaises(ValidationError,
                          PersonView.validate_person_request,
                          PersonDataRepository.get_missing_telephone_number_person())

    def test_missing_email_validate_person_request(self):
        """
        Tests if the method detects a person request with a missing email field
        """

        self.assertRaises(ValidationError,
                          PersonView.validate_person_request,
                          PersonDataRepository.get_missing_email_person())

    def test_missing_gender_validate_person_request(self):
        """
        Tests if the method detects a person request with a missing gender field
        """

        self.assertRaises(ValidationError,
                          PersonView.validate_person_request,
                          PersonDataRepository.get_missing_gender_person())

    def test_invalid_email_validate_person_request(self):
        """
        Tests if the method detects a person request with a invalid email
        """

        self.assertRaises(ValidationError,
                          PersonView.validate_person_request,
                          PersonDataRepository.get_invalid_email_person())

    def test_invalid_gender_validate_person_request(self):
        """
        Tests if the method detects a person request with a gender type different from "m" or "f"
        """

        self.assertRaises(ValidationError,
                          PersonView.validate_person_request,
                          PersonDataRepository.get_invalid_gender_person())

    def test_invalid_birth_date_validate_person_request(self):
        """
        Tests if the method detects a person request with a birth date after current date
        """

        self.assertRaises(ValidationError,
                          PersonView.validate_person_request,
                          PersonDataRepository.get_invalid_birth_date_person())
