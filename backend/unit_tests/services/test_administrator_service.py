"""
Tests related to Administrator Service class
"""
import uuid
from unittest.mock import patch, Mock
from django.test import TestCase
from rest_framework.exceptions import ValidationError
from martin_helder.models import Administrator
from martin_helder.services.administrator_service import AdministratorService
from martin_helder.services.state_service import StateService
from martin_helder.services.person_service import PersonService
from martin_helder.services.credential_service import CredentialService
from unit_tests.data_repository import AdministratorDataRepository

class AdministratorServiceTestCase(TestCase):
    """
    Administrator service test cases
    """

    def setUp(self):
        self.administrator = AdministratorDataRepository.get_valid_administrator()
        self.id_administrator = str(uuid.uuid4())
        self.id_state = str(uuid.uuid4())
        self.id_person = str(uuid.uuid4())
        self.id_credential = str(uuid.uuid4())

    @patch('martin_helder.models.Administrator.objects')
    def test_valid_is_valid_administrator(self, mock_administrator_objects):
        """
        Tests if the method is successful when the administrator from the database is valid

        :param mock_administrator_objects: Mock of the administrator model
        """

        mock_administrator_objects.filter.return_value.exists.return_value = True

        AdministratorService.is_valid_administrator(self.id_administrator)
        mock_administrator_objects.filter.assert_called_once_with(id=self.id_administrator)
        mock_administrator_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.Administrator.objects')
    def test_invalid_is_valid_administrator(self, mock_administrator_objects):
        """
        Tests if the method raises a validation error when the administrator doesn't exist

        :param mock_administrator_objects: Mock of the administrator model
        """

        mock_administrator_objects.filter.return_value.exists.return_value = False

        self.assertRaises(ValidationError,
                          AdministratorService.is_valid_administrator, self.id_administrator)
        mock_administrator_objects.filter.assert_called_once_with(id=self.id_administrator)
        mock_administrator_objects.filter.return_value.exists.assert_called_once()

    @patch.object(StateService, 'is_valid_state')
    @patch.object(PersonService, 'add_person', return_value=Mock(id=str(uuid.uuid4())))
    @patch.object(CredentialService, 'add_credential', return_value=Mock(id=str(uuid.uuid4())))
    @patch.object(Administrator.objects, 'create', return_value=Mock(id=str(uuid.uuid4())))
    def test_add_administrator(self, mock_administrator, mock_credential_service,
                               mock_person_service, mock_state_service):
        """
        Tests if the method saves the administrator successfully

        :param mock_administrator: Mock of the administrator service
        :param mock_credential_service: Mock of the credential service
        :param mock_person_service: Mock of the person service
        :param mock_state_service: Mock of the state service
        """

        mock_new_model = mock_administrator.return_value

        return_value = AdministratorService.add_administrator(self.administrator)
        mock_state_service.assert_called_once_with(self.administrator['state'])
        mock_person_service.assert_called_once_with({
            "street": self.administrator['address']['street'],
            "zip_code": self.administrator['address']['zip_code'],
            "city": self.administrator['address']['city']
        }, {
            "nif": self.administrator['nif'],
            "first_name": self.administrator['first_name'],
            "last_name": self.administrator['last_name'],
            "birth_date": self.administrator['birth_date'],
            "telephone_number": self.administrator['telephone_number'],
            "email": self.administrator['email'],
            "gender": self.administrator['gender']
        })

        mock_credential_service.assert_called_once_with(self.administrator['email'])

        mock_administrator.assert_called_once_with(person_id=mock_person_service.return_value,
                                                   credential_id=mock_credential_service.return_value,
                                                   state_id=self.administrator['state'])

        mock_new_model.save.assert_called_once_with()

        self.assertIn(mock_new_model.id, str(return_value))
