# Zimmerkühlung mit Leitungswasser: Gebläse-Wasserregister mit Schwerkraftzulauf

## 0. Go/No-Go vor jedem Einkauf

Dieses Gerät ist rechtlich eine **Durchlaufkühlung mit Trinkwasser**. Das kann das ganze Vorhaben kippen, also zuerst klären (keine Rechtsberatung):

| # | Frage | Bei "Nein" |
|---|---|---|
| 1 | Erlaubt der Wasserversorger (Satzung, Ergänzende Bestimmungen, AVB) Kühlung im Durchlauf? Viele Versorger untersagen oder beschränken das. Schriftliche Auskunft einholen. | Fallback (Abschnitt 9) |
| 2 | Vermieter einverstanden (Wasserschaden, Haftpflicht)? | Fallback |
| 3 | Gibt es im Haus ein Wasserstopp- oder Leckagesystem, das Dauerfluss (0,3 l/min) als Leck wertet? | Fallback |
| 4 | Gibt es eine Allgemeinverfügung wegen Trockenheit? | Gerät aus |
| 5 | Zulauftemperatur am vorgesehenen Hahn ≤ 18 °C (morgens und nachmittags 5 min laufen lassen, messen)? | Ab 20 °C lohnt es nicht |
| 6 | Sind Wandhahn und Abfluss ≤ 4 m vom Aufstellort entfernt, ohne Stolperfalle? | Variante B (Speicher) |

**Fallback ohne Durchlauf:** Außenverschattung und Nachtlüftung bringen ohne Wasser etwa 27,2 °C statt 30,4 °C, siehe Abschnitt 9.

## 1. Kurzfazit

**Prinzip:** Zwei kleine Wasser-Luft-Wärmetauscher (neue Kfz-Heizungskühler) stehen in einer Kühlbox. Zwei 12-V-Lüfter mit zusammen etwa 4 W (inkl. Netzteil) blasen Raumluft hindurch. Das Wasser läuft drucklos aus einem Kopfbehälter mit freiem Auslauf (wie im WC-Spülkasten) durch beide Register und danach in den Abfluss, den Spülkasten oder die Gießkanne. Es gibt keine Kältemaschine, keinen Netzdruck am Kühler und keine Verbindung zur Trinkwasserleitung.

**Warum Gebläse statt Panelheizkörpern?** Ein Lüfter hebt den Luft-Wärmeübergang stark an. Das Wasser tritt dann fast raumwarm aus (25 °C statt 22 °C), und jeder Liter trägt mehr Kälte:

| | Gebläse-Register (Auslegung) | 3 Panelheizkörper ohne Strom (Alternative) |
|---|---|---|
| Kühlleistung bei 27 °C Raum, Zulauf 15 °C | 239 W | 211 W |
| Wasser pro Tag (10 h) | 200 l | 250 l |
| Liter pro kWh | 84 | 119 |
| Strom | 4 W | 0 W |
| Gewicht gefüllt | ≈ 4 kg Kühler + 12 kg Kopfbehälter | ≈ 95 kg Heizkörper |
| Kosten | ≈ 365 € (Sparstufe ≈ 225 €) | ≈ 560 € |

Die 4 W Strom kosten pro Tag 1,4 Cent. Sie sparen etwa 50 l Wasser, das sind 22 Cent. Deshalb ist der Lüfter die klar bessere Wahl.

**Ergebnisse** (Auslegungsfall, 20 m²-Zimmer, 10 h Betrieb 9–19 Uhr, Planwert):

| Größe | Wert |
|---|---|
| Kühlleistung bei 27 °C Raum, 15 °C Zulauf | 239 W (Bandbreite 175–255 W) |
| Netto-Mittel 9–19 Uhr (nach Abzug der Lüfterwärme) | **229 W**, 24-h-Mittel 95 W |
| Kälte pro Tag | 2,3 kWh |
| Leitungswasser | **200 l/Tag** (Wasser + Abwasser 0,90 €/Tag) |
| Wasseraustritt, Tagesmittel | 25,0 °C, also 11,6 Wh/l |
| Raumtemperatur im Mittel 9–19 Uhr | 27,7 °C ohne, 26,7 °C mit Gerät (**−1,0 K**) |
| Spitze um 19 Uhr, nur Gerät | 28,3 °C statt 30,4 °C (**−2,1 K**) |
| Spitze um 19 Uhr, Gerät + Außenverschattung | **26,1 °C** statt 28,05 °C |

**Rangfolge der Maßnahmen:**
1. **Außenverschattung:** −2,35 K an der Spitze, so viel wie das Gerät.
2. **Nachtlüftung:** 1 K tieferer Start ergibt 0,7 K weniger um 19 Uhr (0,85 K ohne Gerät).
3. **Wassergerät:** −1,9 bis −2,1 K zusätzlich.

Mit allen dreien sind 26,1 °C (Start 25,5 °C) bis 25,4 °C (Start 24,5 °C) erreichbar. Nur mit dem Gerät bleibt man bei 28,3 °C.

