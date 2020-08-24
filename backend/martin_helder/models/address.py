"""
Model layer for address related operations
"""

import uuid
from django.db import models
from rest_framework import serializers

class Address(models.Model):
    """
    Class that represents the address entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=16)
    city = models.CharField(max_length=127)

    class Meta:
        managed = False
        db_table = 'address'


class AddressSerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """

    class Meta:
        model = Address
        fields = '__all__'
