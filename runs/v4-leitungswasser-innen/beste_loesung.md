# Zimmerkühlung mit Leitungswasser: drucklose Heizkörper-Kühlung aus dem Kopfbehälter

## 1. Kurzfazit

**Was bleibt:** Drei Panelheizkörper in Reihe sind der Kühler. Sie brauchen 0 W Strom.

**Was sich grundlegend ändert:** Die Heizkörper hängen nicht mehr am Netzdruck. Der Weg ist jetzt:

Hahn → Schwimmerventil mit freiem Auslauf (Luftstrecke, wie im WC-Spülkasten) → offener Kopfbehälter → Schwerkraft durch die Heizkörper → Überlauftrichter → Sammelkübel.

Das löst mehrere Probleme auf einmal:

| Problem | Lösung |
|---|---|
| Gebrauchte Heizkörper (Inhibitoren, Biofilm) an der Trinkwasserinstallation | Die Luftstrecke trennt sie vollständig vom Netz. Es spielt keine Rolle, was in den Heizkörpern war. |
| Netzdruck schwankt, Nadelventil verstopft und driftet | Der Schwimmer hält den Pegel konstant. Der Durchfluss hängt nur noch von dieser Höhe und einem voreingestellten Ventil ab. |
| Leck oder Schlauchabriss unter Netzdruck | Hinter dem Schwimmerventil liegen nur etwa 0,05–0,1 bar an. Ein Loch tropft, es spritzt nicht. |
| Heizkörper laufen über Nacht leer oder saugen sich leer | Ein Überlauftrichter mit Luftstrecke verhindert den Heber. Die Heizkörper bleiben gefüllt. |

**Ehrlichkeit bei der Leistung:** Die Wärmeübertragung der Heizkörper im Kühlbetrieb ist ungemessen. Die Normwerte stammen aus dem Heizbetrieb bei 50 K Übertemperatur. Deshalb rechne ich mit einem **Planwert (UA × 0,7)** und zeige das Modell (UA × 1,0) nur als obere Erwartung.

| Größe (Auslegung: 3 Heizkörper, 25 l/h) | Planwert, Zulauf 15 °C | Planwert, Zulauf 18 °C | Modell (UA × 1,0), 15 °C |
|---|---|---|---|
| Leistung bei 27 °C Raumluft | **211 W** | 158 W | 256 W |
| Mittel 9–19 Uhr | **204 W** | 153 W | 243 W |
| Kälte pro Tag (10 h) | **2,04 kWh** | 1,53 kWh | 2,43 kWh |
| Wasser pro Tag | 250 l | 250 l | 250 l |
| Liter pro kWh (Tagesmittel) | 123 | 163 | 103 |
| Wasserkosten brutto (4,5 €/m³) | 1,13 €/Tag, 0,55 €/kWh | 1,13 €/Tag, 0,74 €/kWh | 0,46 €/kWh |
| Spitze 19 Uhr, nur Gerät (ohne Gerät 30,4 °C) | 28,5 °C | 28,9 °C | 28,1 °C |
| Spitze 19 Uhr, Gerät + Außenverschattung (ohne Gerät 28,1 °C) | **26,3 °C** | 26,7 °C | 26,0 °C |

Die Zulauftemperatur ist hier die am Heizkörper-Eintritt. Sie liegt wegen Schlauch und Kopfbehälter etwa 0,5–1 K über der am Hahn.

**Rangfolge der Maßnahmen:**
1. **Nachtlüftung** ist gratis und bestimmt die Starttemperatur. 1 K tieferer Start ergibt etwa 0,7 K weniger um 19 Uhr.
2. **Außenverschattung** (Markise, Außenjalousie, Hitzeschutzplane) bringt −2,3 K an der Spitze und ist damit so wirksam wie das Wassergerät.
3. **Wassergerät** bringt weitere etwa −1,8 bis −2,1 K.

**Das Ziel ≤ 26 °C** wird mit dem Planwert knapp verfehlt (26,3 °C). Es wird erreicht, wenn die Nachtlüftung den Start auf ≈ 24,5 °C bringt (→ 25,6 °C) oder wenn das Modell stimmt (→ 26,0 °C).

**Wirtschaftlich ist das nur eingeschränkt.** Die Kälte kostet 0,33–0,74 €/kWh, je nach Weiterverwendung des Wassers und Zulauftemperatur. Ein Klimagerät liegt bei ≈ 0,12–0,20 €/kWh. Das Gerät lohnt sich für einige Hitzetage, wenn Strom, Lärm und Abluftschlauch nicht infrage kommen, und besonders, wenn das Wasser einen Garten gießt.

**Draußen wird nichts gebaut.** Der Nachthimmel-Strahler (≈ 0,9 kWh pro klarer Nacht, ≈ 1.700 €) lohnt hier nicht.

## 2. Physik: Was steckt im Liter?

Wasser nimmt 1,163 Wh/(l·K) auf.

**Liter pro kWh = 860 / (T_aus − T_ein)**

Wie warm das Wasser austritt, hängt an der Tauscherfläche. Mehr Durchfluss bringt wenig: Die Leistung sättigt, die Liter steigen weiter.

