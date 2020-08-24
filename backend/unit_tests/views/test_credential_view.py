"""
Tests related to Credential view class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.credential_view import CredentialView
from unit_tests.data_repository import CredentialDataRepository


class CredentialViewTestCase(TestCase):
    """
    Test case related to Credential View class
    """

    @staticmethod
    def test_true_validate_credential_request():
        """
        Tests if the method validates a valid credential request
        """

        CredentialView.validate_credential_request(CredentialDataRepository.get_valid_credential())

    def test_missing_email_validate_credential_request(self):
        """
        Tests if the method detects a credential request with a missing email field
        """

        self.assertRaises(ValidationError,
                          CredentialView.validate_credential_request,
                          CredentialDataRepository.get_missing_email_credential())
