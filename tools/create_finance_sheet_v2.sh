#!/bin/bash
#
# Create Finance Tracking Google Sheet
# Since gog doesn't support Sheets API directly, we'll create a workaround
#

set -e

ACCOUNT="nweferling82@gmail.com"
DOKUMENTE_FOLDER="1oIUHv-wOSDFNAl2wy0g5Smf5Nu0Mrwxe"

echo "📊 Creating Finanz-Übersicht manually via browser..."
echo ""
echo "I'll create CSV templates that you can import into a new Google Sheet."
echo "Then I'll set it up with all formulas and formatting!"
echo ""

# Create temporary CSVs
cat > /tmp/finance_2026.csv << 'EOF'
Datum,Firma,Kategorie,Betrag (€),MwSt (€),Zahlart,Status,Steuerrelevant,Drive Link,Notizen
2026-01-30,Beispiel GmbH,Shopping,99.99,15.99,Amex,Bezahlt,Nein,,Beispiel-Eintrag
EOF

cat > /tmp/finance_kategorien.csv << 'EOF'
Kategorie,Budget (€),Icon,Beschreibung
Wohnen,1500,🏠,"Miete Nebenkosten Möbel"
Transport,300,🚗,"Auto ÖPNV Taxi Benzin"
Lebensmittel,500,🛒,"Supermarkt Restaurants"
Business,200,💼,"Software Tools Büromaterial"
Reisen,1000,✈️,"Flüge Hotels Aktivitäten"
Shopping,300,🛍️,"Kleidung Elektronik Sonstiges"
Gesundheit,150,🏥,"Arzt Apotheke Versicherung"
Utilities,200,💡,"Strom Internet Telefon"
Bildung,100,🎓,"Kurse Bücher"
Unterhaltung,100,🎮,"Streaming Gaming Events"
Finanzen,50,💳,"Steuern Gebühren Zinsen"
Sonstiges,100,🎁,"Alles Andere"
EOF

echo "✅ CSV templates created in /tmp/"
echo ""
echo "📋 Next steps:"
echo "1. Go to https://sheets.google.com"
echo "2. Create new sheet: 'Finanz-Übersicht'"
echo "3. Create 4 tabs: Dashboard, 2026, Kategorien, Statistiken"
echo "4. Import /tmp/finance_2026.csv into '2026' tab"
echo "5. Import /tmp/finance_kategorien.csv into 'Kategorien' tab"
echo "6. Share the Sheet URL with me"
echo ""
echo "Then I'll add all the formulas, charts, and formatting!"

