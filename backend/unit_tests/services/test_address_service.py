"""
Tests related to Address Service class
"""
import uuid
from unittest.mock import patch, Mock
from django.test import TestCase
from rest_framework.exceptions import ValidationError
from martin_helder.models import Address
from martin_helder.services.address_service import AddressService
from unit_tests.data_repository import AddressDataRepository


class AddressServiceTestCase(TestCase):
    """
    Address service test cases
    """

    def setUp(self):
        self.address = AddressDataRepository.get_valid_address()
        self.id_address = str(uuid.uuid4())

    @patch('martin_helder.models.Address.objects')
    def test_valid_is_valid_address(self, mock_address_objects):
        """
        Tests if the method is successful when the address from the database is valid

        :param mock_address_objects: Mock of the address model
        """

        mock_address_objects.filter.return_value.exists.return_value = True

        AddressService.is_valid_address(self.id_address)
        mock_address_objects.filter.assert_called_once_with(id=self.id_address)
        mock_address_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.Address.objects')
    def test_invalid_is_valid_address(self, mock_address_objects):
        """
        Tests if the method raises a validation error when the address doesn't exist

        :param mock_address_objects: Mock of the address model
        """

        mock_address_objects.filter.return_value.exists.return_value = False

        self.assertRaises(ValidationError,
                          AddressService.is_valid_address, self.id_address)
        mock_address_objects.filter.assert_called_once_with(id=self.id_address)
        mock_address_objects.filter.return_value.exists.assert_called_once()

    @patch.object(Address.objects, 'create', return_value=Mock(id=str(uuid.uuid4())))
    def test_add_address(self, mock_address):
        """
        Tests if the method saves the address successfully

        :param mock_address: Mock of the address service
        """

        mock_new_model = mock_address.return_value

        return_value = AddressService.add_address(self.address['street'],
                                                  self.address['zip_code'],
                                                  self.address['city'])
        mock_address.assert_called_once_with(street=self.address['street'],
                                             zip_code=self.address['zip_code'],
                                             city=self.address['city'])

        mock_new_model.save.assert_called_once_with()

        self.assertEqual(return_value, mock_new_model.id)
