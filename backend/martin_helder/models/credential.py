"""
Model layer for credential related operations
"""
import uuid

from django.db import models
from rest_framework import serializers

class Credential(models.Model):
    """
   Class that represents the credential entity
   """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    password = models.CharField(max_length=128)
    email = models.CharField(unique=True, max_length=127)

    class Meta:
        managed = False
        db_table = 'credential'

class CredentialSerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """

    class Meta:
        model = Credential
        exclude = ('password',)
