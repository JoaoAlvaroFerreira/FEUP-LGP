"""
Model layer for administrator related operations
"""
import uuid

from django.db import models
from rest_framework import serializers
from martin_helder.models.person import PersonSerializer
from martin_helder.models.state import StateSerializer

class Administrator(models.Model):
    """
    Class that represents the administrator entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    credential = models.ForeignKey('Credential', models.DO_NOTHING, unique=True)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True)

    class Meta:
        managed = False
        db_table = 'administrator'


class AdministratorSerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """

    person = PersonSerializer()
    state = StateSerializer()

    class Meta:
        model = Administrator
        fields = '__all__'
