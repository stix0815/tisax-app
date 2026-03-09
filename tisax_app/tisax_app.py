"""
TISAX Risikobewertung Streamlit App
Professional risk assessment tool for Porsche internal use
"""

import streamlit as st
from datetime import datetime
from tisax_logic import TISAXAssessment
from tisax_pdf_export import TISAXPDFExporter

# Page config
st.set_page_config(
    page_title="TISAX Risikobewertung",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
        .main { padding-top: 0; }
        .stTabs [data-baseweb="tab-list"] button { font-size: 16px; font-weight: 500; }
        
        .result-box {
            border-radius: 10px;
            padding: 20px;
            margin: 15px 0;
            font-size: 16px;
        }
        .result-yes {
            background-color: #d4edda;
            border-left: 4px solid #28a745;
            color: #155724;
        }
        .result-no {
            background-color: #f8d7da;
            border-left: 4px solid #dc3545;
            color: #721c24;
        }
        .result-title {
            font-weight: bold;
            font-size: 24px;
            color: #000;
        }
        .result-text {
            font-size: 14px;
            line-height: 1.6;
            margin-top: 15px;
            color: #000;
        }
        .al-box {
            background-color: #e7f3ff;
            border-left: 4px solid #0066cc;
            color: #004085;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .info-box {
            background-color: #f0f8ff;
            border-left: 4px solid #0066cc;
            color: #004085;
            padding: 12px;
            border-radius: 5px;
            margin: 10px 0;
            font-size: 13px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "assessment" not in st.session_state:
    st.session_state.assessment = TISAXAssessment()

# Title
st.title("🔒 TISAX Risikobewertung")
st.markdown("Porsche AG - Interne Bewertung für Lieferanten & Dienstleister")

# Main tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 Allgemeine Informationen",
    "🔐 Informationssicherheit",
    "📊 Datenschutz",
    "🏭 Prototypenschutz",
    "✅ Ergebnis"
])

# TAB 1: General Information
with tab1:
    st.subheader("Allgemeine Informationen")
    
    col1, col2 = st.columns(2)
    with col1:
        kontaktperson = st.text_input(
            "Kontaktperson *",
            value=st.session_state.assessment.data.get("kontaktperson", ""),
            placeholder="Erforderlich",
            key="kontaktperson"
        )
        st.session_state.assessment.data["kontaktperson"] = kontaktperson
        
        abteilung = st.text_input(
            "Abteilung *",
            value=st.session_state.assessment.data.get("abteilung", ""),
            placeholder="Erforderlich",
            key="abteilung"
        )
        st.session_state.assessment.data["abteilung"] = abteilung
    
    with col2:
        unternehmensname = st.text_input(
            "Unternehmensname (falls bekannt)",
            value=st.session_state.assessment.data.get("unternehmensname", ""),
            key="unternehmensname"
        )
        st.session_state.assessment.data["unternehmensname"] = unternehmensname
        
        st.text_input(
            "Datum",
            value=datetime.now().strftime("%Y-%m-%d"),
            disabled=True
        )
        st.session_state.assessment.data["datum"] = datetime.now()
    
    # Ausnahmeregelungen Section
    st.markdown("---")
    st.markdown("### ℹ️ Wichtig: Ausnahmeregelungen")
    
    st.markdown("""
    Eine **TISAX-Zertifizierung ist NICHT notwendig**, wenn:
    """)
    
    with st.expander("🏢 1. Behördlich regulierte Institutionen", expanded=False):
        st.markdown("""
        Das Geschäftspartnerunternehmen ist eine der folgenden behördlich regulierten Institutionen:
        
        - 🏦 **Finanzinstitute** (Banken, Versicherungen)
        - 👨‍⚕️ **Ärzte**
        - 🏥 **Krankenkassen**
        - 📊 **Steuerberater**
        - ⚖️ **Rechtsanwälte**
        - 👔 **Wirtschaftsprüfer** (im Rahmen einer amtlichen Prüfung)
        
        **Grund:** Gesetzliche Bestimmungen zur Vertraulichkeit
        """)
    
    with st.expander("🏛️ 2. Tochterunternehmen & Konzerngesellschaften", expanded=False):
        st.markdown("""
        Das Geschäftspartnerunternehmen ist:
        - Ein **Tochterunternehmen, bei dem Porsche zu mehr als 50% beteiligt ist**, ODER
        - Eine **Konzerngesellschaft der Volkswagen Gruppe**
        """)
    
    with st.expander("☁️ 3. Externe Infrastruktur", expanded=False):
        st.markdown("""
        Der Geschäftspartner speichert oder verarbeitet **Porsche-Informationen NICHT** auf:
        - Seiner eigenen Infrastruktur
        - Seinem eigenen Standort
        
        *Beispiel: Reine Service-Provider, die keine Daten lagern*
        """)
    
    with st.expander("📦 PM-Lieferanten (Risikobewertung)", expanded=False):
        st.markdown("""
        Für **PM (Produktionsmaterial) klassifizierte Lieferanten** ist keine Risikobewertung notwendig.
        
        ⚠️ **ABER:** Auch bei PM-Lieferanten muss das TISAX-Prüfziel für **"High Availability"** eingefordert werden.
        """)

