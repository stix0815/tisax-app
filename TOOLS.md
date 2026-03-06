# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## 📅 Calendar

**Apple Calendar (via AppleScript)**
- **My calendar:** `Assistant-Bot`
- **Method:** Use `osascript` for calendar entries (not `gog`)
- **Recurring events:** Set via `recurrence` property (e.g., `"FREQ=WEEKLY;BYDAY=SU"`)

**Available calendars:**
- Privat (user's personal)
- Arbeit (work)
- Assistant-Bot (mine! ← use this)
- Geplante Erinnerungen
- Geburtstage
- Deutsche Feiertage
- Siri-Vorschläge

**Example (weekly event):**
```applescript
tell application "Calendar"
    tell calendar "Assistant-Bot"
        set newEvent to make new event with properties {summary:"Title", start date:startDate, end date:endDate}
        tell newEvent
            set recurrence to "FREQ=WEEKLY;BYDAY=SU"
        end tell
    end tell
end tell
```

---

---

## 🤖 Model Selection Rule

**Default:** Always use **Haiku** 🚀

**Switch to Sonnet ONLY when:**
- Architecture decisions
- Production code review
- Security analysis
- Complex debugging/reasoning
- Strategic multi-project decisions

**When in doubt:** Try Haiku first.

---

## ⚡ Rate Limits & Budget

**API Rate Limits:**
- 5 seconds minimum between API calls
- 10 seconds between web searches
- Max 5 searches per batch, then 2-minute break
- Batch similar work (1 request for 10 leads, not 10 separate requests)
- **If 429 error:** STOP → wait 5 minutes → retry

**Daily Budget:** $5
- ⚠️ Warning at 75% ($3.75)

**Monthly Budget:** $50
- ⚠️ Warning at 75% ($37.50)

---

Add whatever helps you do your job. This is your cheat sheet.
