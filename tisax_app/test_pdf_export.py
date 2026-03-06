"""
Test PDF Export Functionality
"""

from tisax_logic import TISAXAssessment
from tisax_pdf_export import TISAXPDFExporter
from datetime import datetime


def test_pdf_export():
    """Test PDF generation with sample data"""
    print("Testing PDF Export...")
    
    # Create sample assessment
    assessment = TISAXAssessment()
    assessment.set_data(
        unternehmensname="Porsche AG",
        abteilung="IT-Sicherheit",
        kontaktperson="Max Mustermann (max.mustermann@porsche.de)",
        vertraulichkeit="Geheim - Sehr hoher",
        integritat="Sehr hoher",
        verfugbarkeit="Hoher",
        personenbezogene_daten=True,
        besondere_kategorien=True,
        bauteile=True,
        fahrzeuge=True,
        erprobung=True,
        events=False
    )
    
    result = assessment.assess()
    
    # Add formatted date
    export_data = assessment.data.copy()
    export_data['datum_str'] = datetime.now().strftime('%d.%m.%Y')
    
    # Generate PDF
    exporter = TISAXPDFExporter()
    pdf_bytes = exporter.generate_pdf(result, export_data)
    
    # Save to file
    filename = f"/Users/nwe/clawd/tisax_app/test_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    with open(filename, 'wb') as f:
        f.write(pdf_bytes)
    
    print(f"✅ PDF exported successfully!")
    print(f"   File: {filename}")
    print(f"   Size: {len(pdf_bytes)} bytes")
    print(f"   TISAX Required: {result['tisax_required']}")
    print(f"   Assessment Level: {result['assessment_level']}")
    print(f"   Labels: {', '.join(result['labels'])}")
    
    return True


if __name__ == "__main__":
    try:
        success = test_pdf_export()
        exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
