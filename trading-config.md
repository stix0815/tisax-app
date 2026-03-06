# Trading Bot Config - Noam

**Erstellt:** 2026-01-30

## 1. Asset-Kategorien

### Daytrading Aktien
- **Trading Volume:** > 10 Mio pro Tag
- **Float:** < 15 Mio
- **Fokus:** Kurzfristige Bewegungen

### Dividenden-Aktien (Invest)
- **KGV:** < 20
- **Keine Penny Stocks**
- **Etablierte Aktien** mit langjähriger guter Performance

### Krypto
- **Nur Bitcoin** (BTC)

## 2. Alerts
- **Trigger:** Starke Preisbewegungen (Anstieg/Fall) innerhalb der letzten Minuten
- **Asset-Typ:** Daytrading-Aktien

## 3. Timeframe
- **1-5 Minuten Batch** für Daytrading

## 4. Datenquellen
- **Nasdaq** (Aktien)
- **Binance** (Krypto)
- **Yahoo Finance** (Ergänzung)

## 5. Notification Channel
- **Telegram** (aktueller Chat)

## 6. Execution Mode
- **Nur Alerts** - keine automatischen Orders
- Manuelle Entscheidung durch User

## 7. Logging & Backtesting
- **Ja** - Alle Trades und Alerts loggen
- Backtesting-Daten sammeln

## 8. Deployment
- **Lokal auf dem Mac** laufen lassen
- Dauerhaft im Hintergrund

---

## Nächste Schritte
1. API-Keys einrichten (Nasdaq/Binance/Yahoo)
2. Scanner implementieren
3. Alert-Logic programmieren
4. Telegram-Notifications integrieren
5. Logging-System aufsetzen
6. Testing & Deployment
