"""
Model layer for treatment cycle related operations
"""

import uuid
from django.db import models
from rest_framework import serializers
from reportlab.platypus import Paragraph, Table

class TreatmentCycle(models.Model):
    """
    Class that represents the treatment cycle entity
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    physiotherapist = models.ForeignKey('Physiotherapist', models.DO_NOTHING, blank=True, null=True)
    number_of_sessions = models.IntegerField()
    completed_sessions = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'treatment_cycle'

    def report(self, title_topic_style, text_topic_style):
        """
        Generate report elements
        """

        return [Table([[Paragraph("Paciente", title_topic_style),
                        Paragraph("Fisioterapeuta", title_topic_style)],
                       # pylint: disable=no-member
                       [Paragraph(self.patient.person.first_name + ' ' + self.patient.person.last_name,
                                  text_topic_style),
                        # pylint: disable=no-member
                        Paragraph(self.physiotherapist.person.first_name + ' ' + self.physiotherapist.person.last_name,
                                  text_topic_style)],
                       [Paragraph("Sessões", title_topic_style)],
                       [Paragraph("Completadas " + str(self.completed_sessions) + " de " + str(self.number_of_sessions)
                                  + " sessões", text_topic_style)
                       ]])]

class TreatmentCycleSerializer(serializers.ModelSerializer):
    """
    Class the serializes the model
    """

    class Meta:
        model = TreatmentCycle
        fields = '__all__'