Ich rechne mit dem ε-NTU-Verfahren. Luft und Raum sind die konstante Temperatur, UA ist der Gesamtleitwert der Heizkörper:
- ṁc = Durchfluss × 1,163.
- NTU = UA / ṁc.
- ε = 1 − e^(−NTU).
- Q = ε · ṁc · (T_Raum − T_ein).

**Annahmen für UA** (3 Heizkörper, Raum 27 °C, Zulauf 15 °C, 25 l/h):

| Annahme | UA | Q | Wasser-Austritt |
|---|---|---|---|
| Modell (Exponent 1,3 aus dem Heizbetrieb) | 38,5 W/K | 256 W | 23,8 °C |
| **Planwert (× 0,7)** | **26,9 W/K** | **211 W** | **22,2 °C** |
| Untergrenze (× 0,5) | 19,2 W/K | 169 W | 20,8 °C |

Die Wasserbilanz setzt die Obergrenze: 25 l/h × 1,163 × 12 K = 349 W.

**Durchfluss-Tabelle** (Planwert, 3 Heizkörper, Raum 27 °C, Zulauf 15 °C):

| Durchfluss | Leistung | Austritt | l/kWh |
|---|---|---|---|
| 12 l/h | 143 W | 25,3 °C | 84 |
| 15 l/h | 165 W | 24,4 °C | 91 |
| 20 l/h (Sparmodus) | 192 W | 23,2 °C | 104 |
| **25 l/h (Auslegung)** | **211 W** | **22,2 °C** | **119** |
| 30 l/h | 225 W | 21,5 °C | 133 |
| 35 l/h | 237 W | 20,8 °C | 148 |

- Von 25 auf 35 l/h bringen +40 % Wasser nur +12 % Leistung.
- Von 25 auf 20 l/h spart man 20 % Wasser und verliert 9 % Leistung.
- Ich rechne trotzdem mit 25 l/h, weil das Ziel ≤ 26 °C knapp ist.

**Stufenbetrieb bringt nichts.** Ich habe 15 l/h (9–12 Uhr) plus 30 l/h (12–19 Uhr) simuliert. Die Spitze liegt bei 28,48 °C, identisch zu konstant 25 l/h (28,48 °C), bei 255 statt 250 l. Konstanter Durchfluss ist also einfacher und gleich gut.

## 3. Wärmeübertragung ohne Strom

**Normleistung:** Ein Typ 22, 600 × 1000 mm hat 1.200 W bei ΔT 49,8 K. Mit dem Exponenten 1,3 folgt die Leistung bei kleinem ΔT:

| ΔT Raum − mittleres Wasser | 4 K | 6 K | 8 K | 10 K | 12 K |
|---|---|---|---|---|---|
| Leistung je Heizkörper | 45 W | 77 W | 111 W | 149 W | 189 W |

**Was für Natur-Konvektion spricht:**
- **Gegenstrom:** Die Luft wird am kalten Blech dichter und fällt. Das Wasser, das sich erwärmt, steigt. Kaltes Wasser liegt unten (Eintritt unten), warmes oben (Austritt oben). Die herabfallende Luft trifft auf immer kälteres Blech, das ist günstiges Gegenstromverhalten.
- **Stromlos ist wirklich stromlos:** 0 W.

**Was dagegen spricht und warum ich 0,7 ansetze:**
- Der Exponent gilt im Heizbetrieb bei ΔT ≈ 50 K. Hier liegt ΔT bei 3–10 K.
- Die Schichtung im Wasser ist ungemessen. Bei 25 l/h strömt das Wasser sehr langsam durch große Querschnitte, und der Wasserweg könnte sich kurzschließen.
- **Nachmessen nach dem Aufbau:** Q = 1,163 × Durchfluss [l/h] × (T_aus − T_ein). Beispiel: 25 × 1,163 × 7 K = 204 W.
  - Liegt das Ergebnis unter ≈ 170 W, ist der Aufbau schlechter als der Planwert.
  - Liegt es über ≈ 240 W, ist das Modell bestätigt.

**Strahlungswirkung:** Die kühlen Flächen (17–23 °C, 1,8 m² Front) senken die gefühlte Temperatur vermutlich um 0,3–0,5 K. Das ist nicht eingerechnet.

**Optional, mit Strom: Lüfter.** Zwei 120-mm-PC-Lüfter, gedrosselt auf ≈ 1 W je Stück (Netzteil ≈ 2 W), blasen Luft an die Heizkörper. Das ist eine Schätzung, nicht gemessen:
- UA steigt um etwa 25 %, die Leistung um etwa 15 %.
- Das Wasser tritt wärmer aus, ohne dass mehr Liter nötig sind.
- Die Spitze sinkt um etwa 0,2 K. Kosten ≈ 20 €.
- Das lohnt nur, wenn die letzten 0,2 K zählen.

## 4. Kondensation und Entfeuchtung

**Taupunkte:**
- 27 °C / 50 % r. F.: ≈ 15,8 °C.
- 28 °C / 50 %: 16,6 °C.
- 28 °C / 65 % (schwül): ≈ 20,8 °C.