**Ehrliche Grenzen:**
- Die Kälte kostet je nach Weiterverwendung des Wassers 0,2–0,4 €/kWh. Ein Klimagerät liegt bei etwa 0,14 €/kWh (Strom 0,35 €/kWh, reale EER ≈ 2,5).
- Das Gerät ist eine Option für einige Hitzetage, wenn Strom, Lärm und Abluftschlauch nicht infrage kommen.
- Die Untergrenze liegt physikalisch bei 72 l/kWh (siehe Abschnitt 2). 100 l/Tag sind nur für 1,2–1,4 kWh möglich, nicht für 2,3 kWh.

## 2. Physik: Was steckt im Liter?

Wasser nimmt 1,163 Wh/(l·K) auf. Daraus folgt: **Liter pro kWh = 860 / Temperaturhub des Wassers.**

- Der Hub ist höchstens Raumluft minus Zulauf, bei 27 °C und 15 °C also 12 K. Das ergibt **72 l/kWh als harte Untergrenze**, das sind 14 Wh/l.
- Die Faustzahl "8 Wh/l" gilt nur für 7 K Hub.
- Wie nah man an die 72 kommt, hängt von der Wärmetauscherfläche und dem Luftstrom ab. Dort hilft der Lüfter.

**Wie viel Wasser für eine spürbare Absenkung?**
- Mit dem Gerät kostet **1 K Spitzenabsenkung ≈ 1,1 kWh ≈ 95 l Wasser** (Faustregel 0,92 K je abgeführter kWh).
- −2 K kosten also ≈ 200 l/Tag.

## 3. Kühler: Wärmeübertragung

### 3.1 Bauteil und Auslegung

- **Zwei Kfz-Heizungswärmetauscher, neu,** ca. 200 × 200 × 32 mm (Innenraumheizung, nicht Motorkühler).
- Material: Kupfer/Messing oder komplett Aluminium, nicht gemischt. Endkästen für ≥ 1 bar, Stutzen 16–20 mm.
- **Wasserseitig in Reihe**, unten rein, oben raus. Die Strömung geht also mit dem Auftrieb, und Luftblasen wandern nach oben mit.
- **Luftseitig parallel:** Jeder Kern hat seinen eigenen 200-mm-Lüfter, je ≈ 90 m³/h (Kennlinie beachten: Kern-Druckverlust ≈ 10–15 Pa).
- Luftkapazitätsstrom je Kern: 0,0293 kg/s × 1005 J/(kg·K) = **29,4 W/K**.

### 3.2 Herleitung des Leitwerts UA

Es gibt zwei unabhängige Abschätzungen, und die Planung liegt am unteren Ende beider:

1. **Geometrie (von unten):**
   - Kern 200 × 200 × 32 mm, Lamellenteilung ≈ 1,6 mm, etwa 20 Flachrohre, Fläche A ≈ 1,4 m².
   - Bei 90 m³/h ist die Anströmgeschwindigkeit 0,63 m/s und in den Lamellenspalten ≈ 0,75 m/s. Mit Dh ≈ 3 mm ergibt sich Re ≈ 130, also laminar und thermisch anlaufend mit Nu ≈ 7–8.
   - Das gibt h ≈ 65 W/m²K, einen Lamellenwirkungsgrad von ≈ 0,96 und theoretisch **UA ≈ 90 W/K**.
   - Das ist ein Idealwert. Ungleichverteilung, Staub und Randströmung senken ihn deutlich.
2. **Katalog (von oben):**
   - Kerne dieser Größe werden mit etwa 3–5 kW bei 80 °C Kühlmittel, 20 °C Luft und 300–400 m³/h angegeben. Das entspricht UA ≈ 70–120 W/K bei 400 m³/h.
   - UA skaliert etwa mit V^0,55. Bei 90 m³/h ergibt das **UA ≈ 31–53 W/K**.

**Planwert: UA = 38 W/K je Kern.** Die Bandbreite UA = 15–57 W/K wird unten durchgerechnet.

### 3.3 Rechnung (ε-NTU, Kreuzstrom, Raum 27 °C, Zulauf 15 °C)

- Je Kern gilt ε = 1 − exp[(NTU^0,22 / Cr) · (exp(−Cr · NTU^0,78) − 1)].
- Zwei Stufen in Reihe mit frischer Luft je Stufe: T_aus − T_ein = [1 − (1 − ε)²] · (T_Raum − T_ein).
- Beispiel 20 l/h: C_w = 23,3 W/K, Cr = 0,79, NTU = 1,63, ε = 0,62. Das gibt 0,856 · 12 K = 10,3 K Hub, **Q = 239 W, T_aus = 25,3 °C**. Zwischen den Kernen liegt das Wasser bei 22,4 °C.

| Durchfluss (2 Kerne) | Leistung | Austritt | l/kWh |
|---|---|---|---|
| 10 l/h | 137 W | 26,8 °C | 73 |
| 15 l/h (Sparmodus) | 195 W | 26,2 °C | 77 |
| **20 l/h (Auslegung)** | **239 W** | **25,3 °C** | **84** |
| 25 l/h | 272 W | 24,4 °C | 92 |
| 30 l/h | 299 W | 23,6 °C | 100 |

Mehr Wasser bringt kaum mehr Leistung. Von 20 auf 30 l/h bringen +50 % Wasser nur +25 % Leistung. Daher 20 l/h, im Sparmodus 15 l/h.

### 3.4 Empfindlichkeit gegen UA

