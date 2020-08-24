"""
Tests related to State Service class
"""
import uuid
from unittest.mock import patch, Mock
from django.test import TestCase
from rest_framework.exceptions import ValidationError
from martin_helder.models import State
from martin_helder.services.state_service import StateService
from unit_tests.data_repository import StateDataRepository


class StateServiceTestCase(TestCase):
    """
    State service test cases
    """

    def setUp(self):
        self.state = StateDataRepository.get_valid_state()
        self.id_state = str(uuid.uuid4())

    @patch('martin_helder.models.State.objects')
    def test_valid_is_valid_state(self, mock_state_objects):
        """
        Tests if the method is successful when the state from the database is valid

        :param mock_state_objects: Mock of the state model
        """

        mock_state_objects.filter.return_value.exists.return_value = True

        StateService.is_valid_state(self.id_state)
        mock_state_objects.filter.assert_called_once_with(id=self.id_state)
        mock_state_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.State.objects')
    def test_invalid_is_valid_state(self, mock_state_objects):
        """
        Tests if the method raises a validation error when the state doesn't exist

        :param mock_state_objects: Mock of the state model
        """

        mock_state_objects.filter.return_value.exists.return_value = False

        self.assertRaises(ValidationError,
                          StateService.is_valid_state, self.id_state)
        mock_state_objects.filter.assert_called_once_with(id=self.id_state)
        mock_state_objects.filter.return_value.exists.assert_called_once()

    @patch.object(State.objects, 'create', return_value=Mock(id=str(uuid.uuid4())))
    def test_add_state(self, mock_state):
        """
        Tests if the method saves the state successfully

        :param mock_state: Mock of the state service
        """

        mock_new_model = mock_state.return_value

        return_value = StateService.add_state(self.state['name'],
                                              self.state['description'])

        mock_state.assert_called_once_with(name=self.state['name'],
                                           description=self.state['description'])

        mock_new_model.save.assert_called_once_with()

        self.assertEqual(return_value, mock_new_model.id)
