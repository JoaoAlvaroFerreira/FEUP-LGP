"""
Service layer for muscle test related operations
"""

from rest_framework.exceptions import ValidationError

from martin_helder.services.body_zone_service import BodyZoneService
from martin_helder.models.muscletest import MuscleTest
from martin_helder.models.serializers.muscletest import MuscleTestSerializer
from martin_helder.views.view_utils import Utils


class MuscleTestService:
    """
    Service class for muscle test related operations
    """

    @staticmethod
    def is_valid_muscle_test(muscle_test_id):
        """
        Checks if the specified muscle_test exists

        :param muscle_test_id: if of the muscle_test
        """

        Utils.validate_uuid(muscle_test_id)

        if not MuscleTest.objects.filter(id=muscle_test_id).exists():
            raise ValidationError("The muscle test is not valid!")

    @staticmethod
    def add_muscle_test(muscle_test, id_treatment):
        """
        Creates a muscle test for a new treatment

        :param muscle_test: Muscle test info
        :param id_treatment: Corresponding treatment
        :return: Created Muscle test
        """

        BodyZoneService.is_valid_body_zone(muscle_test['body_zone'])

        new_muscle_test = MuscleTest.objects.create(strength=muscle_test['strength'],
                                                    body_zone_id=muscle_test['body_zone'],
                                                    treatment_id=id_treatment)

        new_muscle_test.save()

        return new_muscle_test.id

    @staticmethod
    def muscle_test_info(muscle_test_id):
        """
        Method that acquires information about a specific muscle_test

        :param muscle_test_id: id of the muscle_test
        :return: Serializer of muscle_test
        """

        MuscleTestService.is_valid_muscle_test(muscle_test_id)

        try:
            muscle_test = MuscleTest.objects.get(id=muscle_test_id)
        except:
            raise ValidationError("The muscle test is not valid!")

        muscle_test_data = MuscleTestSerializer(muscle_test).data

        return muscle_test_data