| UA je Kern | Leistung bei 20 l/h | Austritt |
|---|---|---|
| 15 W/K | 175 W | 22,5 °C |
| 25 W/K | 214 W | 24,2 °C |
| **38 W/K** | **239 W** | 25,3 °C |
| 57 W/K | 255 W | 25,9 °C |

Die Leistung ist robust: Zwei Stufen und hohes ε machen sie unempfindlich gegen UA-Fehler (±10 % bei UA 25–57). Nur ein klar zu schwacher Luftstrom oder Verstopfung würde sie unter 175 W drücken.

### 3.5 Lüfterwärme

Die Lüfter (2 × 1,5 W plus Netzteilverlust) geben **≈ 4 W** in den Raum ab. Die Netto-Kühlleistung ist also Q − 4 W.

Optional kann ein 10-W-Solarmodul am Fenster die Lüfter direkt antreiben. Die Drehzahl folgt dann der Sonne, was gut zur Last passt (≈ 25 €, nicht eingerechnet).

### 3.6 Alternative ohne Strom: Panelheizkörper

Natürliche Konvektion und Strahlung, von unten gerechnet für einen Typ 22, 600 × 1000 mm, bei ΔT ≈ 8 K:

| Fläche | h (W/m²K) | UA |
|---|---|---|
| Frontblech 0,6 m² | 2,7 Konvektion + 4,6 Strahlung = 7,3 | 4,4 W/K |
| Rückseite (Wandnähe) | ≈ 4,0 | 2,4 W/K |
| Konvektorlamellen | | ≈ 2 W/K |
| **Summe** | | **≈ 9 W/K** |

Das entspricht 0,65 × der Norm-Extrapolation (13,9 W/K bei 8 K Übertemperatur). Drei Stück ergeben 27 W/K und bei 25 l/h (ε ≈ 0,6) 211 W. Das braucht aber 250 l/Tag und 95 kg. Es funktioniert, ist aber die schlechtere Wahl.

## 4. Kondensation und Entfeuchtung

**Taupunkte:** 27 °C/50 % ≈ 15,8 °C, 28 °C/50 % ≈ 16,6 °C, 28 °C/65 % ≈ 20,8 °C. Das Zulaufwasser (15 °C) liegt darunter. Die Kondensation betrifft aber nur Kern 1, dessen Wasser von 15 auf 22 °C steigt.

Grobe Abschätzung (±50 %, Lewis-Zahl 1, Teilbenetzung von Kern 1):

| Fall | nasser Bereich | latent | Kondensat | Anmerkung |
|---|---|---|---|---|
| 27 °C/50 %, Zulauf 15 °C (Auslegung) | nur Eintrittsecke | < 5 W | < 10 g/h | praktisch trocken |
| 28 °C/50 %, 15 °C | unteres Drittel Kern 1 | ≈ 10 W | ≈ 15 g/h | |
| 27 °C/50 %, 12 °C | großer Teil Kern 1 | ≈ 15 W | ≈ 30 g/h | |
| 28 °C/65 % (schwül), 15 °C | Kern 1 fast ganz | ≈ 45 W | ≈ 65 g/h (0,7 l/Tag) | Gesamt ≈ 250 W, nur ≈ 205 W sensibel |

**Einordnung:**
- Latente Leistung kommt nicht obendrauf. Sie verbraucht einen Teil der Gesamtleistung.
- Bei Schwüle sinkt die Lufttemperatur weniger, dafür wird die Luft trockener (65 g/h ≈ Feuchteabgabe einer Person). Das ist ein Komfortgewinn, kein Temperaturgewinn. In der Temperaturbilanz setze ich ihn nicht an.

**Wohin mit dem Kondensat?**
- Eine Wanne unter Kern 1 (Backblech mit Ablaufstutzen) führt per Schlauch zum Auslauftrichter.
- Zulaufschlauch, Dosierventil und Kopfbehälter haben etwa 15 °C und schwitzen in schwüler Luft. Sie bekommen 13 mm Dämmung.

## 5. Wärmelast und Raumtemperatur

### 5.1 Herleitung der Raumlast

Annahme: 20 m² (4 × 5 m) × 2,5 m, mittleres Geschoss. Es gibt eine Außenwand nach Südwest, Nachbarräume liegen auf gleicher Temperatur, also gibt es kein Dach und keine Bodenplatte.

| Posten | Annahme | Wert |
|---|---|---|
| Außenwand 10,5 m² (12,5 m² minus Fenster) | U = 1,0 W/m²K (36-cm-Ziegel, leicht gedämmt) | 10,5 W/K |
| Fenster 2 m² | U = 1,8 W/m²K | 3,6 W/K |
| Lüftung/Fugen | 0,2 h⁻¹ × 50 m³ × 0,34 Wh/m³K, plus Türfugen | ≈ 3,5 W/K |
| **G gesamt** | | **17,6 W/K** |
| Wandbesonnung | α ≈ 0,5, Masse dämpft: Außentemperatur effektiv + 1,5 K | |
| Sonne durch Fenster | 2 m² × g 0,6 × Innenvorhang-Faktor 0,55 × Bestrahlung SW (230 W/m² um 9 Uhr, 680 W/m² Spitze 15–17 Uhr) | 150 … 450 W |
| Innere Lasten | Person 70 W + Laptop 30 W + Licht 10 W (nur sensibel) | 110 W |
| Speichermasse | ≈ 90 m² Oberfläche × ≈ 50 kJ/m²K wirksam im 10-h-Zyklus | C = 1,0 kWh/K |