Die Blechoberfläche liegt etwa 0,3 K über der Wassertemperatur. Wasser mit 15 °C ist also unter dem Taupunkt der Raumluft.

**Latente Leistung** rechne ich über den Stoffübergang (Lewis-Zahl 1). Gesamtleistung = sensibel + latent, abgeschlossen über die Wasserbilanz, mit jeweils neu berechneter Austrittstemperatur (Planwert, 25 l/h):

| Fall | nasse Fläche | Gesamt | sensibel | latent | Kondensat | Austritt | zum Vergleich trocken |
|---|---|---|---|---|---|---|---|
| 27 °C/50 %, Zulauf 15 °C (Auslegung) | nur Eintrittsecke von HK 1 | 211 W | ≈ 210 W | < 1 W | ≈ 0–2 g/h | 22,2 °C | 211 W |
| 28 °C/50 %, Zulauf 15 °C | untere ⅓ von HK 1 | ≈ 232 W | ≈ 228 W | ≈ 4 W | ≈ 6 g/h | 23,0 °C | 228 W |
| 28 °C/50 %, Zulauf 12 °C | HK 1 ganz | **≈ 292 W** | ≈ 268 W | ≈ 24 W | ≈ 35 g/h (≈ 0,35 l/Tag) | 22,1 °C | 280 W, 21,6 °C |
| 28 °C/65 % (schwül), Zulauf 15 °C | HK 1 ganz, Anfang HK 2 | **≈ 254 W** | ≈ 196 W | ≈ 58 W | ≈ 85 g/h (≈ 0,85 l/Tag) | 23,7 °C | 228 W, 22,8 °C |

**Einordnung:**
- Latente Leistung kommt nicht obendrauf. Sie kann nur zusätzlich fließen, wenn das Wasser wärmer austritt. Das ist in der Tabelle so gerechnet, die 331 W der Vorversion bei 12 °C waren dagegen doppelt gezählt.
- Bei Schwüle verschiebt Kondensation Leistung von sensibel nach latent. Die **Lufttemperatur sinkt dadurch weniger** (196 statt 228 W sensibel), die **Luft wird trockener**: 85 g/h entsprechen etwa der Feuchteabgabe einer Person. Das ist ein Komfortgewinn, kein Temperaturgewinn, und in der Temperaturbilanz setze ich ihn nicht an.
- Die Auslegung (27 °C, 50 %) ist praktisch trocken.

**Wohin mit dem Kondensat:**
- Eine flache Wanne (z. B. 100 × 30 × 3 cm, ≈ 9 l) steht unter HK 1 und HK 2.
- Zulaufschlauch, Dosierventil und Kopfbehälter haben ≈ 15 °C und beschlagen in schwüler Luft. Sie bekommen 13–19 mm geschlossenzellige Dämmung.
- Verbindungsschläuche zwischen den Heizkörpern haben ≥ 18 °C und sind meist unkritisch.

## 5. Wärmelast und Raumtemperatur

**Annahmen** (alle geschätzt):
- Zimmer 20 m² × 2,5 m, mittleres Geschoss, 2 m² Südwest-Fenster mit Innenvorhang.
- Speichermasse C = 1,0 kWh/K (mittelschwer).
- Hülle und Fugen G = 17,6 W/K gegen T_Außen + 1,5 K.
- Person, Laptop, Licht: 110 W (nur sensible Last).
- Außentemperatur stündlich 9–19 Uhr: 25 / 26,5 / 28 / 29 / 30 / 30 / 30 / 30 / 29,5 / 28,5 °C.
- Sonne durch das Fenster in W, stündlich ab 9 Uhr: 150, 200, 250, 300, 350, 400, 450, 450, 420, 330.
- Start 25,5 °C nach Nachtlüftung.
- Außenverschattung −75 % Sonne.
- Gerät läuft 9–19 Uhr (Planwert, 25 l/h, Zulauf 15 °C), Q = 17,55 W/K × (T_Raum − 15 °C).

**Modell:** C · dT/dt = Sonne + 110 W + G · (T_Außen + 1,5 K − T) − Q_Gerät. Ich rechne in 1-h-Schritten, Genauigkeit ±0,1 K.

| Uhr | nichts | nur Gerät (Plan) | nur Außenverschattung | Außen + Gerät (Plan) |
|---|---|---|---|---|
| 9 | 25,5 | 25,5 | 25,5 | 25,5 |
| 11 | 26,1 | 25,8 | 25,9 | 25,5 |
| 13 | 27,0 | 26,3 | 26,4 | 25,7 |
| 15 | 28,2 | 27,0 | 26,9 | 25,9 |
| 17 | 29,4 | 27,9 | 27,6 | 26,1 |
| 19 | **30,4** | **28,5** | **28,1** | **26,3** |

- **Gerät allein:** Es führt 2,04 kWh pro Tag ab. Im 24-h-Mittel sind das 85 W, in der Betriebszeit im Mittel 204 W.
- **Mittlere Raumtemperatur 9–19 Uhr:** 27,7 °C ohne Gerät, 26,8 °C mit Gerät, also −0,9 K.

