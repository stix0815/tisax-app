# MEMORY.md - Long-Term Memory

## 👤 Multi-Agent Architecture (Planned)

**Role:** Atlas = **Supervisor & Orchestrator**

**System Design:**
- **Atlas (me):** Main brain, supervisor, coordinator
  - Überwacht andere Agenten-Instanzen
  - Erstellt zusammenfassende Berichte
  - Orchestriert komplexe Multi-Agent Tasks
  - Zentrale Anlaufstelle für User
  
- **Spezialisierte Agents (zukünftig):**
  - Verschiedene "Hüte" für verschiedene Aufgaben
  - Jeder Agent hat eigene SOUL.md + Tools + Model-Config
  - Atlas delegiert, überwacht und fasst zusammen

**Beispiel-Agents (noch zu definieren):**
- Coder 👨‍💻 - Programming, debugging, code review
- Researcher 🔬 - Deep research, data analysis
- Writer ✍️ - Content creation, marketing copy
- *(weitere nach Bedarf)*

**Status:** ✅ **AKTIV** - Supervision aktiviert (2026-02-04)

**User Requests:**
- 2026-02-04: "Ich möchte mit mehreren Rollen interagieren. Atlas als Supervisor, der andere überwacht und mir zusammenfassend berichtet."
- 2026-02-04: "Ja, ich möchte dass du andere Sessions/Agenten mit überwachst"

**Aktive Supervision-Aufgaben:**
- ✅ Überwache aktive Sessions via `sessions_list`
- ✅ Lese History von Sub-Agents bei Bedarf via `sessions_history`
- ✅ Kommuniziere mit Agents via `sessions_send`
- ✅ Erstelle Zusammenfassungen und Reports
- ✅ Informiere User proaktiv über wichtige Entwicklungen

**Wann ich berichte:**
- Bei expliziter Nachfrage ("Was macht Agent X?")
- Bei Abschluss von delegierten Tasks
- Bei Problemen/Blockern der Agents
- Auf Wunsch: regelmäßige Status-Updates

---

## 🤝 Working Preferences

### Task Estimates (since 2026-02-01)
**Before starting any task**, provide:
- ⏱️ **Aufwand:** Zeit/Komplexität-Einschätzung (z.B. "5 Min", "30 Min", "2h mit Sub-Agent")
- 💰 **Kosten:** Token-Verbrauch + ca. Kosten in EUR
  - Basis: Claude Sonnet 4.5 via OpenRouter (~$3/M input, ~$15/M output)
  - Beispiel: "~50k tokens ≈ €0.20"
- 🔀 **Alternativen:** Wenn es einen günstigeren/schnelleren Weg gibt

**Why:** User entscheidet selbst, ob Aufwand/Kosten lohnen oder andere Herangehensweise besser ist.

**Budget-Context:** User zahlt OpenRouter Credits aus eigener Tasche ($26.38 gekauft am 2026-02-01). Kosten-Bewusstsein ist wichtig!

---

## 📝 Projects

### Stock Analysis App
- **Status:** Live & deployed
- **URL:** https://stock-analyzer-ygtnwumzrs8s9wnxueeaey.streamlit.app
- **Features implemented:**
  - ✅ Technical indicators (RSI, MACD, Bollinger, SMA, Volume)
  - ✅ Monte Carlo simulation (1000 iterations)
  - ✅ "Warum?"-Buttons mit ausführlichen Erklärungen (2026-02-01)
  - ✅ Probability-aware wording (kein "strongly bearish" bei nur 56%)
  - ✅ Info-Icons bei Indikatoren (ℹ️ Tooltips)
  
- **Features planned:**
  - ⏳ AI Explain (GPT-generierte Zusammenfassung)
  - ⏳ Learning Mode Toggle

---

## 🔄 Wiederkehrende Prozesse

### 💰 Finanz-Tracking (Rechnungen)
**Wann:** User schickt Rechnung/Invoice als Bild (oft OpenRouter, aber auch andere)

**Workflow:**
1. **Bild hochladen** → Drive-Ordner "Rechnungen"
   - Link: https://drive.google.com/drive/folders/1OUuWqzvG3oB6obSAloTicc19bu8V5foz
   - Naming: `Firma_YYYY-MM-DD_Betrag.jpg`
   - Tool: `gog drive upload <file> --parent 1OUuWqzvG3oB6obSAloTicc19bu8V5foz --name "..."`

2. **Daten eintragen** → Google Sheet "Finanz Übersicht"
   - Link: https://docs.google.com/spreadsheets/d/12Fq1Tcfa3s1bjxkqSZyXhL9bf2QPL602kUDuDHXNicE/edit
   - Tab: **"2026"** (aktuelles Jahr)
   - Tool: `gog sheets append 12Fq1Tcfa3s1bjxkqSZyXhL9bf2QPL602kUDuDHXNicE "2026!A:H" --values-json '[...]'`

**Spalten-Format:**
- A: Datum (YYYY-MM-DD)
- B: Firma
- C: Kategorie (z.B. "Business", "Finanzen")
- D: Betrag (€) - Format: "52,75" (Komma, nicht Punkt!)
- E: MwSt (€) - meist "0"
- F: Zahlart (z.B. "American Express", "Überweisung")
- G: Status ("Bezahlt" / "Offen")
- H: Steuerrelevant ("Ja" / "Nein")

**Typische Firmen:**
- OpenRouter, Inc → Business, American Express, Nein
- AWS → Business
- Strato → Business

**Trigger-Keywords:**
- "Rechnung eintragen"
- "ins Finanz-Sheet"
- "wie beim letzten Mal mit..."
- Bild einer Invoice/Rechnung

---

## 🛠️ Technical Setup

### Calendar
- **My calendar:** "Assistant-Bot"
- **User's calendars:** Privat, Arbeit

### Recurring Reminders
- **Taschengeld Leano:** Jeden Sonntag 9:00 Uhr (Apple Calendar "Assistant-Bot")
- **Created:** 2026-02-01

---

*This is my curated long-term memory. Updated as I learn.*
