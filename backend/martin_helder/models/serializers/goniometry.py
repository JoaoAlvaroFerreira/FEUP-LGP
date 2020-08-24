"""
Serializer layer for goniometry related operations
"""

from rest_framework import serializers

from martin_helder.models.goniometry import Goniometry
from martin_helder.models.bodyzone import BodyZoneSerializer


class GoniometrySerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """
    body_zone = BodyZoneSerializer()

    class Meta:
        model = Goniometry
        fields = '__all__'