### Empfindlichkeit Startwert (Nachtlüftung)

| Start 9 Uhr | nichts | nur Gerät | Außen + Gerät | Außen + Gerät + Lüfter |
|---|---|---|---|---|
| 24,5 °C | 29,5 | 27,8 | **25,6** | 25,4 |
| 25,5 °C | 30,4 | 28,5 | 26,3 | 26,1 |
| 26,5 °C | 31,2 | 29,2 | 27,0 | 26,8 |

Die Nachtlüftung ist der größte Einzelhebel. Die Anfangstemperatur klingt mit etwa 70 % über 10 h ab.

### Laufzeit und Nachtbetrieb

- **Start um 12 statt 9 Uhr:** spart 75 l (−30 %), Spitze 28,9 statt 28,5 °C (**+0,4 K**). Start um 11 Uhr ergibt ≈ 28,8 °C. Die frühere Angabe +0,8 K war zu hoch.
- **Nachts oder früh morgens laufen lassen:** Das ist etwa halb so wirksam pro Liter:
  - Bei 24 °C Raum nimmt 1 l nur ≈ 6,3 Wh auf, bei 28,5 °C etwa 9,5 Wh.
  - Die Kälte klingt bis 19 Uhr zusätzlich ab.
  - Nachts lohnt es nur, wenn Fenster nicht offen bleiben dürfen.
- **Kältestes Leitungswasser:** Es gibt keinen verlässlichen Vorteil für bestimmte Uhrzeiten. Steigleitungen stehen morgens oft warm. Deshalb morgens erst ≈ 2–3 l ablaufen lassen, bis das Wasser kühl ist, und die Temperatur messen.

### Empfindlichkeit Zulauftemperatur

(Planwert, 25 l/h, Raum 27 °C, Zulauf = Heizkörper-Eintritt)

| Zulauf | Leistung | Austritt | l/kWh | Spitze, nur Gerät | Spitze, Außen + Gerät |
|---|---|---|---|---|---|
| 12 °C | 263 W (+ ≈ 10 W latent) | 21,0 °C | 95 | ≈ 28,1 | ≈ 25,9 |
| **15 °C** | **211 W** | 22,2 °C | 119 | 28,5 | 26,3 |
| 18 °C | 158 W | 23,4 °C | 158 | 28,9 | 26,7 |
| 20 °C | 123 W | 24,2 °C | 203 | ≈ 29,2 | ≈ 27,0 |

- Bis 18 °C lohnt der Betrieb noch. Ab 20 °C bringt er zu wenig.
- **Vorher messen:** Wasser am vorgesehenen Hahn morgens und nachmittags 5 min laufen lassen und die Temperatur notieren.
- Kopfbehälter und Zulaufschlauch erwärmen das Wasser: ein ungedämmter 20-l-Eimer um etwa 1,5 K, ein gedämmter 10–12-l-Behälter um etwa 0,5 K. Deshalb Dämmhülle und kleiner Behälter.

### Leichtbau und Dachgeschoss

Bei C = 0,5 kWh/K liegt der Raum ohne alles bei ≈ 34,6 °C. Das Gerät bringt dort etwa −4 K, die Spitze bleibt aber über 30 °C. In diesem Fall kommen Außenverschattung und Nachtlüftung zuerst. Das Wassergerät allein reicht dort nicht.

## 6. Aufbau

### 6.1 Prinzip und Skizze

Der Pegel im Kopfbehälter treibt das Wasser durch die Heizkörper. Er wird vom Schwimmerventil konstant gehalten. Hinter dem Kopfbehälter gibt es keinen Netzdruck.

```text
 Kaltwasser-Wandventil (vorhandener Abgang, NUR Kaltwasser)
   │ Schlauch, Geräteventil mit Rückflussverhinderer EA,
   │ Durchflussbegrenzer 3 l/min
   ▼
 ┌──────── Kopfbehälter 10–12 l, Deckel, gedämmt ──────────┐  Gestell
 │  Schwimmer-Füllventil, Düse ≥ 20 mm ÜBER Überlaufkante   │  Pegel
 │  ~~~~~~~~~~ konstanter Pegel ≈ 1,3 m ~~~~~~~~~~~~~~~~~~  │  ≈ 55 cm
 │  Überlauf (DN 25) ──► Schlauch DN 32 ──► Abfluss         │  über Trichter
 └───────────────────────┬──────────────────────────────────┘
                         │ Auslauf unten
                   [Sieb] [Dosierventil, voreingestellt]
                         │ ≈ 15 °C   (alles bis HK 1 gedämmt)
                         ▼ unten
 ┌── HK 1 Typ 22, 600×1000 ──┐  Entlüfter oben, Entleerhahn unten,
 │  15 → 18,2 °C   ≈ 93 W    │  Tropfwanne darunter
 └─────────── oben ──────────┘
                         │ Schlauch (oben → unten)
                         ▼
 ┌── HK 2 ───────────────────┐
 │  18,2 → 20,5 °C ≈ 68 W    │  Tropfwanne
 └─────────── oben ──────────┘
                         ▼
 ┌── HK 3 ───────────────────┐
 │  20,5 → 22,2 °C ≈ 50 W    │
 └─────────── oben ──────────┘
                         │ 22,2 °C (Planwert, bei 27 °C Raum)
                         ▼
        Schlauchende 3 cm ÜBER Überlauftrichter (Luftstrecke,
        Höhe ≈ Oberkante HK 3 + 5 cm, verhindert Heber)
                         │ Fallschlauch
                         ▼
        Sammelkübel 40 l ──Überlauf DN 32──► Abfluss (Dusche, WC,
        Waschbecken-Siphon, Bodenablauf)   → Eimer für WC-Spülung
```

