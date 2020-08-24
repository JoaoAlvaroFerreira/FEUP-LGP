"""
Model layer for goniometry related operations
"""

import uuid
from django.db import models
from reportlab.platypus import Paragraph, Table

class Goniometry(models.Model):
    """
    Class that represents the goniometry entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    min_abduction = models.IntegerField()
    max_abduction = models.IntegerField()
    min_adduction = models.IntegerField()
    max_adduction = models.IntegerField()
    min_flexion = models.IntegerField()
    max_flexion = models.IntegerField()
    min_rotation = models.IntegerField()
    max_rotation = models.IntegerField()
    min_extension = models.IntegerField()
    max_extension = models.IntegerField()
    treatment = models.ForeignKey('Treatment', models.DO_NOTHING)
    body_zone = models.ForeignKey('BodyZone', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goniometry'

    def report(self, subtitle_topic_style, text_topic_style):
        """
         Generate report elements
         """

        return [Table([[Paragraph("Zona do Corpo", subtitle_topic_style),
                        # pylint: disable=no-member
                        Paragraph(self.body_zone.name, text_topic_style)
                        ]], colWidths=(150, None))]
