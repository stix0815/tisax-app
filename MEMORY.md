# MEMORY.md - Long-Term Memory

## 🤝 Working Preferences

### Task Estimates (since 2026-02-01)
**Before starting any task**, provide:
- ⏱️ **Aufwand:** Zeit/Komplexität-Einschätzung (z.B. "5 Min", "30 Min", "2h mit Sub-Agent")
- 💰 **Kosten:** Token-Verbrauch + ca. Kosten in EUR
  - Basis: Claude Sonnet 4.5 via OpenRouter (~$3/M input, ~$15/M output)
  - Beispiel: "~50k tokens ≈ €0.20"
- 🔀 **Alternativen:** Wenn es einen günstigeren/schnelleren Weg gibt

**Why:** User entscheidet selbst, ob Aufwand/Kosten lohnen oder andere Herangehensweise besser ist.

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
- **My calendar:** "Assistant-Bot" (Apple Calendar via AppleScript)
- **User's calendars:** Privat, Arbeit
- **Method:** `osascript` (not `gog`)

### Recurring Reminders
- **Taschengeld Leano:** Jeden Sonntag 9:00 Uhr (Apple Calendar "Assistant-Bot")
- **Created:** 2026-02-01

---

*This is my curated long-term memory. Updated as I learn.*
