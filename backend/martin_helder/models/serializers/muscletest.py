"""
Serializer layer for muscle test related operations
"""

from rest_framework import serializers

from martin_helder.models.muscletest import MuscleTest
from martin_helder.models.bodyzone import BodyZoneSerializer


class MuscleTestSerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """
    body_zone = BodyZoneSerializer()

    class Meta:
        model = MuscleTest
        fields = '__all__'
