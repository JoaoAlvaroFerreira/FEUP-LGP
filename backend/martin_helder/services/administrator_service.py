"""
Service layer for administrator related operations
"""

from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from martin_helder.models.administrator import Administrator, AdministratorSerializer
from martin_helder.services.credential_service import CredentialService
from martin_helder.services.state_service import StateService
from martin_helder.services.person_service import PersonService

from martin_helder.views.view_utils import Utils

class AdministratorService:
    """
    Service class for administrator related operations
    """

    @staticmethod
    def add_administrator(administrator_request):
        '''
        Method to add a new administrator

        :param administrator_request: Incoming request
        :return: administrator and person id from the new person
        '''
        return_value = {}

        StateService.is_valid_state(administrator_request['state'])

        return_value['person_id'] = PersonService.add_person({
            "street": administrator_request['address']['street'],
            "zip_code": administrator_request['address']['zip_code'],
            "city": administrator_request['address']['city']
        }, {
            "nif": administrator_request['nif'],
            "first_name": administrator_request['first_name'],
            "last_name": administrator_request['last_name'],
            "birth_date": administrator_request['birth_date'],
            "telephone_number": administrator_request['telephone_number'],
            "email": administrator_request['email'],
            "gender": administrator_request['gender']
        })

        credential_id = CredentialService.add_credential(administrator_request['email'])

        new_administrator = Administrator.objects.create(person_id=return_value['person_id'],
                                                         credential_id=credential_id,
                                                         state_id=administrator_request['state'])

        new_administrator.save()

        return_value['administrator_id'] = new_administrator.id

        return return_value

    @staticmethod
    def is_valid_administrator(id_administrator):
        """
        Checks if the specified administrator exists

        :param id_administrator: ID of administrator to be checked
        """

        Utils.validate_uuid(id_administrator)

        if not Administrator.objects.filter(id=id_administrator).exists():
            raise ValidationError("The administrator " + id_administrator + " is not valid!")

    @staticmethod
    def get_administrator(id_administrator):
        """
        Returns the administrator with a given id

        :param id_administrator: ID of administrator
        :return: Administrator found or none
        """

        Utils.validate_uuid(id_administrator)

        try:
            admin = Administrator.objects.get(id=id_administrator)
            return AdministratorSerializer(admin).data
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_administrator_by_credential(credential_id):
        """
        Returns the administrator with a given credential id

        :param credential_id: ID of credential
        :return: Administrator found or none
        """

        try:
            admin = Administrator.objects.get(credential_id=credential_id)
            return AdministratorSerializer(admin).data
        except ObjectDoesNotExist:
            return None
