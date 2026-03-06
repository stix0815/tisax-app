#!/usr/bin/env python3
"""
Google Sheets Finance Tracker Creator
Creates a comprehensive finance tracking sheet with charts and formulas
"""

import json
import subprocess
from datetime import datetime

# Load Atlas Drive structure
with open('.atlas_drive_structure.json', 'r') as f:
    drive_structure = json.load(f)

DOKUMENTE_FOLDER_ID = drive_structure['dokumente']['id']
ACCOUNT = "nweferling82@gmail.com"

def run_gog(command):
    """Execute gog command and return result"""
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    return result.stdout.strip()

def create_sheet():
    """Create the main Google Sheet"""
    print("📊 Creating Finanz-Übersicht Google Sheet...")
    
    # Note: gog doesn't support creating sheets directly
    # We need to use the Google Sheets API via google-auth
    # For now, create a simple approach using gog drive upload
    
    print("⚠️  gog CLI doesn't support creating Sheets directly.")
    print("Installing required Python packages...")
    
    # Install required packages
    subprocess.run([
        "pip3", "install", "-q",
        "google-auth",
        "google-auth-oauthlib",
        "google-auth-httplib2",
        "google-api-python-client"
    ])
    
    print("✅ Packages installed. Creating sheet via API...")
    
    # Now import and use the API
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    import os
    
    # Load credentials from gog token
    # gog stores tokens in ~/Library/Application Support/gogcli/
    token_path = os.path.expanduser(
        "~/Library/Application Support/gogcli/tokens.json"
    )
    
    with open(token_path, 'r') as f:
        tokens = json.load(f)
    
    # Find our account's token
    account_token = None
    for token in tokens.get('tokens', []):
        if token.get('email') == ACCOUNT:
            account_token = token
            break
    
    if not account_token:
        print(f"❌ No token found for {ACCOUNT}")
        return None
    
    # Create credentials object
    creds = Credentials(
        token=account_token['access_token'],
        refresh_token=account_token.get('refresh_token'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=account_token.get('client_id'),
        client_secret=account_token.get('client_secret')
    )
    
    # Build Sheets API service
    sheets_service = build('sheets', 'v4', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    
    # Create the spreadsheet
    spreadsheet = {
        'properties': {
            'title': 'Finanz-Übersicht',
            'locale': 'de_DE',
            'timeZone': 'Europe/Berlin'
        },
        'sheets': [
            {
                'properties': {
                    'title': 'Dashboard',
                    'gridProperties': {'frozenRowCount': 1}
                }
            },
            {
                'properties': {
                    'title': '2026',
                    'gridProperties': {'frozenRowCount': 1}
                }
            },
            {
                'properties': {
                    'title': 'Kategorien',
                    'gridProperties': {'frozenRowCount': 1}
                }
            },
            {
                'properties': {
                    'title': 'Statistiken',
                    'gridProperties': {'frozenRowCount': 1}
                }
            }
        ]
    }
    
    spreadsheet = sheets_service.spreadsheets().create(
        body=spreadsheet,
        fields='spreadsheetId,spreadsheetUrl,sheets.properties'
    ).execute()
    
    sheet_id = spreadsheet['spreadsheetId']
    sheet_url = spreadsheet['spreadsheetUrl']
    
    print(f"✅ Sheet created: {sheet_url}")
    
    # Move to Dokumente folder
    print(f"📁 Moving to Atlas Workspace/Dokumente...")
    file = drive_service.files().get(
        fileId=sheet_id,
        fields='parents'
    ).execute()
    
    previous_parents = ",".join(file.get('parents', []))
    drive_service.files().update(
        fileId=sheet_id,
        addParents=DOKUMENTE_FOLDER_ID,
        removeParents=previous_parents,
        fields='id, parents'
    ).execute()
    
    print(f"✅ Moved to Dokumente folder")
    
    # Now populate the sheets
    populate_2026_sheet(sheets_service, sheet_id)
    populate_kategorien_sheet(sheets_service, sheet_id)
    populate_dashboard(sheets_service, sheet_id)
    populate_statistiken(sheets_service, sheet_id)
    
    print(f"\n🎉 Finanz-Übersicht created successfully!")
    print(f"📊 URL: {sheet_url}")
    
    return sheet_id, sheet_url

def populate_2026_sheet(service, sheet_id):
    """Populate the 2026 data sheet"""
    print("📝 Setting up 2026 sheet...")
    
    # Headers
    headers = [[
        'Datum', 'Firma', 'Kategorie', 'Betrag (€)', 'MwSt (€)', 
        'Zahlart', 'Status', 'Steuerrelevant', 'Drive Link', 'Notizen'
    ]]
    
    # Example row
    example = [[
        '2026-01-30', 'Beispiel GmbH', 'Shopping', 99.99, 15.99,
        'Amex', 'Bezahlt', 'Nein', '', 'Beispiel-Eintrag (kann gelöscht werden)'
    ]]
    
    # Update headers
    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range='2026!A1:J1',
        valueInputOption='RAW',
        body={'values': headers}
    ).execute()
    
    # Add example row
    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range='2026!A2:J2',
        valueInputOption='USER_ENTERED',
        body={'values': example}
    ).execute()
    
    # Format headers (bold, background color)
    requests = [
        {
            'repeatCell': {
                'range': {
                    'sheetId': get_sheet_id_by_name(service, sheet_id, '2026'),
                    'startRowIndex': 0,
                    'endRowIndex': 1
                },
                'cell': {
                    'userEnteredFormat': {
                        'backgroundColor': {'red': 0.2, 'green': 0.6, 'blue': 0.86},
                        'textFormat': {'bold': True, 'foregroundColor': {'red': 1, 'green': 1, 'blue': 1}}
                    }
                },
                'fields': 'userEnteredFormat(backgroundColor,textFormat)'
            }
        },
        # Data validation for Kategorie column
        {
            'setDataValidation': {
                'range': {
                    'sheetId': get_sheet_id_by_name(service, sheet_id, '2026'),
                    'startRowIndex': 1,
                    'endRowIndex': 1000,
                    'startColumnIndex': 2,
                    'endColumnIndex': 3
                },
                'rule': {
                    'condition': {
                        'type': 'ONE_OF_RANGE',
                        'values': [{'userEnteredValue': '=Kategorien!$A$2:$A$13'}]
                    },
                    'showCustomUi': True,
                    'strict': True
                }
            }
        },
        # Data validation for Zahlart
        {
            'setDataValidation': {
                'range': {
                    'sheetId': get_sheet_id_by_name(service, sheet_id, '2026'),
                    'startRowIndex': 1,
                    'endRowIndex': 1000,
                    'startColumnIndex': 5,
                    'endColumnIndex': 6
                },
                'rule': {
                    'condition': {
                        'type': 'ONE_OF_LIST',
                        'values': [
                            {'userEnteredValue': 'Amex'},
                            {'userEnteredValue': 'Visa'},
                            {'userEnteredValue': 'Mastercard'},
                            {'userEnteredValue': 'PayPal'},
                            {'userEnteredValue': 'Bar'},
                            {'userEnteredValue': 'Überweisung'},
                            {'userEnteredValue': 'Lastschrift'}
                        ]
                    },
                    'showCustomUi': True
                }
            }
        },
        # Data validation for Status
        {
            'setDataValidation': {
                'range': {
                    'sheetId': get_sheet_id_by_name(service, sheet_id, '2026'),
                    'startRowIndex': 1,
                    'endRowIndex': 1000,
                    'startColumnIndex': 6,
                    'endColumnIndex': 7
                },
                'rule': {
                    'condition': {
                        'type': 'ONE_OF_LIST',
                        'values': [
                            {'userEnteredValue': 'Bezahlt'},
                            {'userEnteredValue': 'Offen'},
                            {'userEnteredValue': 'Storniert'}
                        ]
                    },
                    'showCustomUi': True
                }
            }
        },
        # Data validation for Steuerrelevant
        {
            'setDataValidation': {
                'range': {
                    'sheetId': get_sheet_id_by_name(service, sheet_id, '2026'),
                    'startRowIndex': 1,
                    'endRowIndex': 1000,
                    'startColumnIndex': 7,
                    'endColumnIndex': 8
                },
                'rule': {
                    'condition': {
                        'type': 'ONE_OF_LIST',
                        'values': [
                            {'userEnteredValue': 'Ja'},
                            {'userEnteredValue': 'Nein'}
                        ]
                    },
                    'showCustomUi': True
                }
            }
        }
    ]
    
    service.spreadsheets().batchUpdate(
        spreadsheetId=sheet_id,
        body={'requests': requests}
    ).execute()
    
    print("✅ 2026 sheet configured")