- Außentemperatur 9–19 Uhr stündlich: 25 / 26,5 / 28 / 29 / 30 / 30 / 30 / 30 / 29,5 / 28,5 °C.
- Sonne W, stündlich: 150, 200, 250, 300, 350, 400, 450, 450, 420, 330.
- Start 25,5 °C nach Nachtlüftung, Außenverschattung −75 % Sonne.
- Modell: C · dT/dt = Sonne + 110 W + G · (T_außen + 1,5 K − T) − Q_Gerät. Gerät: Q = 19,9 W/K · (T − 15 °C) − 4 W Lüfterwärme.
- Rechnung in 1-h-Schritten, Genauigkeit ±0,1 K im Modell. Die Annahmen selbst sind ±0,3 K unsicher.

### 5.2 Ergebnis

| Uhr | nichts | nur Gerät | nur Außenverschattung | Außen + Gerät |
|---|---|---|---|---|
| 9 | 25,5 | 25,5 | 25,5 | 25,5 |
| 11 | 26,1 | 25,7 | 25,9 | 25,5 |
| 13 | 27,0 | 26,2 | 26,4 | 25,5 |
| 15 | 28,2 | 26,9 | 26,9 | 25,7 |
| 17 | 29,4 | 27,7 | 27,6 | 25,9 |
| 19 | **30,4** | **28,3** | **28,05** | **26,1** |

**Gerät allein:**
- Mittlere Raumtemperatur 9–19 Uhr: 27,7 °C ohne, **26,7 °C** mit Gerät (−1,0 K).
- Wasserseitig 233 W, netto 229 W (nach Abzug von 4 W Lüfterwärme). Das sind 2,3 kWh pro Tag und 95 W im 24-h-Mittel.

**Empfindlichkeit Startwert (Nachtlüftung):**

| Start 9 Uhr | nichts | nur Gerät | Außen + Gerät |
|---|---|---|---|
| 24,5 °C | 29,6 | 27,6 | **25,4** |
| 25,5 °C | 30,4 | 28,3 | 26,1 |
| 26,5 °C | 31,2 | 29,0 | 26,8 |

Von 1 K Startunterschied bleiben nach 10 h etwa 0,7 K (mit Gerät) bzw. 0,85 K (ohne Gerät) an der Spitze übrig.

**Empfindlichkeit Zulauftemperatur** (20 l/h, Raum 27 °C, Zulauf = Wassertemperatur am Eintritt). Der Kopfbehälter erwärmt das Wasser um etwa 0,5 K, daher zählt die Temperatur am Kernzulauf:

| Zulauf | Leistung | Austritt | l/kWh | Spitze, nur Gerät | Spitze, Außen + Gerät |
|---|---|---|---|---|---|
| 12 °C | 299 W (+ ≈ 15 W latent) | 24,8 °C | 67 | ≈ 27,9 | ≈ 25,6 |
| **15 °C** | **239 W** | 25,3 °C | 84 | 28,3 | 26,1 |
| 18 °C | 179 W | 25,7 °C | 112 | ≈ 28,8 | ≈ 26,7 |
| 20 °C | 139 W | 26,0 °C | 144 | ≈ 29,1 | ≈ 27,0 |

Bis 18 °C lohnt der Betrieb noch, ab 20 °C bringt er zu wenig. Steigleitungen stehen morgens oft warm. Daher morgens zuerst 2–3 l ablaufen lassen, bis das Wasser kühl ist.

**Laufzeit:** Start erst um 12 statt 9 Uhr spart 60 l und kostet etwa +0,4 bis 0,5 K an der Spitze. Nachts laufen lassen lohnt nur, wenn Fenster geschlossen bleiben müssen. Der Hub pro Liter sinkt dann auf etwa 77 %, und die Kälte klingt bis zum Nachmittag ab.

**Dachgeschoss oder Leichtbau:** Der Raum liegt ohne alles bei etwa 34 °C. Das Gerät bringt dort −3 bis −4 K, die Spitze bleibt aber über 30 °C. Dort kommen Verschattung und Nachtlüftung zuerst.

## 6. Aufbau

### 6.1 Skizze

```text
 Kaltwasser-Wandventil (vorhandener Abgang, NUR Kaltwasser)
   │ Geräteventil mit Rückflussverhinderer EA + Durchflussbegrenzer 3 l/min
   │ (Netzdruck nur bis hier, Waschmaschinen-Schlauch 2 m)
   ▼
 ┌─ Kopfbehälter 10 l, Deckel, gedämmt ───────────┐  Regalbrett,
 │ WC-Füllventil, Düse ≥ 20 mm ÜBER Überlaufkante  │  Pegel ≈ 1,5 m
 │ ~~~~~~~~ konstanter Pegel ~~~~~~~~~~~~~~~~~~~~~ │
 │ Überlauf DN 25 ──► Schlauch ──► Abfluss         │
 └──────────────────┬──────────────────────────────┘
                    │ Bodenauslauf ½"
               [Sieb] [Dosierventil, ≈ 0,03 bar, Kv ≈ 0,11]
                    │ ≈ 15,5 °C (gedämmt)
                    ▼ unten
   ┌── Kühlbox auf Kommode (Ansicht von der Seite) ──────────┐
   │  Kern 2 (200×200)  ◄── Lüfter 2 (~1,5 W)  → Luft ≈ 25 °C │
   │    Wasser 22,4 → 25,3 °C                                 │
   │  Kern 1 (200×200)  ◄── Lüfter 1 (~1,5 W)  → Luft ≈ 21 °C │
   │    Wasser 15,5 → 22,4 °C        (Mischluft ≈ 23 °C)      │
   │  Tropfwanne mit Ablaufstutzen ─────────────────────┐     │
   └──────────────────────────────────────────────────── │ ───┘
              oben, Entlüfter am Hochpunkt               │
                    ▼                                    │
        Schlauchende 3 cm ÜBER Trichter (Luftstrecke) ◄──┘
        (Trichter ≈ 0,3 m unter Pegel)
                    │ Fallschlauch
                    ▼
        Sammelkübel 40 l auf Hocker ─ Überlauf ─► Abfluss
        oder direkt in den Spülkasten / Gießkanne
```