**Dosierung:** Der Höhenunterschied zwischen Pegel und Trichter liegt bei ≈ 0,55 m, das sind ≈ 0,054 bar. Für 25 l/h braucht das Dosierventil einen Kv von ≈ 0,11. Das entspricht etwa Voreinstellung 2–3 eines Heizkörper-Thermostat-Ventilunterteils ohne Kopf. Das Sieb davor verhindert Verstopfen. Der Durchfluss bleibt etwa konstant, weil der Pegel konstant bleibt.

**Anschlüsse am Heizkörper:** Zulauf unten, Ablauf oben, die jeweils übrigen Anschlüsse bekommen Blindstopfen. Oben sitzt je ein Entlüfter. Unten ersetzt je ein Entleerhahn (KFE) den freien Stopfen, das ist der echte Tiefpunkt.

### 6.2 Ausbaustufen

| Stufe | Inhalt | Leistung (Planwert, 27 °C) | Wasser | Kosten | Spitze |
|---|---|---|---|---|---|
| Einstieg | 1 gebrauchter Heizkörper, 10 l/h | ≈ 75 W | 100 l/Tag | ≈ 370 € | ≈ −0,7 K |
| Basis | 2 gebrauchte Heizkörper, 15 l/h | ≈ 135 W | 150 l/Tag | ≈ 465 € | ≈ −1,2 K |
| **Voll (Auslegung)** | 3 gebrauchte Heizkörper, 25 l/h | **≈ 211 W** | 250 l/Tag | **≈ 560 €** | **−1,9 K** |
| Sparmodus | wie Voll, 20 l/h | ≈ 192 W | 200 l/Tag | wie Voll | ≈ −1,7 K |

Die Spitzenwerte folgen aus der Faustregel ≈ 0,93 K pro abgeführter kWh.

Die Fixkosten der sicheren Hydraulik (≈ 300 €) sind hoch. Das ist der Preis der Sicherheit. Mit vorhandenem Eimer, Hocker und Kübeln spart man etwa 80 €.

### 6.3 Platz, Last, Mietwohnung

- **Platz:** 3,0 m Wandlänge × 0,15 m für die Heizkörperreihe, dazu etwa 0,5 × 0,5 m für das Gestell und zwei Kübel. Das sind etwa 1 m² Stellfläche.
- **Gewicht:** Die Heizkörper wiegen gefüllt ≈ 95 kg, verteilt auf 3 m (≈ 32 kg/m). Der Kopfbehälter wiegt ≈ 14 kg. Ein Kübel mit 40 l wiegt ≈ 42 kg auf ≈ 0,14 m². Das ist zulässig (Wohnraum-Nutzlast 2 kN/m², Einzellast 2 kN), bei Holzbalkendecken den Kübel nicht randvoll stehen lassen.
- **Mieter:** Es wird nichts gebohrt und nichts an der Installation verändert. Die Heizkörper stehen auf klemmenden Standfüßen, das Gestell steht frei. Eine Kippsicherung (Gurt an einem Haken oder Dübel) braucht die Zustimmung des Vermieters.
- **Alternative bei Platzmangel:** 2 Heizkörper Typ 33 statt 3 Typ 22. Ich schätze etwa 10–15 % weniger Leistung, weil die Konvektionsbleche bei kleinem ΔT schlechter arbeiten. Das ist nicht nachgerechnet.
- **Kaltluftabfall:** Er wird am Heizkörper spürbar. Nicht neben den Sitzplatz stellen, Abstand zur Wand 10 cm.

## 7. Sicherer Trinkwasseranschluss

1. **Trennung durch freien Auslauf (Typ AA):** Das Schwimmer-Füllventil im Kopfbehälter hat eine Luftstrecke von ≥ 20 mm zwischen Düse und höchstem Wasserstand, der durch die Überlaufkante gegeben ist. Das ist das Prinzip jedes WC-Spülkastens.
   - Alles hinter dieser Luftstrecke ist Brauchwasser. Was in gebrauchten Heizkörpern steckt (Inhibitoren, Schlamm, Biofilm), kann nicht zurück ins Netz.
   - Sichtbare Luft bedeutet: Es gibt keinen Tauchfall und keine geschlossene Verbindung zum Abwasser.
