"""
Model layer for state related operations
"""

import uuid
from django.db import models
from rest_framework import serializers


class State(models.Model):
    """
    Class that represents the state entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=127)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'

class StateSerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """

    class Meta:
        model = State
        fields = '__all__'
