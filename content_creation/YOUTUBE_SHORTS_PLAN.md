# YouTube Shorts / Instagram Reels - Finance Education

**Format:** AI-generiert, minimalistisch  
**Nische:** Finance Education (Geld, Investieren, Sparen)  
**Zielgruppe:** 18-35 Jahre, DACH-Raum  
**Frequenz:** 3-5 Shorts/Woche (zum Start)

---

## 🎬 Production Workflow

### **Step 1: Skript schreiben** (30-60 Sek)
- Hook (3 Sek): Aufmerksamkeit grabben
- Value (40 Sek): Hauptinhalt
- CTA (5-10 Sek): Like, Follow, Comment

**Beispiel:**
```
[0-3s] Hook: "90% machen diesen Fehler beim Sparen!"
[3-45s] Value: "Sparst du auf Girokonto? Du verlierst 
               Geld durch Inflation. 2% Inflation = 
               -2.000€ pro Jahr bei 100k. Besser: 
               Tagesgeld (3.5%) oder ETFs (7%+ langfristig)."
[45-60s] CTA: "Speichere das! Follow für mehr Geld-Hacks!"
```

---

### **Step 2: Text-to-Speech** 🎙️

**Tools:**
- **ElevenLabs** (~$5/Monat) - Beste Qualität, natürliche Stimmen
- **Murf.ai** (~$10/Monat) - Sehr gut, Deutsche Stimmen
- **Free:** Google TTS (OK, aber robotisch)

**Meine Empfehlung:** ElevenLabs (klingt wie echter Mensch!)

**Workflow:**
```bash
# Skript → Audio
elevenlabs generate --text "Dein Skript" --voice "German-Professional" --output audio.mp3
```

---

### **Step 3: Video erstellen** 🎥

**Option A: Stock Footage + Text Overlays** (empfohlen!)

**Tools:**
- **CapCut** (kostenlos!) - Best für Shorts/Reels
- **Canva** (~$13/Monat) - Templates + Stock Videos
- **Remotion** (Code-based, PRO-Level)

**Assets:**
- **Pexels** (kostenlos) - Stock Videos
- **Unsplash** (kostenlos) - Bilder
- **Canva Stock** - Animierte Grafiken

**Style:**
```
[Shot 1] Hook → Attention-grabbing visual
  - Text Overlay: Große, fette Schrift
  - Stock Video: Geld, Charts, Lifestyle

[Shot 2-4] Value → Infographics
  - Animated numbers
  - Simple charts
  - Text bullets

[Shot 5] CTA → Call-to-Action
  - "Folge für mehr!" mit Arrow
  - Stock Video: Success/Growth imagery
```

---

### **Option B: Automated with Code** (MEIN VORSCHLAG!)

**Stack:**
- **Remotion** (React-based video rendering)
- **Tailwind CSS** (Styling)
- **Chart.js** (für Grafiken)

**Ich kann dir ein Template bauen:**
```javascript
// Script Input:
const script = {
  hook: "90% machen diesen Fehler beim Sparen!",
  value: "Inflation frisst dein Geld...",
  cta: "Follow für mehr Geld-Hacks!"
}

// Auto-generates:
- TTS Audio
- Synced captions
- Animated charts
- Video export (MP4)
```

**Vorteil:** 1 Command → fertiges Video!

---

## 🎨 Visual Style Guide

**Minimalistisch = Clean & Simple:**

**Color Palette:**
- Background: Schwarz oder dunkelgrau (#1a1a1a)
- Text: Weiß (#ffffff)
- Accent: Neon-Grün oder Gold (#00ff88 oder #ffd700)
- Charts: Gradient (Grün für positiv, Rot für negativ)

**Typography:**
- Font: **Montserrat Bold** oder **Inter Bold**
- Size: GROSS (80-120px für Hook)
- Animation: Fade-in, Slide-in (smooth!)

**Layout:**
- Centered text
- Simple icons/emojis
- Clean transitions
- NO clutter

**Inspiration:**
- Suche: "financial minimalist shorts"
- Accounts: @financialtortoise, @humphrey (Instagram)

---

## 💡 Content-Ideen (Finance)

### **Serie 1: "Geld-Fehler die du vermeiden musst"**
1. "Girokonto als Sparbuch" ❌
2. "Aktien verkaufen bei -10%" ❌
3. "Keine Notfall-Reserve haben" ❌
4. "Versicherungen überzahlen" ❌
5. "Kredit für Konsum nutzen" ❌

### **Serie 2: "So baust du Vermögen auf"**
1. "50/30/20 Regel erklärt"
2. "ETF Sparplan für Anfänger"
3. "Zinseszins-Effekt visualisiert"
4. "100€/Monat → 100k in 20 Jahren"
5. "Diversifikation einfach erklärt"

### **Serie 3: "Geld-Hacks"**
1. "Cashback richtig nutzen (Amex)"
2. "Steuern sparen mit ETFs"
3. "Wie Reiche ihr Geld parken"
4. "Inflation schlagen - 3 Wege"
5. "Passives Einkommen Ideen"

### **Serie 4: "Zahlen die schockieren"**
1. "100k auf Girokonto = -30k in 15 Jahren"
2. "Durchschnitts-Rente in DE: 1.543€"
3. "7% Rendite = Geld verdoppelt in 10 Jahren"
4. "40% der Deutschen haben kein Vermögen"
5. "S&P 500: +10% pro Jahr seit 1980"

---

## 🤖 Automation-Tool Stack

**Ich kann dir bauen:**

### **1. Content Generator Script**
```bash
python generate_short.py --topic "ETF Sparplan" --duration 60

→ Output:
  - script.txt (mit Hook/Value/CTA)
  - audio.mp3 (TTS)
  - captions.srt (Untertitel)
  - video.mp4 (fertiges Short!)
  - caption.txt (Instagram/YouTube Description)
  - hashtags.txt (SEO-optimiert)
```

### **2. Batch-Production**
```bash
# Erstelle 10 Shorts auf einmal
python batch_generate.py --topics topics.csv --count 10

→ 10 fertige Videos in 10 Minuten
```

### **3. Posting Automation** (optional)
- Auto-upload zu YouTube/Instagram
- Scheduled posts
- Cross-posting (beide Plattformen gleichzeitig)

---

## 📅 Content-Kalender (Beispiel-Woche)

**Montag:** Geld-Fehler (Viral-Potential!)  
**Mittwoch:** Geld-Hack (Actionable!)  
**Freitag:** Shocking Stat (Engagement!)  
**Sonntag:** Educational Deep-Dive (Value!)

**Strategie:**
- 2x "Viral Hooks" (Fehler, Schock-Zahlen)
- 2x "Value-Content" (How-To, Hacks)

---

## 🚀 Next Steps (wenn du willst)

**Phase 1: Setup** (30 Min)
- Ich baue dir das Content Generator Tool
- ElevenLabs Account setup (oder Free TTS)
- Template für Remotion Videos

**Phase 2: First Batch** (1 Stunde)
- Ich generiere 10 Skripte
- Rendere 5 Test-Videos
- Du schaust ob Style passt

**Phase 3: Launch** (1 Tag)
- YouTube Shorts Channel erstellen
- Instagram Creator Account
- Erste 5 Videos posten
- Strategie verfeinern

---

**Soll ich anfangen oder erstmal pausieren?** 

Wenn pausieren → ich merke mir:
- ✅ AI-generiert, minimalistisch
- ✅ Finance-Fokus
- ✅ Neu starten
- 📋 Reasoning/Erklärungen später einbauen

Sag Bescheid! 🎬