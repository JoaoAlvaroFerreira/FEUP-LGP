"""
View layer of all address related endpoints
"""

from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView


class AddressView(APIView):
    """
    All endpoints related to address actions
    """

    @staticmethod
    def validate_address_request(address_request):
        """
        Validates the address information received in the request body

        :param address_request: address information received in the request
        """

        if 'street' not in address_request:
            raise ValidationError("Missing street in address!")

        if 'city' not in address_request:
            raise ValidationError("Missing city in address!")

        if 'zip_code' not in address_request:
            raise ValidationError("Missing zip code in address!")
