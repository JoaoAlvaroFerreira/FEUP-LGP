"""
Serializer layer for perimetry related operations
"""

from rest_framework import serializers

from martin_helder.models.perimetry import Perimetry
from martin_helder.models.bodyzone import BodyZoneSerializer

class PerimetrySerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """
    body_zone = BodyZoneSerializer()

    class Meta:
        model = Perimetry
        fields = '__all__'