# TAB 2: Information Security
with tab2:
    st.subheader("Informationssicherheit")
    st.markdown("**Wählen Sie für alle drei Bereiche jeweils eine Option aus:**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**2.1 Vertraulichkeit** *")
        vertraulichkeit = st.selectbox(
            "Vertraulichkeit",
            ["Off", "Öffentlich", "Intern", "Vertraulich - Hoher Schutzbedarf", "Geheim - Sehr hoher Schutzbedarf"],
            label_visibility="collapsed",
            key="vertraulichkeit"
        )
        st.session_state.assessment.data["vertraulichkeit"] = vertraulichkeit
        
        with st.expander("ℹ️ Was ist Vertraulichkeit?"):
            st.markdown("""
            **Definition:** Sicherstellung der ausschließlich berechtigten Nutzung von Informationen und dabei insbesondere die Verhinderung von unberechtigter Veröffentlichung von Informationen.
            
            **Beispiele:**
            - 🟢 **Öffentlich:** Pressemeldungen, Produktkataloge für Kunden
            - 🟡 **Intern:** Geschäftliche Kommunikationsdaten (Telefonnummern, E-Mail-Adressen), betriebliche Vorgaben zum Arbeitsschutz, Arbeitsordnung
            - 🟠 **Vertraulich:** Personenbezogene Daten über dienstliche Kommunikation (z.B. Gehaltsdaten), Budgetplanungen, Revisionsberichte
            - 🔴 **Geheim:** Besondere Arten personenbezogener Daten (z.B. Gesundheitsdaten), Cycle Pläne, strategische Unternehmenspläne, Entwurfszeichnungen von Prototypen
            """)
    
    with col2:
        st.markdown("**2.2 Integrität** *")
        integritat = st.selectbox(
            "Integrität",
            ["Off", "Kein Schutzbedarf", "Normaler Schutzbedarf", "Hoher Schutzbedarf", "Sehr hoher Schutzbedarf"],
            label_visibility="collapsed",
            key="integritat"
        )
        st.session_state.assessment.data["integritat"] = integritat
        
        with st.expander("ℹ️ Was ist Integrität?"):
            st.markdown("""
            **Definition:** Sicherstellung, dass Informationen nicht unbeabsichtigt oder unberechtigt verändert werden.
            
            **Beispiele:**
            - 🟢 **Kein Schutzbedarf:** (Keine spezifischen Beispiele)
            - 🟡 **Normaler Schutzbedarf:** Standortpläne, Organigramme, einzelne interne Telefonnummern
            - 🟠 **Hoher Schutzbedarf:** JIT-Aufträge, Pressemeldungen, Inhalte des Internetauftritts, Produktionssteuerungsdaten
            - 🔴 **Sehr hoher Schutzbedarf:** Bilanzierung (z.B. Jahresabschluss), Patente, kryptographische Schlüssel, Gehaltsabrechnungen
            """)
    
    with col3:
        st.markdown("**2.3 Verfügbarkeit** *")
        verfugbarkeit = st.selectbox(
            "Verfügbarkeit",
            ["Off", "Kein Schutzbedarf", "Normaler Schutzbedarf", "Hoher Schutzbedarf", "Sehr hoher Schutzbedarf"],
            label_visibility="collapsed",
            key="verfugbarkeit"
        )
        st.session_state.assessment.data["verfugbarkeit"] = verfugbarkeit
        
        with st.expander("ℹ️ Was ist Verfügbarkeit?"):
            st.markdown("""
            **Definition:** Sicherstellung, dass die Verfügbarkeit von Informationen nicht aufgrund von unerwünschten Handlungen oder Ereignissen beeinträchtigt wird.
            
            **Beispiele:**
            - 🟢 **Kein Schutzbedarf:** Intranet-Anwendung mit allgemeinen Mitarbeiterinformationen
            - 🟡 **Normaler Schutzbedarf:** Bewerberportal
            - 🟠 **Hoher Schutzbedarf:** Gehaltsabrechnung, Buchhaltung
            - 🔴 **Sehr hoher Schutzbedarf:** IT-Systeme, deren Ausfall einen unmittelbaren Produktionsstopp zur Folge hat
            """)

