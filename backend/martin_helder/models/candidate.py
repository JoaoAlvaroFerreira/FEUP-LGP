"""
Model layer for candidate related operations
"""

import uuid
from django.db import models

class Candidate(models.Model):
    """
    Class that represents the candidate entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    professional_certificate = models.CharField(max_length=11)
    curriculum = models.CharField(max_length=255)
    observations = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate'
