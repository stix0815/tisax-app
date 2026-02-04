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

**Status:** Konzept definiert, Umsetzung folgt bei Bedarf

**User Request (2026-02-04):** "Ich möchte mit mehreren Rollen interagieren. Atlas als Supervisor, der andere überwacht und mir zusammenfassend berichtet."

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
  
- **Features planned:**
  - ⏳ Info-Icons bei Indikatoren (ℹ️ Tooltips)
  - ⏳ AI Explain (GPT-generierte Zusammenfassung)
  - ⏳ Learning Mode Toggle

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
