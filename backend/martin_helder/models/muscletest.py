"""
Model layer for muscle test related operations
"""

import uuid
from django.db import models
from reportlab.platypus import Paragraph, Table

class MuscleTest(models.Model):
    """
    Class that represents the muscle test entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    strength = models.IntegerField()
    body_zone = models.ForeignKey('BodyZone', models.DO_NOTHING)
    treatment = models.ForeignKey('Treatment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'muscle_test'

    def report(self, subtitle_topic_style, text_topic_style):
        """
         Generate report elements
         """

        return [Table([[Paragraph("Zona do Corpo", subtitle_topic_style),
                        # pylint: disable=no-member
                        Paragraph(self.body_zone.name, text_topic_style)
                        ]], colWidths=(150, None))]
