"""
Model layer for perimetry related operations
"""

import uuid
from django.db import models
from reportlab.platypus import Paragraph, Table

class Perimetry(models.Model):
    """
    Class that represents the perimetry entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    size = models.IntegerField()
    treatment = models.ForeignKey('Treatment', models.DO_NOTHING)
    body_zone = models.ForeignKey('BodyZone', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'perimetry'

    def report(self, subtitle_topic_style, text_topic_style):
        """
        Generate report elements
        """

        return [Table([[Paragraph("Zona do Corpo", subtitle_topic_style),
                        # pylint: disable=no-member
                        Paragraph(self.body_zone.name, text_topic_style)
                        ]], colWidths=(150, None))]
