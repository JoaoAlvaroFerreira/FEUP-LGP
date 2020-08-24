"""
Model layer for body zone related operations
"""

import uuid
from django.db import models
from rest_framework import serializers

class BodyZone(models.Model):
    """
    Class that represents the body zone entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'body_zone'

class BodyZoneSerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """

    class Meta:
        model = BodyZone
        fields = '__all__'
