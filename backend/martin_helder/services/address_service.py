"""
Service layer for address related operations
"""

from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from martin_helder.models import Address


from martin_helder.views.view_utils import Utils

class AddressService:
    """
    Service class for address related operations
    """

    @staticmethod
    def add_address(street, zip_code, city):
        """
        Method create a new address

        :param street: Address street
        :param zip_code: Address zip code
        :param city: Address city
        :return: Address created id
        """

        new_address = Address.objects.create(street=street, zip_code=zip_code, city=city)

        new_address.save()

        return new_address.id

    @staticmethod
    def check_address(street, zip_code, city):
        """
        Returns the address if it exists or none

        :param street: Address street
        :param zip_code: Address zip code
        :param city: Address city
        :return: Address found or none
        """
        try:
            address = Address.objects.get(street=street, zip_code=zip_code, city=city)
            return address.id
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def is_valid_address(id_address):
        """
        Checks if the specified address exists

        :param id_address: ID of address to be checked
        """

        Utils.validate_uuid(id_address)

        if not Address.objects.filter(id=id_address).exists():
            raise ValidationError("The address " + id_address + " is not valid!")
