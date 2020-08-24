"""
Service layer for credential related operations
"""

from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password, make_password
from martin_helder.models.credential import Credential, CredentialSerializer
from martin_helder.views.view_utils import Utils

class CredentialService:
    """
    Service class for credential related operations
    """

    @staticmethod
    def add_credential(email):
        """
        Method create a new credential

        :param password: State name
        :return: Credential created id
        """

        password = Utils.generate_random_password()

        new_credential = Credential.objects.create(password=make_password(password), email=email)

        new_credential.save()

        # TODO: Send email with "password"
        print(f"PASSWORD: {password}")

        return new_credential.id

    @staticmethod
    def is_valid_credential(id_credential):
        """
        Checks if the specified credential exists

        :param id_credential: ID of credential to be checked
        """

        Utils.validate_uuid(id_credential)

        if not Credential.objects.filter(id=id_credential).exists():
            raise ValidationError("The credential " + id_credential + " is not valid!")

    @staticmethod
    def check_credential(email, password):
        """
        Checks if the credentials exists and returns it

        :param email: email to be checked
        :param password: password to be checked
        :return: Credential data found
        """

        try:
            credential = Credential.objects.get(email=email)
        except ObjectDoesNotExist:
            raise ValidationError(f"No account found with the email {email}!")

        if not check_password(password, credential.password):
            raise ValidationError("Wrong password!")

        return CredentialSerializer(credential).data

    @staticmethod
    def reset_password(id_credential, current_password, new_password):
        """
        Method that resets the password of a given credential

        :param id_credential: email to be checked
        :param current_password: credential current password
        :param new_password: new password to be changed
        """

        try:
            credential = Credential.objects.get(id=id_credential)
        except ObjectDoesNotExist:
            raise ValidationError("No credential found!")

        if not check_password(current_password, credential.password):
            raise ValidationError("Wrong current password!")

        credential.password = make_password(new_password)
        credential.save()

    @staticmethod
    def recover_password(email):
        """
        Method that recovers the password of a given credential

        :param email: email of the credential to be changed
        """

        try:
            credential = Credential.objects.get(email=email)
        except ObjectDoesNotExist:
            raise ValidationError(f"No account found with the email {email}!")

        password = Utils.generate_random_password()

        credential.password = make_password(password)
        credential.save()

        # TODO: Send email with new "password"
        print(f"NEW PASSWORD: {password}")
