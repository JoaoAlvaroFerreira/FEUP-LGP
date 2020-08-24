"""
Model layer for patient related operations
"""

import uuid
from django.db import models


class Patient(models.Model):
    """
    Class that represents the patient entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    doctor = models.ForeignKey('Doctor', models.DO_NOTHING, blank=True, null=True)
    profession = models.CharField(max_length=127)
    diagnostic = models.TextField()
    clinical_history = models.TextField()
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'
