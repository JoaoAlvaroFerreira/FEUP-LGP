"""
Model layer for contact related operations
"""

import uuid
from django.db import models

class Contact(models.Model):
    """
    Class that represents the contact entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    cellphone_number = models.CharField(max_length=16)
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    patient_relation = models.CharField(max_length=127)

    class Meta:
        managed = False
        db_table = 'contact'
