"""
Service layer for state related operations
"""

from rest_framework.exceptions import ValidationError
from martin_helder.models import State

from martin_helder.views.view_utils import Utils

class StateService:
    """
    Service class for state related operations
    """

    @staticmethod
    def add_state(name, description):
        """
        Method create a new state

        :param name: State name
        :param description: State description
        :return: State created id
        """

        new_state = State.objects.create(name=name, description=description)

        new_state.save()

        return new_state.id

    @staticmethod
    def check_state(name, description):
        """
        Returns the state if it exists or none

        :param name: State name
        :param description: State description
        :return: State found or none
        """

        state = State.objects.filter(name=name, description=description)

        if state.exists():
            return state

        return None

    @staticmethod
    def is_valid_state(id_state):
        """
        Checks if the specified state exists

        :param id_state: ID of state to be checked
        """

        Utils.validate_uuid(id_state)

        if not State.objects.filter(id=id_state).exists():
            raise ValidationError("The state is not valid!")