# TAB 3: Data Protection
with tab3:
    st.subheader("Datenschutz")
    st.markdown("**Wählen Sie für beide Fragen jeweils Ja oder Nein:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**3.1 Personenbezogene Daten** *")
        st.markdown("Erhebt oder verarbeitet der Dienstleister personenbezogene Daten im Auftrag?")
        pd = st.selectbox(
            "Personenbezogene Daten",
            ["Off", "Ja", "Nein"],
            label_visibility="collapsed",
            key="personenbezogene_daten"
        )
        st.session_state.assessment.data["personenbezogene_daten"] = pd
    
    with col2:
        st.markdown("**3.2 Besondere Kategorien** *")
        st.markdown("Erhebt/verarbeitet der Dienstleister besondere Kategorien von Daten?")
        bkpd = st.selectbox(
            "Besondere Kategorien",
            ["Off", "Ja", "Nein"],
            label_visibility="collapsed",
            key="besondere_kategorien"
        )
        st.session_state.assessment.data["besondere_kategorien"] = bkpd

# TAB 4: Prototype Protection
with tab4:
    st.subheader("Prototypenschutz")
    st.markdown("**Wählen Sie für alle vier Fragen jeweils Ja oder Nein:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**4.1 Prototypen-Bauteile** *")
        bauteile = st.selectbox(
            "Bauteile",
            ["Off", "Ja", "Nein"],
            label_visibility="collapsed",
            key="bauteile"
        )
        st.session_state.assessment.data["bauteile"] = bauteile
        
        st.markdown("**4.3 Erprobungsfahrzeuge** *")
        erprobung = st.selectbox(
            "Erprobung",
            ["Off", "Ja", "Nein"],
            label_visibility="collapsed",
            key="erprobung"
        )
        st.session_state.assessment.data["erprobung"] = erprobung
    
    with col2:
        st.markdown("**4.2 Prototypenfahrzeuge** *")
        fahrzeuge = st.selectbox(
            "Fahrzeuge",
            ["Off", "Ja", "Nein"],
            label_visibility="collapsed",
            key="fahrzeuge"
        )
        st.session_state.assessment.data["fahrzeuge"] = fahrzeuge
        
        st.markdown("**4.4 Prototypen bei Events** *")
        events = st.selectbox(
            "Events/Shootings",
            ["Off", "Ja", "Nein"],
            label_visibility="collapsed",
            key="events"
        )
        st.session_state.assessment.data["events"] = events