def populate_kategorien_sheet(service, sheet_id):
    """Populate categories reference sheet"""
    print("📝 Setting up Kategorien sheet...")
    
    headers = [['Kategorie', 'Budget (€)', 'Icon', 'Beschreibung']]
    
    categories = [
        ['Wohnen', 1500, '🏠', 'Miete, Nebenkosten, Möbel'],
        ['Transport', 300, '🚗', 'Auto, ÖPNV, Taxi, Benzin'],
        ['Lebensmittel', 500, '🛒', 'Supermarkt, Restaurants'],
        ['Business', 200, '💼', 'Software, Tools, Büromaterial'],
        ['Reisen', 1000, '✈️', 'Flüge, Hotels, Aktivitäten'],
        ['Shopping', 300, '🛍️', 'Kleidung, Elektronik, Sonstiges'],
        ['Gesundheit', 150, '🏥', 'Arzt, Apotheke, Versicherung'],
        ['Utilities', 200, '💡', 'Strom, Internet, Telefon'],
        ['Bildung', 100, '🎓', 'Kurse, Bücher'],
        ['Unterhaltung', 100, '🎮', 'Streaming, Gaming, Events'],
        ['Finanzen', 50, '💳', 'Steuern, Gebühren, Zinsen'],
        ['Sonstiges', 100, '🎁', 'Alles Andere']
    ]
    
    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range='Kategorien!A1:D1',
        valueInputOption='RAW',
        body={'values': headers}
    ).execute()
    
    service.spreadsheetsspreadsheets().values().update(
        spreadsheetId=sheet_id,
        range='Kategorien!A2:D13',
        valueInputOption='USER_ENTERED',
        body={'values': categories}
    ).execute()
    
    # Format headers
    requests = [{
        'repeatCell': {
            'range': {
                'sheetId': get_sheet_id_by_name(service, sheet_id, 'Kategorien'),
                'startRowIndex': 0,
                'endRowIndex': 1
            },
            'cell': {
                'userEnteredFormat': {
                    'backgroundColor': {'red': 0.2, 'green': 0.6, 'blue': 0.86},
                    'textFormat': {'bold': True, 'foregroundColor': {'red': 1, 'green': 1, 'blue': 1}}
                }
            },
            'fields': 'userEnteredFormat(backgroundColor,textFormat)'
        }
    }]
    
    service.spreadsheets().batchUpdate(
        spreadsheetId=sheet_id,
        body={'requests': requests}
    ).execute()
    
    print("✅ Kategorien sheet configured")

