"""
View layer of all credential related endpoints
"""

from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView


class CredentialView(APIView):
    """
    All endpoints related to credential actions
    """

    @staticmethod
    def validate_credential_request(credential_request):
        """
        Validates the credential information received in the request body

        :param credential_request: credential information received in the request
        """

        if 'password' not in credential_request:
            raise ValidationError("Missing password in credential!")
