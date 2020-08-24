"""
Tests related to Patient Service class
"""

import uuid
from unittest.mock import patch, Mock
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.models import Person
from martin_helder.services.person_service import PersonService
from martin_helder.services.address_service import AddressService
from unit_tests.data_repository import PersonDataRepository


class PersonServiceTestCase(TestCase):
    """
    Person service test cases
    """

    def setUp(self):
        self.id_person = str(uuid.uuid4())
        self.person_request = PersonDataRepository.get_valid_person()

    @patch('martin_helder.models.Person.objects')
    def test_valid_is_valid_person(self, mock_person):
        """
        Tests if the method is successful when the person from the database is valid

        :param mock_person: Mock of the person model
        """

        mock_person.filter.return_value.exists.return_value = True

        PersonService.is_valid_person(self.id_person)
        mock_person.filter.assert_called_once_with(id=self.id_person)
        mock_person.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.Person.objects')
    def test_invalid_is_valid_person(self, mock_person):
        """
        Tests if the method raises a validation error when the person doesn't exist

        :param mock_person: Mock of the person model
        """

        mock_person.filter.return_value.exists.return_value = False

        self.assertRaises(ValidationError,
                          PersonService.is_valid_person, self.id_person)
        mock_person.filter.assert_called_once_with(id=self.id_person)
        mock_person.filter.return_value.exists.assert_called_once()

    @patch.object(AddressService, 'check_address', return_value=Mock(id=str(uuid.uuid4())))
    @patch.object(Person.objects, 'create', return_value=Mock(id=str(uuid.uuid4())))
    def test_valid_add_person_address_exists(self, mock_person, mock_address_service_check):
        """
        Tests if the method saves the person successfully when the address exists

        :param mock_person: Mock of the person model
        :param mock_address_service_check: Mock of check_address from address service
        """

        mock_new_model = mock_person.return_value

        return_value = PersonService.add_person({'street': self.person_request['address']['street'],
                                                 'zip_code': self.person_request['address']['zip_code'],
                                                 'city': self.person_request['address']['city']},
                                                {'nif': self.person_request['nif'],
                                                 'first_name': self.person_request['first_name'],
                                                 'last_name': self.person_request['last_name'],
                                                 'birth_date': self.person_request['birth_date'],
                                                 'telephone_number': self.person_request['telephone_number'],
                                                 'email': self.person_request['email'],
                                                 'gender': self.person_request['gender']}
                                                )

        mock_address_service_check.assert_called_once_with(self.person_request['address']['street'],
                                                           self.person_request['address']['zip_code'],
                                                           self.person_request['address']['city']
                                                           )

        mock_person.assert_called_once_with(address_id=mock_address_service_check.return_value,
                                            nif=self.person_request['nif'],
                                            first_name=self.person_request['first_name'],
                                            last_name=self.person_request['last_name'],
                                            birth_date=self.person_request['birth_date'],
                                            telephone_number=self.person_request['telephone_number'],
                                            email=self.person_request['email'],
                                            gender=self.person_request['gender'])


        mock_new_model.save.assert_called_once_with()

        self.assertIn(mock_new_model.id, str(return_value))

    @patch.object(AddressService, 'check_address', return_value=None)
    @patch.object(AddressService, 'add_address', return_value=Mock(id=str(uuid.uuid4())))
    @patch.object(Person.objects, 'create', return_value=Mock(id=str(uuid.uuid4())))
    def test_valid_add_person_address_doesnt_exist(self,
                                                   mock_person,
                                                   mock_address_service_add,
                                                   mock_address_service_check):
        """
        Tests if the method saves the person successfully when the address doesn't exist

        :param mock_person: Mock of the person model
        :param mock_address_service_check: Mock of check_address from address service
        :param mock_address_service_add: Mock of add_address from address service
        """

        mock_new_model = mock_person.return_value

        return_value = PersonService.add_person({'street': self.person_request['address']['street'],
                                                 'zip_code': self.person_request['address']['zip_code'],
                                                 'city': self.person_request['address']['city']},
                                                {'nif': self.person_request['nif'],
                                                 'first_name': self.person_request['first_name'],
                                                 'last_name': self.person_request['last_name'],
                                                 'birth_date': self.person_request['birth_date'],
                                                 'telephone_number': self.person_request['telephone_number'],
                                                 'email': self.person_request['email'],
                                                 'gender': self.person_request['gender']}
                                                )

        mock_address_service_check.assert_called_once_with(self.person_request['address']['street'],
                                                           self.person_request['address']['zip_code'],
                                                           self.person_request['address']['city']
                                                           )

        mock_address_service_add.assert_called_once_with(self.person_request['address']['street'],
                                                         self.person_request['address']['zip_code'],
                                                         self.person_request['address']['city']
                                                         )

        mock_person.assert_called_once_with(address_id=mock_address_service_add.return_value,
                                            nif=self.person_request['nif'],
                                            first_name=self.person_request['first_name'],
                                            last_name=self.person_request['last_name'],
                                            birth_date=self.person_request['birth_date'],
                                            telephone_number=self.person_request['telephone_number'],
                                            email=self.person_request['email'],
                                            gender=self.person_request['gender'])


        mock_new_model.save.assert_called_once_with()

        self.assertIn(mock_new_model.id, str(return_value))
