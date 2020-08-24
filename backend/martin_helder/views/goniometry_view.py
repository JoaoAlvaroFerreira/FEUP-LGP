"""
View layer of all goniometry related endpoints
"""

from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView


class GoniometryView(APIView):
    """
    All endpoints related to goniometry actions
    """

    @staticmethod
    def validate_goniometry_request(goniometry_request):
        """
        Validates the goniometry information received in the request body

        :param goniometry_request: Goniometry information received in the request
        """

        if 'body_zone' not in goniometry_request:
            raise ValidationError("Missing body zone in goniometry!")

        goniometry_elements = ['abduction', 'adduction', 'flexion', 'rotation', 'extension']

        for element in goniometry_elements:
            if (not isinstance(goniometry_request['min_'+element], int) or not
                    0 <= goniometry_request['min_'+element] <= 180):
                raise ValidationError("Goniometry minimum {} must be a number between 0 and 180!".format(element))

            if (not isinstance(goniometry_request['max_'+element], int) or not
                    0 <= goniometry_request['max_'+element] <= 180):
                raise ValidationError("Goniometry maximum {} must be a number between 0 and 180!".format(element))

            if goniometry_request['max_'+element] <= goniometry_request['min_'+element]:
                raise ValidationError("Goniometry maximum {0} must be greater than the minimum {0}"
                                      .format(element))
