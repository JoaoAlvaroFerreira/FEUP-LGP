"""
Model layer for doctor related operations
"""

import uuid
from django.db import models
from rest_framework import serializers


class Doctor(models.Model):
    """
    Class that represents the doctor entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    professional_certificate = models.CharField(max_length=16, unique=True)
    email = models.CharField(max_length=127, unique=True)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class DoctorSerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """

    class Meta:
        model = Doctor
        fields = '__all__'
