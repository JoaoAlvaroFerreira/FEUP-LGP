"""
Model layer for treatment related operations
"""

import uuid
from django.db import models
from reportlab.platypus import Paragraph, Table

class Treatment(models.Model):
    """
   Class that represents the treatment entity
   """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    treatment_cycle = models.ForeignKey('TreatmentCycle', models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    pain_level = models.IntegerField(blank=True, null=True)
    medication = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    periodic_evaluation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treatment'

    def report(self, title_topic_style, text_topic_style, text_style, graph):
        """
        Generate report elements
        """

        return [Table([[Paragraph("Início", title_topic_style),
                        Paragraph("Fim", title_topic_style)],
                       [Paragraph(str(self.start_date), text_topic_style),
                        Paragraph(str(self.end_date), text_topic_style)]]),
                Paragraph("Nível de Dor", title_topic_style)] + \
         graph + \
                 [Paragraph("Sumário", title_topic_style),
                  Paragraph(self.summary, text_style),
                  Paragraph("Medicação", title_topic_style),
                  Paragraph(self.medication, text_style),
                  Paragraph("Tratamento", title_topic_style),
                  Paragraph(self.treatment, text_style),
                  Paragraph("Avaliação Periódica", title_topic_style),
                  Paragraph(self.periodic_evaluation, text_style)
                  ]
