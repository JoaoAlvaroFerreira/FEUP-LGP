"""
Service layer for person related operations
"""

from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from martin_helder.models import Person
from martin_helder.services.address_service import AddressService
from martin_helder.views.view_utils import Utils


class PersonService:
    """
    Service class for person related operations
    """

    @staticmethod
    def is_valid_person(id_person):
        """
        Checks if the specified person exists

        :param id_person: ID of person to be checked
        """

        Utils.validate_uuid(id_person)

        if not Person.objects.filter(id=id_person).exists():
            raise ValidationError("The person is not valid!")

    @staticmethod
    def add_person(address_data, person_data):
        """
        Creates a new person

        :param address_data: list with street, zip_code and city, respectivly
        :param person_data: list with nif, first_name, last_name, birth_date, telephone_number and email, respectivly
        :return: Created person id
        """

        address = AddressService.check_address(address_data["street"], address_data["zip_code"], address_data["city"])

        if address is None:
            address = AddressService.add_address(address_data["street"], address_data["zip_code"], address_data["city"])

        try:
            new_person = Person.objects.create(address_id=address,
                                               nif=person_data["nif"],
                                               first_name=person_data["first_name"],
                                               last_name=person_data["last_name"],
                                               birth_date=person_data["birth_date"],
                                               telephone_number=person_data["telephone_number"],
                                               email=person_data["email"],
                                               gender=person_data["gender"])
        except IntegrityError as error:
            if 'unique constraint' in str(error):
                raise ValidationError("Unique contraint violation!"
                                      " Another user with the same nif and/or email already exists")

            raise ValidationError("Unexpected error creating person!")

        new_person.save()

        return new_person.id