2. **Zusatzsicherung:** Ein Geräteventil mit Rückflussverhinderer EA sitzt direkt am Hahn. Es sichert den Schlauch, falls das Füllventil ausgebaut wird. Es ist nicht die Hauptsicherung. EA-Ventile jährlich nach Herstellerangabe prüfen.
3. **Nur vorhandene Abgänge nutzen:** Keine neue Stichleitung, kein T-Stück in der Installation. Nach Feierabend den Wandhahn schließen, nicht den Hahn am Gerät. So steht nur der Schlauch (≈ 0,13 l pro m) still.
4. **Morgens:** ≈ 2–3 l ablaufen lassen, bis das Wasser kühl ist, und das Wasser für WC oder Putzen verwenden.
5. **Nie:** Warmwasser oder Mischbatterie anschließen, das Wasser trinken, duschen oder vernebeln.
6. **Füllventil kann hängen bleiben** (Kalk, Schmutz). Drei Schutzstufen:
   - Der Durchflussbegrenzer (3 l/min) vor dem Ventil begrenzt den Schaden.
   - Der Überlauf (DN 25 am Behälter, DN 32 zum Abfluss) fängt 3 l/min sicher ab.
   - Der Wassermelder alarmiert.
   - Zusätzlich monatliche Sichtprüfung.
7. **Überlaufschlauch:** Er darf nicht knicken und sein Ende nicht angehoben werden. Ende fest in den Abfluss klemmen.
8. **Legionellen:**
   - Das Wasser bleibt < 25 °C und wird nicht versprüht, die Heizkörper sind geschlossen.
   - Es gibt keine tägliche Entleerung. Die Heizkörper bleiben über Nacht gefüllt und werden morgens erneuert: 21 l Heizkörper + 10 l Behälter werden bei 25 l/h in etwa 1,2 h getauscht.
   - Länger als 3 Tage nicht benutzt: über die Entleerhähne entleeren, offen trocknen lassen und nicht nass stehen lassen.
   - Behälter abgedeckt halten (Mücken, Algen).
9. **Korrosion:** Stahl im Frischwasser rostet. Das Wasser kann bräunlich sein, helle Kübel und Emaille verfärben sich.
   - Bei Lochfraß nach mehreren Saisons tropft es nur (Niederdruck).
   - Am Saisonende entleeren und trocknen.
   - Gebrauchte Heizkörper vor dem Kauf auf Rost und Undichtheit prüfen und wässern.
10. **Leckageschutz:** Der Dauerdurchfluss von 0,4 l/min kann in Häusern mit Wasserstopp- oder Leckagesystem (Dauerverbrauch-Erkennung) die Wohnung absperren. Vorher klären.
11. **Gebäudeinstallation:** Der Dauerfluss frischt die Kaltwasserleitung eher auf. Es fließt nichts zurück, und Erwärmung der Kaltwasserleitung entsteht nur, wenn man gar nicht fließen lässt.

## 8. Wasser, Kosten, Weiterverwendung

**Bilanz** (Betriebszeit 9–19 Uhr, Auslegung, Planwert):

| Größe | Wert |
|---|---|
| Durchfluss | 25 l/h → **250 l/Tag** |
| Kälte | 2,04 kWh/Tag, 24-h-Mittel 85 W, Betriebsmittel 204 W |
| Wasser + Abwasser (4,5 €/m³) | 1,13 €/Tag, ≈ 0,55 €/kWh brutto |
| Strom | 0 W (Lüfter optional ≈ 2 W) |
| 20–30 Hitzetage | ≈ 23–34 € brutto |

**Weiterverwendung** (von Hand abholbar, ≈ 100 l/Tag):

| Verwendung | Liter/Tag |
|---|---|
| WC-Spülung mit Eimer (2 Personen, 8–10 Spülungen à 5 l) | 40–60 |
| Putzen, Bodenwischen, Handwäsche | 15–20 |
| Pflanzen | 20–30 |
| **Summe** | **≈ 90–110** |

- **Pflanzen:** Nur Zierpflanzen, und nur bei neuen oder gründlich gespülten Heizkörpern. Gebrauchte Heizkörper können Inhibitor- und Rostreste abgeben. Kein Gemüse oder Kräuter damit gießen.
- **Netto** bleiben ≈ 150 l/Tag als Verlust, etwa 0,68 €/Tag. Wer nichts abholt, zahlt die vollen 1,13 €/Tag.
- **Kürzere Laufzeit:** Betrieb erst ab 12 Uhr (175 l) statt ab 9 Uhr spart 75 l bei +0,4 K. Im Sparmodus (20 l/h) sind es 200 l/Tag.
- **Garten oder Kleingarten:** Dort lassen sich die 250 l/Tag gut verwerten (Gießen), das ist die beste Verwendung.
- **Nicht möglich:** Zurück in Dusche oder Waschmaschine leiten. Das Wasser hat nicht Trinkwasserqualität, und der Druck fehlt (Kreuzverbindungsverbot).
- **Keine Badewanne nötig:** Der Kübel und der Überlaufschlauch zu Dusche, WC-Schüssel, Waschbecken-Siphon oder Bodenablauf reichen. Der Überlauf geht in jeden vorhandenen Abfluss.

