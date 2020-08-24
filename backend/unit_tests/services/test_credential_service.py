"""
Tests related to Credential Service class
"""
import uuid
from unittest import mock
from unittest.mock import patch, Mock
from django.test import TestCase
from rest_framework.exceptions import ValidationError
from martin_helder.models import Credential
from martin_helder.services.credential_service import CredentialService
from unit_tests.data_repository import CredentialDataRepository


class CredentialServiceTestCase(TestCase):
    """
    Credential service test cases
    """

    def setUp(self):
        self.credential = CredentialDataRepository.get_valid_credential()
        self.id_credential = str(uuid.uuid4())

    @patch('martin_helder.models.Credential.objects')
    def test_valid_is_valid_credential(self, mock_credential_objects):
        """
        Tests if the method is successful when the credential from the database is valid

        :param mock_credential_objects: Mock of the credential model
        """

        mock_credential_objects.filter.return_value.exists.return_value = True

        CredentialService.is_valid_credential(self.id_credential)
        mock_credential_objects.filter.assert_called_once_with(id=self.id_credential)
        mock_credential_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.Credential.objects')
    def test_invalid_is_valid_credential(self, mock_credential_objects):
        """
        Tests if the method raises a validation error when the credential doesn't exist

        :param mock_credential_objects: Mock of the credential model
        """

        mock_credential_objects.filter.return_value.exists.return_value = False

        self.assertRaises(ValidationError,
                          CredentialService.is_valid_credential, self.id_credential)
        mock_credential_objects.filter.assert_called_once_with(id=self.id_credential)
        mock_credential_objects.filter.return_value.exists.assert_called_once()

    @patch.object(Credential.objects, 'create', return_value=Mock(id=str(uuid.uuid4())))
    def test_add_credential(self, mock_credential):
        """
        Tests if the method saves the credential successfully

        :param mock_credential: Mock of the credential service
        """

        mock_new_model = mock_credential.return_value

        return_value = CredentialService.add_credential(self.credential['email'])
        mock_credential.assert_called_once_with(password=mock.ANY, email=self.credential['email'])

        mock_new_model.save.assert_called_once_with()

        self.assertEqual(return_value, mock_new_model.id)