# TAB 5: Results
with tab5:
    st.subheader("Bewertungsergebnis")
    
    # Check mandatory fields first
    mandatory_fields_filled = (
        st.session_state.assessment.data.get("kontaktperson", "").strip() != "" and
        st.session_state.assessment.data.get("abteilung", "").strip() != ""
    )
    
    if not mandatory_fields_filled:
        st.error(
            "❌ **Pflichtfelder erforderlich:** Bitte füllen Sie Kontaktperson und Abteilung aus (markiert mit *)."
        )
    
    # Check mandatory tabs
    mandatory_tabs_filled = (
        st.session_state.assessment.data.get("vertraulichkeit") != "Off" and
        st.session_state.assessment.data.get("integritat") != "Off" and
        st.session_state.assessment.data.get("verfugbarkeit") != "Off" and
        st.session_state.assessment.data.get("personenbezogene_daten") != "Off" and
        st.session_state.assessment.data.get("besondere_kategorien") != "Off" and
        st.session_state.assessment.data.get("bauteile") != "Off" and
        st.session_state.assessment.data.get("fahrzeuge") != "Off" and
        st.session_state.assessment.data.get("erprobung") != "Off" and
        st.session_state.assessment.data.get("events") != "Off"
    )
    
    # Run assessment
    result = st.session_state.assessment.assess()
    
    # Check if form is complete
    if not mandatory_fields_filled:
        st.info("⏳ Warten auf Pflichtfelder (Tab 1)...")
    elif not mandatory_tabs_filled:
        st.error(
            "❌ **Alle Tabs müssen vollständig ausgefüllt sein:** "
            "Bitte wählen Sie in den Tabs 🔐 Informationssicherheit*, 📊 Datenschutz* und 🏭 Prototypenschutz* "
            "jeweils eine Option aus (mit * markiert)."
        )
    elif not result["form_complete"]:
        st.warning(
            "⚠️ **Bewertung konnte nicht durchgeführt werden.**"
        )
    elif result["tisax_required"] is None:
        st.info("Bewertung wird berechnet...")
    else:
        # Display result
        if result["tisax_required"]:
            st.markdown(f"""
            <div class="result-box result-yes">
                <div class="result-title">✅ TISAX erforderlich: JA</div>
                <div class="al-box">
                    <strong>Assessment-Level:</strong> {result["assessment_level"]}<br>
                    <strong>Schutzbedarf:</strong> Digital
                </div>
                <div class="result-text">
                    {result["result_text"].replace(chr(10), '<br>')}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Display required labels
            if result["required_labels"]:
                st.markdown("### 📌 Erforderliche TISAX Labels:")
                labels_text = "<br>".join([f"• {label}" for label in result["required_labels"]])
                st.markdown(f"""
                <div class="info-box">
                    {labels_text}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-box result-no">
                <div class="result-title">❌ TISAX erforderlich: NEIN</div>
                <div class="result-text">
                    {result["result_text"]}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # PDF Export Button
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            if st.button("📥 Export als PDF", use_container_width=True, disabled=not (mandatory_fields_filled and mandatory_tabs_filled)):
                exporter = TISAXPDFExporter()
                pdf_data = exporter.generate_pdf(
                    st.session_state.assessment.data,
                    result
                )
                st.download_button(
                    label="📄 PDF herunterladen",
                    data=pdf_data,
                    file_name=f"TISAX_Bewertung_{st.session_state.assessment.data['unternehmensname']}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        with col2:
            if st.button("🔄 Formular zurücksetzen", use_container_width=True):
                st.session_state.assessment.reset()
                st.rerun()

# Footer
st.markdown("---")
st.caption("Porsche AG - TISAX Risikobewertung | Interne Nutzung")
