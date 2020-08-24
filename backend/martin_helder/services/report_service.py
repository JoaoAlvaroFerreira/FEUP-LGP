"""
Service layer for generating reports
"""

import io
import datetime
from dataclasses import dataclass

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Indenter, Table, Image, PageBreak
from reportlab.lib import utils
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_RIGHT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import PCMYKColor
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import HorizontalBarChart, VerticalBarChart
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class ReportService:
    """
    Service class for generating reports
    """

    # pylint: disable=too-many-instance-attributes
    @dataclass
    class BarChart:
        """
        Class for drawing a customized bar chart
        """

        data: []
        categories: []
        width: int
        height: int
        graph_x: int
        graph_y: int
        value_min: int
        value_max: int
        value_step: int

        def vertical_bar_chart(self):
            """
            Draws a vertical bar chart
            :return: vertical bar chart
            """

            drawing = Drawing(200, 280)
            graph = VerticalBarChart()
            graph.x = self.graph_x
            graph.y = self.graph_y

            graph.width = self.width
            graph.height = self.height

            graph.valueAxis.forceZero = 1
            graph.valueAxis.valueMin = self.value_min
            graph.valueAxis.valueMax = self.value_max
            graph.valueAxis.valueStep = self.value_step

            graph.data = self.data
            graph.categoryAxis.categoryNames = self.categories

            graph.barLabels.nudge = 15
            graph.barLabelFormat = '%dº'
            graph.barLabels.dx = 0
            graph.barLabels.dy = 0
            graph.barLabels.boxAnchor = 'n'
            graph.barLabels.fontName = 'Vera'
            graph.barLabels.fontSize = 10

            graph.bars[0].fillColor = PCMYKColor(45, 45, 0, 0, alpha=85)
            graph.bars[1].fillColor = PCMYKColor(70, 75, 0, 0, alpha=100)
            graph.bars.fillColor = PCMYKColor(64, 62, 0, 18, alpha=85)
            drawing.add(graph, '')

            return [drawing]

        def horizontal_bar_graph(self):
            """
            Draws a horizontal bar chart

            :return: horizontal bar chart
            """
            drawing = Drawing(200, 50)
            graph = HorizontalBarChart()
            graph.x = self.graph_x
            graph.y = self.graph_y

            graph.width = self.width
            graph.height = self.height

            graph.valueAxis.valueMin = self.value_min
            graph.valueAxis.valueMax = self.value_max
            graph.valueAxis.valueStep = self.value_step

            graph.data = self.data
            graph.categoryAxis.categoryNames = self.categories

            graph.barLabels.nudge = 15
            graph.barLabelFormat = '%d'
            graph.barLabels.dx = 0
            graph.barLabels.dy = 7
            graph.barLabels.boxAnchor = 'n'
            graph.barLabels.fontName = 'Vera'
            graph.barLabels.fontSize = 10

            graph.bars[0].fillColor = PCMYKColor(45, 45, 0, 0, alpha=85)
            graph.bars[1].fillColor = PCMYKColor(64, 75, 0, 18, alpha=95)
            graph.bars.fillColor = PCMYKColor(64, 62, 0, 18, alpha=85)
            drawing.add(graph, '')

            return [drawing]

    @staticmethod
    def _header_footer(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()

        # Header
        img = utils.ImageReader('https://www.martinhelder.pt/img/logotipo.png')
        img_w, img_h = img.getSize()
        header = Image('https://www.martinhelder.pt/img/logotipo.png', width=0.7 * img_w, height=0.7 * img_h)
        width, height = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin + 0 * width, doc.height + doc.topMargin - height + 35)

        # Footer
        right = ParagraphStyle('BodyText', alignment=TA_RIGHT, fontName='Vera')
        footer = Table([[Paragraph(str(doc.page), styles['BodyText']),
                         Paragraph("Documento gerado a " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                   right)]],
                       colWidths=(None, 0.8 * doc.width))
        footer.wrap(doc.width, doc.topMargin)
        footer.drawOn(canvas, doc.leftMargin, 0.6 * doc.bottomMargin)

        # Release the canvas
        canvas.restoreState()

    # pylint: disable=too-many-locals
    @staticmethod
    def treatment_report(treatment, treatment_cycle, goniometries, perimetries, muscle_tests):
        """
        Returns the list of relevant results for the searched query
        """

        pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
        pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
        pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
        pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

        sample_style_sheet = getSampleStyleSheet()
        buffer = io.BytesIO()

        my_doc = SimpleDocTemplate(buffer, rightMargin=50, leftMargin=50, topMargin=100)

        title = ParagraphStyle(name='title', parent=sample_style_sheet['Heading1'], fontSize=18, spaceAfter=15,
                               fontName='VeraBd')
        title_topic = ParagraphStyle(name='title_topic', parent=sample_style_sheet['Heading2'],
                                     spaceAfter=30, fontName='VeraBd')
        text_title_topic = ParagraphStyle(name='title_topic', parent=sample_style_sheet['Heading2'], leading=17,
                                          fontSize=13, fontName='VeraBd')
        subtitle_topic = ParagraphStyle(name='subtitle_topic', parent=sample_style_sheet['Heading3'],
                                        fontName='VeraBd')
        text = ParagraphStyle(name='text', parent=sample_style_sheet['BodyText'], fontSize=10,
                              alignment=TA_JUSTIFY, fontName='Vera')
        text_topic = ParagraphStyle(name='text_topic', parent=sample_style_sheet['BodyText'], leading=25,
                                    fontSize=12, fontName='Vera')
        horizontal_text_topic = ParagraphStyle(name='text_topic', parent=sample_style_sheet['BodyText'], fontSize=12,
                                               fontName='Vera')

        chart = ReportService.BarChart([[treatment.pain_level]], ["Dor"], width=250, height=20, graph_x=30, graph_y=20,
                                       value_min=0, value_max=10, value_step=1)
        flowables = [Paragraph("Relatório de Tratamento", title)] + [Spacer(1, 0.40 * inch)] +\
                    treatment_cycle.report(title_topic, text_topic) + treatment.report(text_title_topic, text_topic,
                                                                                       text,
                                                                                       chart.horizontal_bar_graph())

        flowables += [PageBreak(), Paragraph("Perimetrias", title_topic)]
        for perimetry in perimetries:
            chart = ReportService.BarChart([[perimetry.size]], ["Tamanho"], width=350, height=30, graph_x=30,
                                           graph_y=-5, value_min=0, value_max=200, value_step=20)
            flowables += [Indenter("1cm")] + perimetry.report(subtitle_topic, horizontal_text_topic) + \
                         chart.horizontal_bar_graph() + [Indenter("-1cm"), Spacer(1, 0.60 * inch)]

        flowables += [PageBreak(), Paragraph("Testes Musculares", title_topic)]
        for muscle_test in muscle_tests:
            chart = ReportService.BarChart([[muscle_test.strength]], ["Força"], width=350, height=30, graph_x=30,
                                           graph_y=-5, value_min=0, value_max=5, value_step=1)
            flowables += [Indenter("1cm")] + muscle_test.report(subtitle_topic, horizontal_text_topic) + \
                         chart.horizontal_bar_graph() + [Indenter("-1cm"), Spacer(1, 0.60 * inch)]

        flowables += [PageBreak(), Paragraph("Goniometrias", title_topic)]
        page_break = False
        for goniometry in goniometries:
            chart_data = [[goniometry.min_abduction, goniometry.min_adduction,
                           goniometry.min_flexion, goniometry.min_rotation, goniometry.min_extension],
                          [goniometry.max_abduction,
                           goniometry.max_adduction,
                           goniometry.max_flexion,
                           goniometry.max_rotation,
                           goniometry.max_extension]]
            chart = ReportService.BarChart(chart_data, ['Abdução', 'Adução', 'Flexão', 'Rotação', 'Extensão'],
                                           width=350, height=150, graph_x=30, graph_y=65, value_min=0, value_max=180,
                                           value_step=20)
            flowables += [Indenter("1cm")] + goniometry.report(subtitle_topic, horizontal_text_topic) + \
                         chart.vertical_bar_chart() + [Indenter("-1cm")]

            if page_break:
                flowables += [PageBreak()]

            page_break = not page_break

        my_doc.build(flowables, onFirstPage=ReportService._header_footer,
                     onLaterPages=ReportService._header_footer)

        buffer.seek(0)

        return buffer
