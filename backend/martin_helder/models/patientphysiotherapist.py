"""
Model layer for patient physiotherapist related operations
"""

import uuid
from django.db import models

class PatientPhysiotherapist(models.Model):
    """
    Class that represents the patient physiotherapist entity
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    physiotherapist = models.ForeignKey('Physiotherapist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_physiotherapist'
