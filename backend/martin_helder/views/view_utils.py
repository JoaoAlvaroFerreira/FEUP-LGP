"""
Utilitary module
"""

import datetime
import random
import string
from uuid import UUID
from dateutil import tz
from rest_framework.exceptions import ValidationError


class Utils:
    """
    Utilitary class
    """
    @staticmethod
    def validate_uuid(uuid, version=4):
        """
        Utilitary function that throws exception if the uuid is invalid
        """

        try:
            uuid_obj = UUID(uuid, version=version)
        except ValueError:
            raise ValidationError("Invalid uuid!")

    @staticmethod
    def get_expire_time(ttl):
        """
        Utilitary function that returns token expire time

        :param ttl: token time-to-live
        :return: token expire time
        """

        to_zone = tz.gettz('Portugal')
        utc = datetime.datetime.now()
        central = utc.astimezone(to_zone)

        return central + datetime.timedelta(seconds=ttl)

    @staticmethod
    def generate_random_password(string_length=8):
        """
        Utilitary function that generates a random password

        :return: random password
        """

        letters_and_digits = string.ascii_letters + string.digits
        return ''.join((random.choice(letters_and_digits) for i in range(string_length)))
