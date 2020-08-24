"""
View layer of all person related endpoints
"""
import re
from datetime import datetime
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from martin_helder.views.address_view import AddressView

class PersonView(APIView):
    """
    All endpoints related to person actions
    """

    @staticmethod
    def validate_person_request(person_request):
        """
        Validates the person information received in the request body

        :param person_request: person information received in the request
        """

        if 'nif' not in person_request:
            raise ValidationError("Missing nif in person!")

        if 'first_name' not in person_request:
            raise ValidationError("Missing first name in person!")

        if 'last_name' not in person_request:
            raise ValidationError("Missing last name in person!")

        if 'birth_date' not in person_request:
            raise ValidationError("Missing birth date in person!")

        if 'telephone_number' not in person_request:
            raise ValidationError("Missing telephone number in person!")

        if 'email' not in person_request:
            raise ValidationError("Missing email in person!")

        if 'gender' not in person_request:
            raise ValidationError("Missing gender in person!")

        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                    person_request['email']) is None:
            raise ValidationError('Invalid email format in person!')

        if 'gender' in person_request and not (person_request['gender'] == 'm' or person_request['gender'] == 'f'):
            raise ValidationError('Gender must be "m" or "f" in person!')

        if ('birth_date' in person_request and
                datetime.strptime(person_request['birth_date'], "%Y-%m-%d").date() >= datetime.now().date()):
            raise ValidationError('Birth date cannot be higher than current date in person!')

        if 'address' not in person_request:
            raise ValidationError("Missing address in person!")

        AddressView.validate_address_request(person_request['address'])
