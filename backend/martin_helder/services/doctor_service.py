"""
Service layer for doctor related operations
"""
from sqlite3 import IntegrityError
from rest_framework.exceptions import ValidationError

from martin_helder.models import Doctor
from martin_helder.services.state_service import StateService


class DoctorService:
    """
    Service class for doctor related operations
    """

    @staticmethod
    def add_doctor(new_doctor_request):
        """
        Method to add a new doctor

        :param new_doctor_request: Information for the requested new doctor
        :return: ID of Doctor created
        """

        return_value = {}

        StateService.is_valid_state(new_doctor_request['state_id'])
        DoctorService.is_unique_professional_certificate(new_doctor_request['professional_certificate'])
        DoctorService.is_unique_email(new_doctor_request['email'])

        try:
            new_doctor = Doctor.objects.create(name=new_doctor_request['name'],
                                               professional_certificate=new_doctor_request['professional_certificate'],
                                               email=new_doctor_request['email'],
                                               state_id=new_doctor_request['state_id'])

        except IntegrityError as error:
            if 'unique constraint' in str(error):
                raise ValidationError("Unique constraint violation!"
                                      "Another doctor with the same professional certificate and/or email already "
                                      "exists!")

            raise ValidationError("Unexpected error creating doctor!")

        new_doctor.save()

        return_value['doctor_ID'] = new_doctor.id

        return return_value

    @staticmethod
    def is_unique_professional_certificate(professional_certificate):
        """
        Checks if the new doctor professional certificate is already registered with another doctor

        :param professional_certificate: Professional certificate of the new doctor
        """

        if Doctor.objects.filter(professional_certificate=professional_certificate).exists():
            raise ValidationError("There's already a Doctor registered with this professional certificate!")

    @staticmethod
    def is_unique_email(email):
        """
        Checks if the new doctor email is already registered with another doctor

        :param email: Email of the new doctor
        """

        if Doctor.objects.filter(email=email).exists():
            raise ValidationError("There's already a Doctor registered with this email!")