**Recht** (keine Rechtsberatung):
- **Vermieter:** Zustimmung einholen. Gewicht, Wasserschaden und Haftpflicht vorher klären.
- **Durchlaufkühlung:** Vieles spricht dafür, dass viele Wasserversorger in ihren Allgemeinen Versorgungsbedingungen die Nutzung von Trinkwasser zur Durchlaufkühlung einschränken. Dieses Vorhaben ist im Kern so eine Durchlaufkühlung. Vorher beim Versorger nachfragen.
- **Abrechnung:** Der Verbrauch läuft über den Wohnungswasserzähler, das Abwasser meist nach Frischwassermenge. Gießwasser wird also mitbezahlt.
- **Trockenheit:** Kommunen können per Allgemeinverfügung Trinkwasser für Kühlzwecke untersagen. Dann nicht betreiben.

## 9. Speicher oder Dauerdurchfluss?

**Dauerdurchfluss.** Der Kopfbehälter (10–12 l) ist nur ein Puffer mit Verweilzeit von ≈ 30 min, kein Speicher. Ein großer Tagesspeicher wäre unhygienisch (Stagnation) und braucht eine Pumpe. Ein 200-l-Tank (15 → 25 °C) liefert nur ≈ 2,3 kWh mit im Mittel geringem Temperaturunterschied zur Raumluft, also eine deutlich schwächere Momentanleistung bei gleichem Wasserbedarf.

## 10. Stückliste (ca.-Preise, Voll-Ausbau)