**Dosierung:**
- Der Höhenunterschied Pegel–Trichter beträgt ≥ 0,3 m, das sind ≈ 0,03 bar.
- Für 20 l/h (0,02 m³/h) braucht das Dosierventil Kv = 0,02 / √0,03 ≈ 0,115. Das entspricht einem voreingestellten Thermostatventil-Unterteil ohne Kopf (Stellung 2–3).
- Der Pegel bleibt konstant, also bleibt der Durchfluss konstant, unabhängig vom Netzdruck.

### 6.2 Aufstellung und Platz

- **Standort:** Zimmer direkt neben Bad oder Küche, Schlauchweg ≤ 4 m zum Abfluss. Der Überlaufschlauch (DN 32, ≥ 2 % Gefälle) läuft durch die Tür unter einer Kabel- oder Schlauchbrücke.
- **Kühlbox:** ≈ 25 × 45 × 25 cm, auf einer Kommode oder einem Tisch. Ausblas in den Raum, nicht auf den Sitzplatz, Abstand zur Wand ≥ 10 cm.
- **Kopfbehälter:** Regalbrett bei ≈ 1,4 m Höhe, Gewicht gefüllt ≈ 12 kg.
- **Kübel:** 40 l wiegen ≈ 42 kg, auf Hocker (Gefälle zum Abfluss). Bei Holzbalkendecken nicht randvoll stehen lassen.
- **Geräusch:** Die Lüfter laufen bei ≈ 600–700 U/min. Erwartet werden 20–25 dB(A). Das ist im Datenblatt zu prüfen.
- **Mietwohnung:** Es wird nichts gebohrt und nichts an der Installation verändert. Der Schlauch hängt nur an einem vorhandenen Wandventil.

### 6.3 Ausbaustufen

| Stufe | Inhalt | Leistung bei 27 °C Raum | Wasser/Tag | Spitze nur Gerät | Spitze Außen + Gerät | Kosten |
|---|---|---|---|---|---|---|
| Sparstufe | 1 Kern, 1 Lüfter, 10 l/h | 122 W | 100 l | ≈ 29,3 °C | ≈ 27,1 °C | ≈ 225 € |
| Voll, Sparmodus | 2 Kerne, 15 l/h | 195 W | 150 l | ≈ 28,7 °C | ≈ 26,5 °C | ≈ 365 € |
| **Voll (Auslegung)** | 2 Kerne, 20 l/h | **239 W** | 200 l | 28,3 °C | 26,1 °C | ≈ 365 € |

Mit vorhandenem Eimer, Regalbrett, Thermometer und Wassermelder sinkt die Sparstufe auf etwa 170 €. Sie ist zugleich der **Messaufbau**: Damit lässt sich UA vor der Erweiterung prüfen (Abschnitt 11).

## 7. Sicherer Trinkwasseranschluss und Hygiene

1. **Trennung durch freien Auslauf:** Das Füllventil im Kopfbehälter hat ≥ 20 mm Luftstrecke zwischen Düse und höchstem Wasserstand (Überlaufkante). Das ist das Prinzip jedes WC-Spülkastens. Alles dahinter ist Brauchwasser und kann nicht zurück in die Leitung.
2. **Zusatzsicherung:** Ein Geräteventil mit Rückflussverhinderer EA sitzt direkt am Hahn. Es sichert den Schlauch, falls das Füllventil ausgebaut wird. EA-Ventile jährlich nach Herstellerangabe prüfen.
3. **Nur vorhandene Abgänge nutzen,** keine neue Stichleitung und kein T-Stück. Nach Feierabend den Wandhahn schließen.
4. **Nie:** Warmwasser oder Mischbatterie anschließen, das Wasser trinken oder vernebeln.
5. **Füllventil kann hängen bleiben.** Schutzstufen:
   - Der Durchflussbegrenzer (3 l/min) begrenzt den Schaden.
   - Der Überlauf DN 25 am Behälter, dazu der Überlaufschlauch DN 32, fängt 3 l/min sicher ab.
   - Wassermelder alarmieren.
   - Monatlich Sichtprüfung. Den Überlaufschlauch fest im Abfluss klemmen, nicht knicken, Ende nicht anheben.
