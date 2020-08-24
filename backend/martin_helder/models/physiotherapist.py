"""
Model layer for physiotherapist related operations
"""

import uuid
from django.db import models
from rest_framework import serializers
from martin_helder.models.person import PersonSerializer
from martin_helder.models.state import StateSerializer

class Physiotherapist(models.Model):
    """
    Class that represents the physiotherapist entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True)
    professional_certificate = models.CharField(max_length=11)
    candidate_date = models.DateField()
    curriculum = models.CharField(max_length=255)
    credential = models.ForeignKey('Credential', models.DO_NOTHING)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True)

    class Meta:
        managed = False
        db_table = 'physiotherapist'

class PhysiotherapistSerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """

    person = PersonSerializer()
    state = StateSerializer()

    class Meta:
        model = Physiotherapist
        fields = '__all__'
