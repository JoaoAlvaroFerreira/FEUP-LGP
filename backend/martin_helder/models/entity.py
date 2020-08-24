"""
Model layer for entity related operations
"""

import uuid
from django.db import models

class Entity(models.Model):
    """
    Class that represents the entity entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity'