6. **Strom und Wasser:** Die Lüfter laufen mit 12 V. Das Steckernetzteil steht höher als alle Wasserteile und außerhalb der Tropfzone. Die Tropfwanne fängt Kondensat und Leckwasser.
7. **Legionellen und Biofilm:**
   - **Nur neue Teile,** keine gebrauchten Kühler mit altem Biofilm oder Inhibitoren. Vor dem Einsatz 30 min durchspülen.
   - Das Wasser bleibt im Mittel unter 25 °C und wird nicht versprüht.
   - **Täglicher Zyklus:** Abends Wandhahn zu. Der Kopfbehälter läuft in etwa 20 min leer, danach Schlauch am Kern abziehen und den Kern ablaufen lassen. Behälter und Kübel abtropfen lassen.
   - Die Wassermenge im System ist klein (Kerne ≈ 0,4 l je Stück, Behälter 10 l), sie wird täglich erneuert.
8. **Korrosion:** Alu, Kupfer und Messing in Frischwasser sind für eine Saison in Ordnung. Am Saisonende entleeren und trocknen. Bei Lochfraß tropft es nur (0,03 bar).
9. **Leckageschutz im Haus:** Der Dauerfluss von 0,33 l/min kann ein Wasserstoppsystem auslösen. Vorher klären (Go/No-Go Nr. 3).
10. **Gebäudeinstallation:** Der Dauerfluss frischt die Kaltwasserleitung eher auf. Es fließt nichts zurück.

## 8. Wasser, Kosten, Weiterverwendung, Recht

**Bilanz (Auslegung, 10 h):**

| Größe | Wert |
|---|---|
| Durchfluss | 20 l/h, **200 l/Tag** (ein Mensch verbraucht im Schnitt ≈ 120 l/Tag) |
| Wasser + Abwasser, 4,5 €/m³ | 0,90 €/Tag, ≈ 0,39 €/kWh |
| Strom | 4 W, 0,04 kWh/Tag, ≈ 1,4 ct |
| 25 Hitzetage | ≈ 23 € brutto |

**Weiterverwendung (nur Brauchwasser, nicht für Hautkontakt):**

| Verwendung | Liter/Tag |
|---|---|
| **WC-Spülkasten:** Fallschlauch in den Spülkasten (über Wasserspiegel). Sein Füllventil schließt, solange das Kastenwasser reicht. Der Überlauf des Kastens ist harmlos. | 30–50 |
| Boden wischen, Fenster putzen (nicht Handwäsche) | 10–20 |
| Zierpflanzen, Balkon (nur neue Kühler, gespült) | 20–50 |
| **Summe realistisch** | **60–120** |

- Kein Gemüse oder Kräuter gießen. Nicht in Dusche, Waschmaschine oder Handwäsche leiten (Kreuzverbindungsverbot, keine Trinkwasserqualität, kein Druck).
- **Netto-Kosten:** Bei 100 l Weiterverwendung bleiben 100 l Verlust, also 0,45 €/Tag und ≈ 0,19 €/kWh. Bei nur 40 l (WC) sind es 0,72 €/Tag (0,31 €/kWh). Wer nichts weiterverwendet, zahlt 0,39 €/kWh.
- **Mit Garten** lassen sich die 200 l/Tag fast vollständig nutzen (Gießen, 25 °C ist ideal). Das ist die beste Verwendung.
- **Weniger Wasser:** Sparmodus 15 l/h (150 l/Tag, 195 W) oder Start erst um 12 Uhr (−60 l, +0,4 bis 0,5 K).

**Recht (keine Rechtsberatung):**
- **Versorger:** Durchlaufkühlung mit Trinkwasser ist oft ausgeschlossen oder genehmigungspflichtig. Das ist K.-o.-Kriterium Nr. 1 (Abschnitt 0).
- **Vermieter:** Zustimmung, Haftpflicht und Wasserschaden vorher klären.
- **Abrechnung:** Der Verbrauch läuft über den Wohnungswasserzähler. Das Abwasser wird meist nach Frischwassermenge berechnet. Gießwasser wird also mitbezahlt, außer bei einem Gartenzähler.
- **Trockenheit:** Kommunen können per Allgemeinverfügung die Nutzung für Kühlzwecke untersagen. Dann nicht betreiben.

## 9. Speicher oder Dauerdurchfluss? Fallback ohne Durchlauf

**Standard: Dauerdurchfluss** von 20 l/h über den 10-l-Kopfbehälter. Der Behälter ist nur ein Puffer (Verweilzeit ≈ 30 min). Ein großer Tagesspeicher wäre hygienisch schlechter und braucht eine Pumpe.

### Variante B: Speicherbetrieb (falls Durchlauf verboten ist oder kein Abfluss in der Nähe liegt)

- **Aufbau:** Dieselbe Kühlbox. Statt des Kopfbehälters steht eine 60-l-Tonne mit Deckel neben der Box. Eine 12-V-Mini-Pumpe (≈ 3 W, zusammen mit den Lüftern ≈ 7 W) wälzt 120 l/h durch beide Kerne (Wasser oben zurück in die Tonne).
- **Befüllung:** Mit Schlauch vom Wandhahn über freien Auslauf (EA-Ventil, wie oben). Es gibt keinen Dauerfluss, die Wassermenge ist genau die befüllte.
- **Rechnung:** Bei 120 l/h ist C_w ≫ C_Luft und ε je Kern ≈ 0,68. Zusammen ≈ 37 W/K × (T_Raum − T_Tonne). Die Tonne hat 70 Wh/K. Das ergibt:
  - bis 24 °C Tonnentemperatur: 628 Wh in ≈ 2,6 h (Mittel ≈ 240 W),
  - bis 25 °C: ≈ 700 Wh in ≈ 3,4 h (Mittel ≈ 210 W),
  - also **≈ 86 l/kWh**, ähnlich wie im Durchlauf.