| Teil | € |
|---|---|
| 3 × Panelheizkörper Typ 22, 600 × 1000, gebraucht (neu 3 × 125) | 150 |
| 3 × Standfuß-Sets (klemmend, ohne Bohren in den Boden) | 60 |
| Kopfbehälter 12 l mit Deckel + Dämmhülle | 25 |
| WC-Füllventil mit Luftstrecke (Seiteneinlass) | 12 |
| 2 Tankdurchführungen (Auslauf ½", Überlauf DN 25) | 15 |
| Geräteventil mit Rückflussverhinderer EA + Zulaufschlauch 2 m + Durchflussbegrenzer 3 l/min | 30 |
| Doppel-Eckventil (nur falls kein freier Abgang vorhanden) | 15 |
| Schmutzsieb + Thermostat-Ventilunterteil (voreinstellbar, als Dosierventil) | 25 |
| 4 Gewebe- oder Wellschläuche ½", 0,5–1,5 m | 40 |
| Fittings (Nippel, Reduzierstücke, Dichtungen) | 15 |
| 3 Entlüfter, 3 Entleerhähne (KFE), Blindstopfen | 35 |
| Überlauftrichter, Fallschlauch, Schellen | 12 |
| 2 Sammelkübel 40 l (mit Überlaufdurchführung) | 28 |
| Überlaufschlauch DN 32, 3 m | 12 |
| Gestell für Kopfbehälter (freistehend) | 25 |
| Rohrdämmung 13 mm (Zulauf bis HK 1) | 8 |
| 2 Wassermelder | 20 |
| 2 Thermometer, Hygrometer, Messbecher 1 l | 23 |
| Kippgurt, Haken | 8 |
| **Summe** | **≈ 560** |

- **Einstieg** (1 Heizkörper) ≈ 370 €, **Basis** (2) ≈ 465 €.
- **Mit neuen Heizkörpern:** ≈ +225 € (Voll ≈ 785 €).
- **Lüfter-Plus:** ≈ +20 €.
- **Beim Kauf gebrauchter Heizkörper** auf Rost, Undichtheit und Verbiegung prüfen.

## 11. Bauanleitung

1. **Vorklärung:** Vermieter, Versorger (Durchlaufkühlung erlaubt?), Wasserstopp-System, Haftpflicht. Zulauftemperatur am vorgesehenen Hahn messen.
2. **Standort:** Innenwand, nicht in der Sonne, Abstand 10 cm zur Wand, nicht neben dem Sitzplatz. Hahn und Abfluss sollten nah liegen (≤ 3 m).
3. **Heizkörper vorbereiten:**
   - Sichtprüfung auf Rost und Undichtheit.
   - Mindestens 30 min mit Schlauch durchspülen, bis das Wasser klar ist, das Abwasser in den Abfluss.
   - Entlüfter und Entleerhähne einsetzen, dichten.
   - 24 h gefüllt stehen lassen und auf Nässe prüfen.
4. **Aufstellen:** Auf Standfüßen, Kippgurt, Tropfwannen unter HK 1 und HK 2.
5. **Kopfbehälter bauen:**
   - Mit Stufenbohrer Auslauf unten und Überlauf etwa 4 cm unter dem Rand bohren, Durchführungen einsetzen.
   - Füllventil seitlich montieren, Düse **≥ 20 mm über der Überlaufunterkante**, Schwimmer so einstellen, dass er ≥ 2 cm darunter abschaltet.
   - Dämmhülle, Deckel mit Schlitz für den Zulaufschlauch.
6. **Gestell:** Der Pegel liegt etwa 55 cm über dem Überlauftrichter. Der Trichter sitzt etwa 5 cm über der Oberkante von HK 3.
7. **Hydraulik:** Auslauf Behälter → Sieb → Dosierventil (Flussrichtung beachten) → Schlauch zu HK 1 unten. Dann HK 1 oben → HK 2 unten → HK 2 oben → HK 3 unten. HK 3 oben → Bogen → Schlauchende 3 cm über den Trichter → Fallschlauch in den Kübel. Alles Kalte dämmen.
8. **Überlauf:** Überlaufschlauch DN 32 vom Behälter und vom Kübel zum Abfluss, fest geklemmt, kein Knick.
9. **Hahn:** Kaltwasser-Wandventil → Geräteventil EA (Durchflussbegrenzer drin) → Schlauch → Füllventil.
10. **Erstbefüllung:** Wasserventil langsam öffnen, Entlüfter öffnen, bis Wasser kommt. 1 h auf Dichtheit prüfen, Wassermelder aufstellen.
11. **Dosieren:**
    - Ziel 0,4 l/min: Messbecher am Fallrohr, 1 l in etwa 2,5 min.
    - Zweite Regelgröße: **Ablauftemperatur 22–24 °C**. Über 25 °C mehr Wasser. Unter 21 °C weniger Wasser, sonst verschwendet man Liter.
    - Nach 2 h nachmessen.
12. **Betrieb:**
    - Morgens Wandhahn öffnen, erst 2–3 l ablaufen lassen, dann Zulaufschlauch anschließen.
    - Zulauftemperatur nach 30 min und 3 h prüfen.
    - Abends Wandhahn zu.
    - Wöchentlich Füllventil und Sieb sichten, Wannen und Kübel reinigen.
13. **Nachmessen:** Q = 1,163 × l/h × (T_aus − T_ein), Erwartung Planwert ≈ 205–210 W (Tabelle in Abschnitt 3).

## 12. Grenzen, ehrlich

- **Die Hauptzahl ist eine Annahme.** 211 W (Planwert) bis 256 W (Modell), Bandbreite 169–256 W. Erst Nachmessen nach dem Aufbau zeigt, wo der Aufbau liegt.
- **Wasser ist ein dünner Kälteträger.** 119 l/kWh beim Planwert (95 l/kWh bei 12 °C, 158 bei 18 °C). Das kostet 0,55–0,74 €/kWh brutto, drei- bis sechsmal so viel wie ein Klimagerät.
- **Allein reicht es nicht für ≤ 26 °C.** Erst mit Außenverschattung und guter Nachtlüftung kommt der Raum auf 25,6–26,3 °C. Im Dachgeschoss bleibt es über 30 °C.
- **Zulauftemperatur ist die Hauptunsicherheit.** Ab 18 °C lohnt es sich kaum, ab 20 °C gar nicht.
- **Mehr Leistung kostet überproportional Wasser:** +12 % Leistung kosten +40 % Wasser.
- **Nur etwa 100 l/Tag** sind ohne Garten sinnvoll weiterverwendbar. Gebrauchte Heizkörper machen das Wasser für Pflanzen ungeeignet.
- **Bei Wasserstopp-System im Haus, Trockenheitsverbot, Versorger-Verbot oder Zulauf ≥ 20 °C** bleibt das Gerät aus.
- **Das größte Alltagsrisiko** ist ein hängendes Füllventil, ein geknickter Überlaufschlauch oder ein undichter Heizkörper. Dagegen helfen Durchflussbegrenzer, Überlauf, Wassermelder und Sichtprüfung.

## 13. Energiebilanz

Die Bilanz ist das **Mittel der Betriebszeit 9–19 Uhr** im Auslegungsfall: Gerät allein, Planwert, Zulauf 15 °C, 25 l/h, ohne Außenverschattung.

- Die Raumluft liegt ohne Gerät im Mittel bei 27,7 °C und mit Gerät bei 26,8 °C.
- Die Kühlleistung beträgt 204 W (24-h-Mittel 85 W).
- Das Wasser tritt im Mittel mit ≈ 22,0 °C aus. Die mittlere Oberflächentemperatur der Heizkörper ist ≈ 19,3 °C.
- Der Leitungswasserverbrauch beträgt 250 l/Tag. In die Luft verdunstet im Auslegungsfall nichts, Kondensat fällt kaum an.

```json
{
  "knoten": {
    "Wohnung": {"T_C": 26.8, "rolle": "umgebung"},
    "Heizkoerper": {"T_C": 19.3, "rolle": "komponente"},
    "Leitungswasser": {"T_C": 15, "rolle": "umgebung"}
  },
  "stroeme": [
    {"von": "Wohnung", "nach": "Heizkoerper", "W": 204, "art": "waerme"},
    {"von": "Heizkoerper", "nach": "Leitungswasser", "W": 204, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Wohnung", "T_ein_C": 27.7, "T_aus_C": 26.8, "kuehlleistung_W": 204},
  "luft_T_C": 30,
  "wasserverlust_l_pro_tag": 0
}
```