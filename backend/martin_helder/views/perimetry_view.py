"""
View layer of all perimetries related endpoints
"""

from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView


class PerimetryView(APIView):
    """
    All endpoints related to perimetries actions
    """

    @staticmethod
    def validate_perimetry_request(perimetry_request):
        """
        Validates the perimetry information received in the request body

        :param perimetry_request: Perimetry information received in the request
        """

        if 'size' not in perimetry_request:
            raise ValidationError("Missing size in perimetry!")

        if 'body_zone' not in perimetry_request:
            raise ValidationError("Missing body zone in perimetry!")

        if (not isinstance(perimetry_request['size'], int) or not
                0 <= perimetry_request['size'] <= 200):
            raise ValidationError("Perimetry size must be a number between 0 and 200!")
