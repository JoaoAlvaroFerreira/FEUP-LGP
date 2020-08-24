"""
Model layer for patient entity related operations
"""

import uuid
from django.db import models

class PatientEntity(models.Model):
    """
    Class that represents the patient entity entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    entity = models.ForeignKey('Entity', models.DO_NOTHING, blank=True, null=True)
    process_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'patient_entity'
