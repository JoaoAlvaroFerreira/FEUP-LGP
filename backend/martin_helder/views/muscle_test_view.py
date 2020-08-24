"""
View layer of all muscle test related endpoints
"""

from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView


class MuscleTestView(APIView):
    """
    All endpoints related to muscle test actions
    """

    @staticmethod
    def validate_muscle_test_request(muscle_test_request):
        """
        Validates the muscle test information received in the request body

        :param muscle_test_request: Muscle test information received in the request
        """

        if 'strength' not in muscle_test_request:
            raise ValidationError("Missing strength in muscle test!")

        if 'body_zone' not in muscle_test_request:
            raise ValidationError("Missing body zone in muscle test!")

        if (not isinstance(muscle_test_request['strength'], int) or not
                1 <= muscle_test_request['strength'] <= 5):
            raise ValidationError("Muscle test strength must be a number between 1 and 5!")
