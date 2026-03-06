"""
TISAX PDF Export Module
Generates professional PDF reports for TISAX assessments
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import io


class TISAXPDFExporter:
    """Generate professional TISAX assessment PDF reports"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom paragraph styles"""
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=20,
            textColor=colors.HexColor('#C4122E'),
            spaceAfter=12,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        self.styles.add(ParagraphStyle(
            name='SectionHeading',
            parent=self.styles['Heading2'],
            fontSize=12,
            textColor=colors.HexColor('#333333'),
            spaceAfter=8,
            spaceBefore=8,
            fontName='Helvetica-Bold'
        ))
        
        self.styles.add(ParagraphStyle(
            name='Normal',
            fontSize=10,
            textColor=colors.HexColor('#333333'),
            fontName='Helvetica',
            alignment=TA_JUSTIFY
        ))
        
        self.styles.add(ParagraphStyle(
            name='ResultYes',
            fontSize=14,
            textColor=colors.HexColor('#155724'),
            fontName='Helvetica-Bold',
            spaceAfter=10
        ))
        
        self.styles.add(ParagraphStyle(
            name='ResultNo',
            fontSize=14,
            textColor=colors.HexColor('#721c24'),
            fontName='Helvetica-Bold',
            spaceAfter=10
        ))
    
    def generate_pdf(self, assessment_data: dict, result: dict) -> bytes:
        """
        Generate PDF from assessment result
        
        Args:
            assessment_data: Form data dict from TISAXAssessment
            result: Result dict from TISAXAssessment.assess()
        
        Returns:
            PDF as bytes
        """
        pdf_buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=A4,
            rightMargin=1.5*cm,
            leftMargin=1.5*cm,
            topMargin=1.5*cm,
            bottomMargin=1.5*cm
        )
        
        story = []
        
        # Header
        story.append(Paragraph("TISAX Risikobewertung", self.styles['CustomTitle']))
        story.append(Spacer(1, 0.5*cm))
        
        # Company Information
        story.append(Paragraph("Unternehmensangaben", self.styles['SectionHeading']))
        
        company_table_data = [
            ["Unternehmensname:", assessment_data.get("unternehmensname", "N/A")],
            ["Abteilung:", assessment_data.get("abteilung", "N/A")],
            ["Kontaktperson:", assessment_data.get("kontaktperson", "N/A")],
            ["Bewertungsdatum:", datetime.now().strftime("%d.%m.%Y")]
        ]
        
        company_table = Table(company_table_data, colWidths=[4*cm, 12*cm])
        company_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#333333')),
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LINEBELOW', (0, -1), (-1, -1), 0.5, colors.grey)
        ]))
        story.append(company_table)
        story.append(Spacer(1, 0.5*cm))
        
        # Assessment Details
        story.append(Paragraph("Bewertungsdetails", self.styles['SectionHeading']))
        
        assessment_table_data = [
            ["Bereich", "Auswahl"],
            ["Vertraulichkeit", assessment_data.get("vertraulichkeit", "N/A")],
            ["Integrität", assessment_data.get("integritat", "N/A")],
            ["Verfügbarkeit", assessment_data.get("verfugbarkeit", "N/A")],
            ["Personenbezogene Daten", assessment_data.get("personenbezogene_daten", "N/A")],
            ["Besondere Kategorien", assessment_data.get("besondere_kategorien", "N/A")],
            ["Prototypen-Bauteile", assessment_data.get("bauteile", "N/A")],
            ["Prototypenfahrzeuge", assessment_data.get("fahrzeuge", "N/A")],
            ["Erprobungsfahrzeuge", assessment_data.get("erprobung", "N/A")],
            ["Prototypen bei Events", assessment_data.get("events", "N/A")]
        ]
        
        assessment_table = Table(assessment_table_data, colWidths=[7*cm, 9*cm])
        assessment_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e7f3ff')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#004085')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey)
        ]))
        story.append(assessment_table)
        story.append(Spacer(1, 0.5*cm))
        
        # Results
        story.append(Paragraph("Bewertungsergebnis", self.styles['SectionHeading']))
        
        if result["form_complete"]:
            if result["tisax_required"] is not None:
                if result["tisax_required"]:
                    story.append(Paragraph(
                        "✅ TISAX erforderlich: JA",
                        self.styles['ResultYes']
                    ))
                    story.append(Paragraph(
                        f"<b>Assessment-Level:</b> {result['assessment_level']}",
                        self.styles['Normal']
                    ))
                    story.append(Spacer(1, 0.3*cm))
                    
                    result_text = result["result_text"].replace('\n', '<br/>')
                    story.append(Paragraph(result_text, self.styles['Normal']))
                else:
                    story.append(Paragraph(
                        "❌ TISAX erforderlich: NEIN",
                        self.styles['ResultNo']
                    ))
                    story.append(Paragraph(result["result_text"], self.styles['Normal']))
            else:
                story.append(Paragraph("Bewertung konnte nicht durchgeführt werden.", self.styles['Normal']))
        else:
            story.append(Paragraph("Das Formular ist nicht vollständig ausgefüllt.", self.styles['Normal']))
        
        story.append(Spacer(1, 1*cm))
        
        # Signature field
        story.append(Paragraph("Genehmigung", self.styles['SectionHeading']))
        story.append(Spacer(1, 1*cm))
        story.append(Paragraph("_" * 50, self.styles['Normal']))
        story.append(Paragraph("Unterschrift & Datum", self.styles['Normal']))
        
        # Footer
        story.append(Spacer(1, 1*cm))
        story.append(Paragraph(
            "Porsche AG - Interne Nutzung<br/>Dieses Dokument ist vertraulich.",
            self.styles['Normal']
        ))
        
        # Build PDF
        doc.build(story)
        pdf_data = pdf_buffer.getvalue()
        pdf_buffer.close()
        
        return pdf_data
