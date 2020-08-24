"""
Model layer for person related operations
"""

import uuid
from django.db import models
from rest_framework import serializers

from martin_helder.models.address import AddressSerializer


class Person(models.Model):
    """
    Class that represents the person entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    address = models.ForeignKey('Address', models.DO_NOTHING)
    nif = models.CharField(unique=True, max_length=32)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    telephone_number = models.CharField(max_length=16)
    email = models.CharField(unique=True, max_length=127)
    gender = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'person'


class PersonSerializer(serializers.ModelSerializer):
    """
    Class the serializes the model
    """

    address = AddressSerializer()

    class Meta:
        model = Person
        fields = '__all__'