- **Tagesbetrieb:** Zwei Füllungen pro Tag (9–12 Uhr und 13–16 Uhr) bringen ≈ 1,3–1,4 kWh, also −1,2 K an der Spitze und 120 l/Tag.
- **Verwendung:** Das Wasser wird am selben Tag für WC, Putzen und Pflanzen genutzt. Abends Tonne leeren und trocknen (Legionellen: nie über Nacht bei 25 °C stehen lassen).
- **Nachteil:** Es ist Handarbeit, und die Leistung ist um etwa 40 % niedriger als im Durchlauf.

### Fallback-Paket ohne Wasser (Stufen)

| Stufe | Maßnahme | Spitze 19 Uhr (Start 25,5 °C) |
|---|---|---|
| 0 | Außenverschattung + Nachtlüftung (Start 24,5 °C) | ≈ 27,2 °C (statt 30,4 °C) |
| 1 | + Speicherbetrieb B (falls das Wasser ohnehin gebraucht wird) | ≈ 26,1 °C |
| 2 | + Ventilator (20–30 W) für gefühlte Kühlung | gefühlt −1 bis −2 K |

## 10. Stückliste (Voll-Ausbau, ca.-Preise)

| Teil | € |
|---|---|
| 2 × Kfz-Heizungswärmetauscher neu, ca. 200 × 200 × 32 mm (Kupfer/Messing oder Alu) | 70 |
| Gehäuse: Siebdruck/Sperrholz 10 mm, Schaumstoffdichtband, Schrauben | 25 |
| Kondensatwanne (Backblech/Fliesenwanne) mit Ablaufstutzen | 10 |
| 2 × Gehäuselüfter 200 mm, 12 V (Datenblatt: ≤ 2 W bei 90 m³/h) | 30 |
| Steckernetzteil 12 V/1 A + Drehzahlsteller | 15 |
| Kopfbehälter: Eimer 10–12 l mit Deckel, WC-Füllventil seitlich, 2 Durchführungen | 35 |
| Geräteventil mit Rückflussverhinderer EA, Durchflussbegrenzer 3 l/min, Zulaufschlauch 2 m | 30 |
| Dosierventil (Thermostatventil-Unterteil) + Schmutzsieb | 25 |
| Schlauch 16 mm ≈ 6 m, Tüllen, Schellen, 2 Entlüfter | 35 |
| Sammelkübel 40 l mit Überlaufdurchführung | 15 |
| Überlaufschlauch DN 32, 3 m, mit Schellen | 10 |
| 2 Wassermelder | 20 |
| 2 Thermometer, Hygrometer, Messbecher 1 l | 20 |
| Rohrdämmung 13 mm, Kleinteile | 10 |
| Konsole/Regalbrett für den Kopfbehälter (falls keines vorhanden) | 15 |
| **Summe** | **≈ 365** |

- **Sparstufe** (1 Kern, 1 Lüfter, vorhandener Eimer, 1 Melder): ≈ 225 €, mit Vorhandenem ≈ 170 €.
- **Variante B** ersetzt den Kopfbehälter durch Tonne (≈ 15 €) und Pumpe (≈ 15 €) und spart den Überlaufschlauch.
- **Solarmodul** (optional): ≈ 25 €.

## 11. Bauanleitung

1. **Vorklärung (Abschnitt 0):** Versorger, Vermieter, Wasserstopp, Haftpflicht. Zulauftemperatur am Hahn messen.
2. **Standort:** Zimmer neben Bad oder Küche, Innenwand, nicht in der Sonne. Hahn und Abfluss ≤ 4 m entfernt.
3. **Kerne prüfen:** Dichtheit mit Leitungswasser, ≥ 30 min durchspülen, bis das Wasser klar ist (Abwasser in den Abfluss). 24 h gefüllt stehen lassen und auf Nässe prüfen.
4. **Gehäuse bauen:** Kerne übereinander einsetzen, jeweils mit eigenem Lüfterstutzen. Luft geht durch den Kern, nicht daran vorbei (Dichtband). Tropfwanne unter Kern 1.
5. **Kopfbehälter bauen:**
   - Mit Stufenbohrer Bodenauslauf und Überlauf (≈ 4 cm unter dem Rand) bohren, Durchführungen einsetzen.
   - Füllventil seitlich montieren, Düse ≥ 20 mm über der Überlaufunterkante. Der Schwimmer schaltet ≥ 2 cm darunter ab.
   - Dämmhülle und Deckel mit Schlitz für den Zulaufschlauch.