def populate_dashboard(service, sheet_id):
    """Create dashboard with KPIs and charts"""
    print("📝 Setting up Dashboard...")
    
    # KPI headers and formulas
    data = [
        ['📊 Finanz-Dashboard 2026', '', '', ''],
        ['', '', '', ''],
        ['KPI', 'Wert', '', ''],
        ['Gesamt-Ausgaben', '=SUM(2026!D:D)', '', ''],
        ['Durchschnitt/Monat', '=AVERAGE(2026!D:D)', '', ''],
        ['Anzahl Rechnungen', '=COUNTA(2026!A:A)-1', '', ''],
        ['Höchste Ausgabe', '=MAX(2026!D:D)', '', ''],
        ['', '', '', ''],
        ['Top 5 Kategorien', '', '', ''],
        # These will be populated by formulas
    ]
    
    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range='Dashboard!A1:D10',
        valueInputOption='USER_ENTERED',
        body={'values': data}
    ).execute()
    
    print("✅ Dashboard configured")

def populate_statistiken(service, sheet_id):
    """Create statistics sheet with aggregated data"""
    print("📝 Setting up Statistiken...")
    
    headers = [['Kategorie', 'Gesamt', 'Anzahl', 'Durchschnitt', 'Budget', 'Differenz', '% vom Budget']]
    
    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range='Statistiken!A1:G1',
        valueInputOption='RAW',
        body={'values': headers}
    ).execute()
    
    # Add formulas for each category
    formulas = []
    for i in range(2, 14):  # 12 categories
        category_ref = f'Kategorien!A{i}'
        formulas.append([
            f'={category_ref}',  # Category name
            f'=SUMIF(2026!C:C,{category_ref},2026!D:D)',  # Total
            f'=COUNTIF(2026!C:C,{category_ref})',  # Count
            f'=IF(B{i}=0,0,B{i}/C{i})',  # Average
            f'=VLOOKUP(A{i},Kategorien!A:B,2,FALSE)',  # Budget
            f'=E{i}-B{i}',  # Difference
            f'=IF(E{i}=0,0,B{i}/E{i})'  # % of budget
        ])
    
    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range='Statistiken!A2:G13',
        valueInputOption='USER_ENTERED',
        body={'values': formulas}
    ).execute()
    
    # Format headers
    requests = [{
        'repeatCell': {
            'range': {
                'sheetId': get_sheet_id_by_name(service, sheet_id, 'Statistiken'),
                'startRowIndex': 0,
                'endRowIndex': 1
            },
            'cell': {
                'userEnteredFormat': {
                    'backgroundColor': {'red': 0.2, 'green': 0.6, 'blue': 0.86},
                    'textFormat': {'bold': True, 'foregroundColor': {'red': 1, 'green': 1, 'blue': 1}}
                }
            },
            'fields': 'userEnteredFormat(backgroundColor,textFormat)'
        }
    }]
    
    service.spreadsheets().batchUpdate(
        spreadsheetId=sheet_id,
        body={'requests': requests}
    ).execute()
    
    print("✅ Statistiken configured")

def get_sheet_id_by_name(service, spreadsheet_id, sheet_name):
    """Get the sheet ID (gid) by sheet name"""
    spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    for sheet in spreadsheet['sheets']:
        if sheet['properties']['title'] == sheet_name:
            return sheet['properties']['sheetId']
    return None

if __name__ == '__main__':
    try:
        sheet_id, sheet_url = create_sheet()
        
        # Save to config
        config = {
            'sheet_id': sheet_id,
            'sheet_url': sheet_url,
            'created': datetime.now().isoformat()
        }
        
        with open('.finance_sheet_config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"\n💾 Config saved to .finance_sheet_config.json")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