6. **Hydraulik:** Behälterauslauf → Sieb → Dosierventil → Schlauch zu Kern 1 unten. Kern 1 oben → Kern 2 unten. Kern 2 oben (Entlüfter am Hochpunkt) → Schlauchende 3 cm über den Trichter → Fallschlauch in den Kübel. Alles Kalte dämmen. **Pegel ≥ 0,3 m über dem Trichter.**
7. **Überlauf:** Überlaufschlauch vom Behälter und vom Kübel zum Abfluss, fest geklemmt, Gefälle ≥ 2 %, kein Knick.
8. **Hahn:** Wandventil → Geräteventil EA (Durchflussbegrenzer drin) → Zulaufschlauch → Füllventil.
9. **Erstbefüllung:** Wandventil langsam öffnen, Entlüfter öffnen, bis Wasser kommt. 1 h auf Dichtheit prüfen, Wassermelder aufstellen.
10. **Dosieren:**
    - Ziel 0,33 l/min: Messbecher am Fallrohr, 1 l in etwa 3 min.
    - Zweite Regelgröße ist die **Ablauftemperatur** von 24–26 °C bei 27 °C Raum. Darüber mehr Wasser, darunter weniger.
    - Nach 2 h nachmessen.
11. **Betrieb:**
    - Morgens Wandhahn öffnen, erst 2–3 l ablaufen lassen, dann anschließen.
    - Zulauftemperatur nach 30 min und 3 h prüfen.
    - Abends Wandhahn zu, Behälter und Kern leerlaufen lassen (Abschnitt 7).
    - Wöchentlich Füllventil, Sieb, Wanne und Entlüfter prüfen.
12. **Nachmessen:** Q = 1,163 × l/h × (T_aus − T_ein).
    - Erwartung bei 20 l/h, Raum 27 °C: ≈ 239 W, das sind 10,3 K Hub.
    - **Bandbreite 175–255 W**, also 7,5–11 K Hub. Liegt der Hub darunter, sind Luftstrom oder Kern schwächer als geplant (Lüfter höher drehen, Kern prüfen).
    - **Sparstufe (1 Kern, 10 l/h):** Erwartung 122 W, Austritt ≈ 25,5 °C. Liegt der Hub bei nur 7 K oder weniger (< 80 W), bleibt die Erweiterung auf 2 Kerne trotzdem sinnvoll, bringt aber weniger als gerechnet.

## 12. Grenzen, ehrlich

- **Die Kernzahl UA ist eine Abschätzung** (31–53 W/K aus Katalogwerten, theoretisch ≈ 90 W/K). Die Leistung ist wegen der zwei Stufen robust (175–255 W), sollte aber nach dem Aufbau gemessen werden.
- **Wasser ist ein dünner Kälteträger.** 84 l/kWh, physikalisch mindestens 72 l/kWh. 100 l/Tag sind nur für 1,2–1,4 kWh möglich.
- **Wirtschaftlich** ist es nur eingeschränkt: 0,2–0,4 €/kWh gegen etwa 0,14 €/kWh beim Klimagerät. Es lohnt sich für wenige Hitzetage oder mit Garten.
- **Allein reicht es nicht für ≤ 26 °C** (28,3 °C). Erst mit Außenverschattung und Nachtlüftung kommt man auf 25,4–26,1 °C. Im Dachgeschoss bleibt es über 30 °C.
- **Zulauftemperatur ist die Hauptunsicherheit.** Ab 18 °C lohnt es kaum, ab 20 °C nicht.
- **Die Weiterverwendung ist begrenzt:** Ohne Garten lassen sich nur 60–120 l/Tag nutzen, der Rest geht in den Abfluss.
- **Größte Alltagsrisiken:** hängendes Füllventil, geknickter Überlaufschlauch, verstopftes Sieb. Dagegen helfen Durchflussbegrenzer, Überlauf, Wassermelder und Sichtprüfung.
- **Bei Verbot des Versorgers, Wasserstopp-System, Trockenheitsverbot oder Zulauf ≥ 20 °C** bleibt das Gerät aus.

## 13. Energiebilanz

Bilanz als **Mittel der Betriebszeit 9–19 Uhr**, Auslegungsfall (2 Kerne, 20 l/h, Zulauf 15 °C, nur Gerät, ohne Außenverschattung).

- Die Raumluft liegt im Mittel bei 27,7 °C ohne und 26,7 °C mit Gerät.
- Das Wasser tritt im Mittel mit 25,0 °C aus, die mittlere Wassertemperatur im Kühler ist (15 + 25,0)/2 = 20,0 °C.
- Wasserseitig werden 233 W abgeführt. Davon stammen 229 W netto aus dem Raum und 4 W aus der Lüfterwärme (Strom).
- Leitungswasserverbrauch: 200 l/Tag. In die Luft verdunstet nichts, Kondensat fällt kaum an.

```json
{
  "knoten": {
    "Wohnung": {"T_C": 26.7, "rolle": "umgebung"},
    "Kuehler": {"T_C": 20.0, "rolle": "komponente"},
    "Netzstrom": {"T_C": 20.0, "rolle": "umgebung"},
    "Leitungswasser": {"T_C": 15, "rolle": "umgebung"}
  },
  "stroeme": [
    {"von": "Wohnung", "nach": "Kuehler", "W": 229, "art": "waerme"},
    {"von": "Netzstrom", "nach": "Kuehler", "W": 4, "art": "arbeit"},
    {"von": "Kuehler", "nach": "Leitungswasser", "W": 233, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Wohnung", "T_ein_C": 27.7, "T_aus_C": 26.7, "kuehlleistung_W": 229},
  "luft_T_C": 30,
  "wasserverlust_l_pro_tag": 0
}
```