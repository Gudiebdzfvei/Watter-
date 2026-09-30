# Wasserleitung kühlen im geschlossenen Wasserkreislauf: solar getriebener Adsorptionskühler ohne Strom (Runde 2)

## 1. Kurzfassung

**Der reine Verdunster-Kondensator-Loop kühlt nicht.** Dampf strömt nur zum niedrigeren Druck, also zur kälteren Stelle. Der Kondensator müsste kälter sein als die Leitung. Bei 32 °C und 40 % r. F. liegt die Feuchtkugeltemperatur bei etwa 22 °C. Ein offener nasser Lappen bringt 24 °C-Wasser also nur auf etwa 22–23 °C, und das Wasser geht dabei verloren. Deshalb wechsle ich nicht den Ansatz der letzten Runde (Sorption), sondern baue ihn physikalisch sauber und baubar neu auf.

**Der Kreislauf ist eine solar getriebene Wärmepumpe mit drei Temperaturen. Arbeitsmittel ist ausschließlich Wasser, Sorbens ist Silikagel:**

- **Nachts (Kälteproduktion):** Wasser verdampft bei etwa 3–9 °C und 0,8–1,1 kPa in Rohren, die im kalten Wasserbad liegen. Das Silikagel bindet den Dampf, er kondensiert also nicht am Verdampfer. Die Bindungswärme geht an die Nachtluft (21 °C).
- **Tags (Regeneration):** Die Sonne heizt das Silikagel im verglasten Kollektor auf 100–115 °C. Der Dampf wird ausgetrieben, kondensiert im verrippten Kondensator bei etwa 42 °C und gibt die Wärme an die Außenluft ab. Das Kondensat läuft per Schwerkraft durch einen Siphon zurück zum Verdampfer.
- **Antrieb:** Sonnenwärme mit hoher Temperatur, Tag/Nacht-Wechsel, Schwerkraft, Kamineffekt und wachsgesteuerte Klappen. Strom: **0 W**. Wasserverlust: **0**.

**Wo bleibt die Kondensationswärme?** In der Außenluft, am Kondensator bei etwa 42 °C. Das ist wärmer als die Luft (32 °C), also fließt sie von selbst dorthin. Die Leitung bleibt kalt, weil Verdampfung und Kondensation zeitlich und räumlich getrennt auf zwei Temperaturniveaus (5 °C und 42 °C) stattfinden. Das Silikagel puffert den Dampf dazwischen. Die Sonnenwärme hebt die Wärme von 5 °C auf 42 °C, so wie ein Kompressor es täte. Ohne Sonne gäbe es netto null Kühlung.

**Ergebnis für den Auslegungsfall (Klartag, konservativ gerechnet):**

| | Balkon | Fassade |
|---|---|---|
| Kollektorfläche (Apertur) | 2,55 m² | 10,2 m² (4 Module) |
| Silikagel | 50 kg | 200 kg |
| Nutzkälte ans Leitungswasser (netto) | 0,90 kWh/Tag (Mittel 37 W) | 4,4 kWh/Tag (Mittel 184 W) |
| Menge bei 24 °C → im Mittel 11 °C | ca. 59 L/Tag | ca. 290 L/Tag |
| Auslauftemperatur | 8–15 °C, Mittel 11 °C (siehe 5.5) | ebenso, 600-L-Speicher |
| Strom / Wasserverlust | 0 W / 0 L | 0 W / 0 L |
| Trübwetter | halbe Menge bei hellem Dunst, ca. 0 bei bedecktem Himmel (siehe 6) | |

Die Zahlen sind gegenüber Runde 1 (87 L) bewusst niedriger. Grund sind eine realistische Isotherme, ein realistischer COP und die reale Auslauftemperatur.

---

## 2. Warum das Prinzip funktioniert (Energiepfad)

```
  TAG (Sonne, ca. 10 Std.)                   NACHT (ca. 8-9 Std. nutzbar)

  Sonne 800 W/m2                              Verdampfer 3-9 C, ca. 1 kPa
     |  (Strahlung)                             Wasser verdampft, Waerme
     v                                          kommt aus dem kalten Bad
  Kollektor 80-115 C                              | Dampf (nur durch Klappe R2)
     |  Waerme                                    v
     v                                          Adsorber (Silikagel) ca. 33 C
  Adsorber: Gel gibt Dampf ab                     bindet Dampf
     | Dampf (Klappe R1)                          Bindungswaerme --> Nachtluft 21 C
     v
  Kondensator ca. 42 C  --> Waerme an Tagluft 32 C
     | Kondensat, Schwerkraft, Siphon
     v
  Verdampfer (wartet auf die Nacht)
```

Energiebilanz je Zyklus (Balkon): Sonnenwärme 3,83 kWh plus Kälte aus dem Bad 1,14 kWh ergeben 4,97 kWh Abwärme. Davon gehen etwa 3,9 kWh nachts vom Adsorber an die Luft und etwa 1,1 kWh tags vom Kondensator an die Luft.

**Zweiter Hauptsatz:** Es sind drei Temperaturen im Spiel: Antrieb 100–115 °C, Wärmeabgabe 33–42 °C, Kälte 5 °C. Mit T_m ≈ 37 °C, also 310 K, ist der Carnot-Grenzwert COP = T_e/(T_m−T_e) · (T_h−T_m)/T_h ≈ 278/32 · 53/363 ≈ 1,27. Realisiert wird ein COP von 0,30–0,35, das sind 25 % von Carnot. Für eine einbettige, intermittierende Anlage ohne Wärmerückgewinnung ist das typisch. Die 46 % aus Runde 1 waren zu hoch.

**Isolation der Verdampferseite:** Ohne Klappe würde der heiße Adsorber tags in den kalten Verdampfer desorbieren. Er würde also das Bad heizen statt den Kondensator zu speisen. Deshalb braucht der Verdampferzweig eine Dampfdiode (R2).

---

## 3. Aufbau Balkon

**Aufstellung:** nach Süden (±30°), unverschattet von 9 bis 16 Uhr, Balkonlast mindestens 2 kN/m². Gewicht gesamt ca. 450 kg, das sind ca. 1,5 kN/m² auf 3 m².

```
  Seitenansicht (Sued = links, Fassade/Wand = rechts)

   Sonne \   \   \                    Kamin-Aufsatz (Rueckkanal)
          \   \   \                        | Abluft nachts
   Bruestung        ______________________|__    ~2,4 m
     |             /  Doppelglas 40 Grad  /|
     |            /  20 Rohre Edelstahl  / |    KONDENSATOR
     |           /   + Silikagel 50 kg  /  |    (Rippen, Schatten
     |          /____________________ /    |     unter Kollektor-
     |          Klappen unten (Zuluft)     |     Hochpunkt, 1,3-2,1 m)
     |                 R2 [Folie]  R1      |        | Kondensat
     |                   |___Dampf___|_____|        v
     |                   |                      U-Siphon im Bad
     |     +-------------+--------------+         (Schenkel 0,85 m)
     |     | BAD 160 L, Tank 0,45 x 1,0 m|
     |     |  Verdampferrohre (Vakuum)   |   100 mm Daemmung
     |     |  Trinkwasser-Wendel 24 m    |   Trinkwasser: 24 C oben rein,
     |     +-----------------------------+   kalt unten raus (Gegenstrom)
   Grundflaeche ca. 1,0 x 3,0 m
```

### 3.1 Bauteile und Werkstoffe

- **Adsorber (Rohrbündel statt Flachbox):**
  - 20 Rohre Edelstahl 1.4404, Ø 42,4 × 1,2 mm, 2,8 m lang, mit je 2,45 kg Silikagel (RD-Typ, 2–3 mm Körnung).
  - Im Bett steckt ein Kupfer-Sternprofil, das den Wärmeweg auf ca. 10 mm verkürzt.
  - An den Enden liegen zwei Sammler DN50, dazu eine Dampf-Sammelleitung DN80. Alles ist geschweißt.
  - **Druckfestigkeit:** Für ein Rundrohr gilt p_krit ≈ 2E/(1−ν²)·(t/D)³. Mit t/D = 1,2/42,4 ergibt das etwa 10 MPa, gegenüber 0,1 MPa Außendruck. Damit ist die Sicherheit über 50, und es gibt keine Flachbleche unter Vakuum.
  - Auf den Rohren sitzt außen ein Alu-Absorberblech mit selektiver Beschichtung. Alu liegt nur außerhalb des Vakuums, es gibt also keine Wasserstoffbildung im System.
- **Kollektorkasten:**
  - Doppelverglasung (a₁ ≈ 3 W/m²K, a₂ ≈ 0,012 W/m²K², η₀ ≈ 0,72), Dämmung auf der Rückseite.
  - Unten liegt eine Zuluftklappe, oben führt ein Rückkanal zum Kamin-Aufsatz. Die Kaminhöhe ab Zuluft beträgt ca. 1,9 m.
  - Im Kasten sitzen rückseitig Alu-Rippen auf den Rohren (Luftseite UA ≈ 45 W/K).
- **Klappensteuerung ohne Strom (zwei Wachs-Dehnstoffelemente, ODER-verknüpft):**
  - Element 1 sitzt an der Innenseite des Deckglases. Es schließt die Klappen bei mehr als 40 °C und öffnet sie bei weniger als 35 °C (Feder). Das heißt: Sonne = zu, Abend = auf.
  - Element 2 sitzt am Adsorbersammler und öffnet die Klappen bei mehr als 115 °C. Das ist der Überhitzungsschutz.
- **Verdampfer im Bad:** Tank aus Edelstahl, atmosphärisch, 160 L.
  - 12 Rohre DN80 (88,9 × 2 mm) horizontal, Vakuum innen. Auch sie sind rund und daher vakuumfest.
  - Innen liegt Sinterfilz mit einem flachen Wasserfilm von ca. 1 cm. Die Fläche von ca. 4 m² ergibt ein UA von über 1000 W/K, das reicht für Spitzen von 150 W bei ca. 0,15 K Differenz.
  - Trinkwasser fließt in einer Edelstahl-Wellrohrwendel (24 m DN20, ca. 2 m², UA ≈ 400 W/K) im Bad. Es gibt keine Verbindung zum Vakuumsystem, und das Bad bleibt unter 14 °C.
- **Kondensator:** verrippte Rohre, Rippenfläche ca. 8 m², UA ≈ 45 W/K bei natürlicher Konvektion und Kamin. Er liegt im Schatten unter dem Kollektor-Hochpunkt, mit 15 cm Abstand zur Wand.
- **Siphon im Kondensatweg:**
  - Der maximale Druckunterschied tags beträgt 8,2 − 0,9 ≈ 7,3 kPa, das entspricht 0,74 m Wassersäule.
  - Die Schenkel sind 0,85 m tief. Deshalb ist der Tank 1,0 m hoch, und der Siphon liegt im Bad.
  - So entsteht keine Wärmebrücke zur Außenluft. Das Siphonwasser verdunstet nachts nicht auf Kosten der Umgebung, sondern kühlt zusammen mit dem Bad.
- **Salzlösungen:** keine. Feste Sorbentien brauchen keine Pumpe und haben kein Kristallisations- und Korrosionsproblem.

### 3.2 Dampfdioden (die kritischste Stelle)

- **Funktionsnotwendig ist nur R2** (Verdampfer → Adsorber). R1 (Adsorber → Kondensator) ist Komfort, denn nachts ist der Kondensator trocken. Ohne R1 würde nur etwas Restwasser im Siphonschenkel verdunsten.
- **Bauart:** Folienklappe aus PTFE, 0,1 mm, auf einem polierten, waagerechten Edelstahl-Ringsitz (DN100). Der Flusspfad läuft aufwärts. Die Öffnungsdruckdifferenz beträgt ρ_A·g ≈ 0,22 kg/m² · 9,81 ≈ **2 Pa**. Das entspricht 0,03 K Verdampfertemperatur und ist vernachlässigbar.
- **Dichtheit im geschlossenen Zustand:** Die Folie wird mit bis zu 7 kPa auf den Sitz gedrückt (ca. 55 N bei DN100). Zulässig ist eine Rückleckage von ca. 10 % des Dampfstroms. Der Dampfstrom tags beträgt ca. 0,1 g/s, die zulässige Leckage also ca. 0,01 g/s. Das ist mit einer geläppten Dichtfläche gut erreichbar, denn die Dichtheitsforderung betrifft Wasserdampf und nicht Luft.
- **Redundanz:** R2 als Doppelklappe in Reihe. Dazu kommt der Frostwächter (siehe 7).
- **Risiko bleibt:** Kondensatfilm, der die Folie klebt, und Verschmutzung. Das ist die wichtigste Prototypfrage.

### 3.3 Nichtkondensierbare Gase

- Alle Verbindungen sind geschweißt oder metallgedichtet. Anforderung: He-Leckrate ≤ 10⁻⁸ mbar·L/s, das sind 10⁻⁶ Pa·L/s. In 10 Jahren ergibt das ca. 315 Pa·L.
- Diese Menge wird in einem **Gassammler** (5 L, am oberen Kondensatorende) abgelegt. Das entspricht ca. 63 Pa, also weniger als 1 % des Dampfdrucks und ohne Wirkung.
- Zur Wartung gibt es einen Service-Stutzen. Alle 2–3 Jahre wird mit einer Handpumpe oder einem Servicegerät nachevakuiert. Das ist Wartung und kein Betriebsstrom.
- Das Gel wird vor dem Verschließen bei 150 °C unter Vakuum ausgeheizt.
- Stahl und Edelstahl 316L erzeugen in reinem Wasser praktisch keinen Wasserstoff. Als Kontrolle dienen zwei Thermometer am Kondensator: Ein kalter Bereich am Ende zeigt Gas an.

### 3.4 Sicherheit

- **Stagnation:** Ein Klartag bei ausgefallenem Verbraucher erzeugt im Kollektor bis ca. 130 °C. Mit fast trockenem Gel (x ≈ 0,02) liegt der Dampfdruck bei unter 20 kPa. Rohre und Sammler sind für 1 MPa ausgelegt. Zusätzlich sitzt ein Sicherheitsventil bei 150 kPa abs. Im Normalbetrieb wird es nie erreicht.
- Berührungsschutz am Kollektor (bis 115 °C), Glasbruchsicherheit durch Verbundglas.

---

## 4. Rechnung Balkon (Klartag)

### 4.1 Isotherme und Δx

Richtwerte für Silikagel RD (25–35 °C):

- **Adsorption nachts:** T_ads ≈ 33 °C, T_verd ≈ 5–9 °C, p ≈ 0,85–1,15 kPa, p_s(33 °C) = 5,0 kPa, also r. F. ≈ 17–23 %. Beladung x_ads ≈ 0,08.
- **Regeneration tags:** T_kond ≈ 42 °C, p = 8,2 kPa. Bei T_ads,end = 100 °C ist p_s = 101 kPa, r. F. ≈ 8 %, Beladung x_des ≈ 0,045. Bei nur 90 °C wären es 12 % und x ≈ 0,055.
- **Δx = 0,08 − 0,045 ≈ 0,035** (Auslegung). Die Runde-1-Annahme von 0,08 wird damit deutlich unterschritten, wie vom Gutachter gefordert.

Mit 50 kg Gel ergeben sich **1,75 kg Wasser pro Tag**.

### 4.2 Wärmebedarf der Regeneration

- Fühlbare Wärme: Wärmekapazität des Adsorbers ca. 100 kJ/K (Gel 45, Wasser 12, Rohre 30, Rippen/Sammler 13), Erwärmung 25 → 105 °C, ΔT = 80 K, ergibt **8,0 MJ**.
- Desorption und Bindung: 1,75 kg · 2,8 MJ/kg = **4,9 MJ**.
- Zuschlag für Sammler und Dampfleitung: **0,9 MJ**.
- Summe: **13,8 MJ = 3,83 kWh** (Mittel 160 W über 24 h).

### 4.3 Kälte

- Verdampfung: 1,75 kg · 2,49 MJ/kg = 4,36 MJ = 1,21 kWh.
- Kondensat kommt mit 42 °C zurück: 1,75 · 4,19 · 36 = 0,26 MJ = 0,07 kWh.
- Speicherverluste (100 mm Dämmung, 1,7 m², ΔT ≈ 17 K): 10 W = 0,24 kWh.
- **Nutzkälte ans Leitungswasser: 1,21 − 0,07 − 0,24 = 0,90 kWh/Tag (37 W).** Die Werte sind gerundet.
- **COP_th** = 4,36/13,8 = 0,32 (brutto) bzw. 0,30 (netto Verdampfer). Das liegt im typischen Bereich 0,25–0,40.
- **Solar-COP** = 1,14/15,5 kWh Einstrahlung ≈ 0,074.

### 4.4 Solarseite (der Kollektor reicht)

- Einstrahlung auf 40° geneigter Fläche: ca. 6,2 kWh/m²·Tag (Spitze 800 W/m²), auf 2,55 m² ergibt das 15,8 kWh. Ich rechne mit 15,5 kWh.
- Stundenrechnung (Kollektor η₀ = 0,72, a₁ = 3, a₂ = 0,012, C = 100 kJ/K):
  - 08 Uhr: 35 °C.
  - 09 Uhr: 52 °C.
  - 10 Uhr: Beginn der Desorption bei 62–65 °C.
  - 12 Uhr: 85 °C.
  - 13–14 Uhr: 100 °C, Desorptionsende.
  - Danach steigt die Temperatur bis maximal 115 °C, dann öffnet Element 2.
- Der Kollektor liefert damit etwa 30 % mehr Wärme als nötig. Dieser Überschuss ist Absicht: Er sichert die Regeneration an Dunsttagen (siehe 6).

### 4.5 Auslauftemperatur und Menge (konsistent gerechnet)

Für die Wendel gilt UA = 400 W/K. Das Bad ist ein Reservoir, also ε = 1 − exp(−UA/(ṁ·c_p)):

| Zapfrate | ṁ·c_p | NTU | ε |
|---|---|---|---|
| 3 L/min | 209 W/K | 1,9 | 0,85 |
| 5 L/min | 348 W/K | 1,15 | 0,68 |
| 8 L/min | 557 W/K | 0,72 | 0,51 |

Auslauf T_aus = 24 − ε·(24 − T_bad):

| Bad | 3 L/min | 5 L/min |
|---|---|---|
| 5 °C (morgens) | 7,9 °C | 11,1 °C |
| 8 °C | 10,4 °C | 13,1 °C |
| 11,5 °C (abends) | 13,4 °C | 15,5 °C |

- Das Bad schwingt täglich um ca. 6,5 K (5 → 11,5 °C). Das passt zur Tagesproduktion von 1,14 kWh bei 174 Wh/K Badkapazität.
- Bei sparsamer Zapfung (3 L/min) liegt der Tagesmittelwert bei **ca. 11 °C**, bei 5 L/min bei 13–14 °C.
- Menge: 0,90 kWh/Tag / (1,163 Wh/(kg·K) · 13 K) = **59 L/Tag**. Menge und Temperatur sind jetzt konsistent.

### 4.6 Nachtzeitachse und Wärmeabfuhr

| Zeit | Vorgang |
|---|---|
| 07:30 | R2 schließt (p_Adsorber > p_Verdampfer) |
| ca. 09:30 | Desorption beginnt bei ca. 62–65 °C, Dampf zum Kondensator |
| 14:00 | Desorption abgeschlossen, Bett 100 °C bis 115 °C, Klappen zu |
| 14:00–19:30 | Abkühlung über das Deckglas (ca. 400 W bei ΔT 60 K) |
| ca. 19:30 | Wachselement öffnet die Klappen (Glas unter 35 °C) |
| bis 22:00 | Bett fällt auf ca. 40 °C |
| 22:00–06:30 | Adsorption aktiv, T_ads 35 → 31 °C, nutzbares Fenster ca. 8,5 h |

Die Wärmeabfuhr nachts beträgt zu Beginn ca. 300–350 W. Mit der Kaminhöhe von 1,9 m ergibt sich ein Auftrieb von etwa 0,7 Pa, bei ΔT ≈ 10 K also etwa 0,8 m/s im Kanal. Das sind ca. 0,1 m³/s, also eine Wärmekapazität von ca. 120 W/K. Mit UA_Luftseite = 45 W/K ist ε ≈ 0,3, wirksam also ca. 33 W/K. Die Adsorbertemperatur liegt damit ca. 10 K über der Luft, im Mittel 33 °C. Das ist genau die Annahme in 4.1. Ein knappes Ergebnis: Bei wärmeren Nächten sinkt Δx.

### 4.7 Kondensator

Die Desorption bringt ca. 4,2 MJ in ca. 4,5 h, im Mittel 260 W und in der Spitze ca. 380 W. Mit UA = 45 W/K ergibt das ΔT ≈ 8 K, also T_kond ≈ 40 °C bei 32 °C Luft. In Hitzewellen (37 °C) steigt er auf 45 °C und der Ertrag sinkt um ca. 15 %. Wind bis 3 m/s hilft dem Kondensator und schadet dem Kollektor: Die Kollektorverluste steigen um ca. 20 %, der Ertrag sinkt um ca. 10 %.

---

## 5. Fassadenvariante (4 Stockwerke, ca. 12–14 m)

**Prinzip:** vier Balkonmodule übereinander (Sägezahn-Bänder, 45°, je 3,0 × 0,85 m, zusammen 10,2 m²), die an einem gemeinsamen senkrechten Dampfsteigrohr DN150 hängen.

- **Höhe als Teil der Lösung:**
  - Der Kamin hinter den Sägezahn-Bändern ist 10 m hoch und liefert ca. 3,9 Pa Auftrieb (ΔT = 10 K). Das ergibt etwa 1,2 m/s Luftgeschwindigkeit und ca. 1,3 m³/s.
  - Damit reicht die Wärmeabfuhr von ca. 1,3 kW auch mit UA ≈ 300–400 W/K (größere Rippenflächen).
  - Die Adsorbertemperatur liegt nachts im Mittel bei ca. 29 °C, das Δx steigt auf 0,038.
  - Die Kondensatleitung wird zum Fallrohr, der Siphon liegt unten im Speicher.
- **Dampfleitung 12 m:** Der Dampfstrom nachts beträgt ca. 0,25 g/s, mit ρ = 0,0066 kg/m³ also 38 L/s (Spitze ca. 110 L/s). Durch DN150 ergibt das v ≈ 6,5 m/s in der Spitze und einen laminaren Druckabfall von etwa 1 Pa. Das sind ca. 0,015 K und damit gegenüber 65–80 Pa/K vernachlässigbar.
- **Rechnung:**

| Größe | Wert |
|---|---|
| Gel | 200 kg, Δx = 0,038, 7,6 kg Wasser/Tag |
| Verdampfung | 7,6 · 2,49 = 18,9 MJ = 5,26 kWh |
| Kondensat-Abzug | 0,32 kWh |
| Speicherverlust (600 L, 120 mm, 4,5 m²) | 22 W = 0,53 kWh |
| **Netto ans Leitungswasser** | **4,4 kWh/Tag (184 W)** |
| Menge bei 24 → 11 °C | **ca. 290 L/Tag** |
| Wärmebedarf | 58 MJ = 16,2 kWh = 26 % der 63 kWh Einstrahlung |
| COP_th | ca. 0,32 |

  Das ist knapp: Die Anlage braucht 26 % Nutzungsgrad gegenüber 25 % beim Balkon. Ein Reservemodul wäre sinnvoll.
- **Speicher:** 600 L (Schwingung ca. 7 K) im Keller oder Erdgeschoss nahe der Zapfstelle. Die 290 L/Tag decken etwa 3–4 Wohnungen zu je 60–100 L.
- **Tragwerk:** Gel 200 kg, Edelstahl ca. 300 kg, Speicher 600 L, Kollektorkästen und Rahmen ca. 400 kg, gesamt ca. 1,6 t, verteilt auf mehrere Konsolen. Statischer Nachweis nötig.

---

## 6. Wetter und Betrieb (ehrlich)

Die Leistung ist nicht proportional zur Einstrahlung, weil die Desorption eine Schwellentemperatur braucht: Die Desorption beginnt erst bei ca. 62–65 °C, sonst gibt es keinen Dampffluss zum 42 °C-Kondensator (8,2 kPa).

| Wetter | Einstrahlung | Adsorber-Endtemperatur | Δx | Balkon netto |
|---|---|---|---|---|
| Klartag | 6,2 kWh/m²d | 100–115 °C | 0,035 | 59 L/Tag |
| Heller Dunst, Wolkenfelder | ca. 4 kWh/m²d (Spitzen ca. 450 W/m²) | ca. 85 °C | ca. 0,02 | **ca. 25 L/Tag** |
| Bedeckt | ≤ 2 kWh/m²d (< 250 W/m²) | Stagnation ca. 45–65 °C | ≈ 0 | **ca. 0** |

Bei 150 W/m² liegt die Stagnationstemperatur des Doppelglaskollektors bei etwa 50–60 °C, unter der Schwelle. Bei 300 W/m² sind es ca. 80–85 °C. Der Kältespeicher (160 L) puffert etwa einen Tag (ca. 1 kWh pro 6 K). Bei drei Regentagen fällt die Kälte aus. Das ist die größte Schwäche gegenüber einer Stromlösung, und sie ist bei der harten Vorgabe „ohne Strom" nicht zu beheben. Vakuumröhren oder ein Zeolith wären mögliche Verbesserungen für schlechtes Wetter, siehe Punkt 7.

---

## 7. Frost, Wartung, Optionen, Kosten

- **Frostschutz:**
  - Ein Wachsthermostat (wie ein Heizkörperventil, Schließpunkt 3 °C, mit Faltenbalg-Durchführung) sitzt in Reihe zu R2. Es sperrt den Dampfweg, wenn das Bad unter 3 °C fällt. Ohne diesen Schutz würde die Kältemenge nach zwei Tagen ohne Zapfung das Bad unter 0 °C bringen (11,5 °C − 2 · 6,5 K).
  - Im Winter ist die Anlage außer Betrieb: Kollektor abdecken, Trinkwasserwendel entleeren, Bad ablassen. Der Siphon liegt im gedämmten Bad, das Arbeitsmittel bleibt im System.
- **Option Zeolith:** AQSOA/SAPO-34 regeneriert bei 65–80 °C und arbeitet bei Trübwetter besser. Die Isotherme ist hier nicht sicher belegt, ich setze sie deshalb nicht an. Sie ist eine Prototypoption und kostet ein Vielfaches.
- **Kosten (grob):** Balkon ca. 5.000–7.000 € (Einzelstück), Serie ca. 2.500–3.500 €. Fassade ca. 18.000–25.000 €. Wirtschaftlich ist das einer Kompressoranlage unterlegen: 0,9 kWh Kälte kosten dort ca. 0,25 kWh Strom. Der Nutzen liegt in der Stromfreiheit und der Betriebssicherheit ohne Kältemittel.
- **Unsicherheit:** ±30 %. Δx, Kollektorverluste, Klappendichtheit und Wärmeabfuhr nachts müssen am Prototyp gemessen werden.

### Variante B: rein passiv, ohne Sorbens (schwächer, Rückfallebene)

- Das Modell:
  - Ein evakuiertes Wasser-Wärmerohr verbindet die Speicherwendel mit einer nachts zum klaren Himmel abstrahlenden Fläche.
  - Bei 20 °C Luft, Taupunkt 17 °C ergibt Berdahl-Martin eine Himmelstemperatur von ca. 6 °C.
  - Ein Panel bei 15 °C strahlt netto ca. 44 W/m² ab, die Konvektion (h ≈ 3–4 W/m²K mit Windschutzfolie) nimmt 15–20 W/m² wieder auf.
  - Es bleiben ca. **10–20 W/m²**, nicht 20–30.
- Der Ertrag:
  - 3 m² · 8 h · 15 W/m² ergibt etwa 0,36 kWh pro Nacht.
  - Das sind ca. 30 L pro Tag auf ca. 15 °C, also nicht deutlich kälter als Luft.
  - Unter dem Taupunkt kommt Tau auf das Panel. Tagsüber muss es abgedeckt werden.
- Bewertung: robust, aber für Auslauftemperaturen unter 15 °C ungeeignet.

---

## 8. Was gegenüber Runde 1 korrigiert wurde

| Kritik | Korrektur |
|---|---|
| Δx zu optimistisch | Δx = 0,035 aus der Isotherme (x_ads 0,08, x_des 0,045) |
| COP 0,52 zu hoch | COP_th 0,32, 25 % von Carnot |
| Auslauf und Menge widersprüchlich | Wendel-NTU und Tabelle, Mittel 11 °C bei 59 L |
| Trübwetter „proportional" | Schwellentemperatur, Klassentabelle (0–25 L) |
| Nachtwärmeabfuhr knapp | UA-Rechnung, Kamin, reduziertes Fenster von 8,5 h |
| Flachbox implodiert, Alu im Vakuum | Rundrohre (p_krit ca. 10 MPa), Alu nur außen |
| Klappen, Gas, Frost, Überdruck | Folienklappe (2 Pa), Dichtheitsforderung, Gassammler, Frostwächter, Ventil |
| Zahlen uneinheitlich, Luft 32 °C nachts | ein Datensatz, Bilanz mit Tagluft 32 °C und Nachtluft 21 °C |
| Variante B zu optimistisch | 10–20 W/m², 0,36 kWh, 30 L |
| Kosten, Gewicht, Aufstellung fehlten | Abschnitte 3 und 7 |

---

## 9. Energiebilanz (Zyklusmittel über 24 h, Balkon, Klartag)

Es gibt keinen Zustand, in dem Tag- und Nachtvorgang gleichzeitig stationär laufen. Die Bilanz ist deshalb ein 24-h-Mittel. Tagesströme gehen an die Tagluft (32 °C), die Nachtwärme des Adsorbers an die Nachtluft (21 °C). Die Knotentemperaturen sind Zyklusmittel.

| Strom | Leistung |
|---|---|
| Sonne → Kollektor (absorbiert, 0,72 · 15,5 kWh) | 465 W |
| Kollektor → Adsorber | 160 W |
| Kollektor → Tagluft (Verluste) | 305 W |
| Verdampfer → Adsorber (Dampf, 1,75 kg · 2,49 MJ) | 50,4 W |
| Adsorber → Kondensator (Dampf, 1,75 kg · 2,40 MJ) | 48,6 W |
| Adsorber → Nachtluft | 161,8 W |
| Kondensator → Tagluft (**Kondensationswärme**) | 45,5 W |
| Kondensator → Verdampfer (Kondensat, fühlbar) | 3,1 W |
| Speicher → Verdampfer | 47,3 W |
| Leitungswasser → Speicher (**Nutzkälte**) | 37,3 W |
| Tagluft → Speicher (Verlust) | 10,0 W |

Zufuhr 465 + 37,3 + 10 = 512,3 W. Abfuhr an die Luft 305 + 45,5 + 161,8 = 512,3 W.

```json
{
  "knoten": {
    "Sonne": {"T_C": 5500, "rolle": "umgebung"},
    "Luft_Tag": {"T_C": 32, "rolle": "umgebung"},
    "Luft_Nacht": {"T_C": 21, "rolle": "umgebung"},
    "Leitungswasser": {"T_C": 24, "rolle": "umgebung"},
    "Kollektor": {"T_C": 85, "rolle": "komponente"},
    "Adsorber": {"T_C": 60, "rolle": "komponente"},
    "Kondensator": {"T_C": 42, "rolle": "komponente"},
    "Verdampfer": {"T_C": 5, "rolle": "komponente"},
    "Kaeltespeicher": {"T_C": 8, "rolle": "komponente"}
  },
  "stroeme": [
    {"von": "Sonne", "nach": "Kollektor", "W": 465.0, "art": "strahlung"},
    {"von": "Kollektor", "nach": "Adsorber", "W": 160.0, "art": "waerme"},
    {"von": "Kollektor", "nach": "Luft_Tag", "W": 305.0, "art": "waerme"},
    {"von": "Verdampfer", "nach": "Adsorber", "W": 50.4, "art": "stoff"},
    {"von": "Adsorber", "nach": "Kondensator", "W": 48.6, "art": "stoff"},
    {"von": "Adsorber", "nach": "Luft_Nacht", "W": 161.8, "art": "waerme"},
    {"von": "Kondensator", "nach": "Luft_Tag", "W": 45.5, "art": "waerme"},
    {"von": "Kondensator", "nach": "Verdampfer", "W": 3.1, "art": "stoff"},
    {"von": "Kaeltespeicher", "nach": "Verdampfer", "W": 47.3, "art": "waerme"},
    {"von": "Leitungswasser", "nach": "Kaeltespeicher", "W": 37.3, "art": "waerme"},
    {"von": "Luft_Tag", "nach": "Kaeltespeicher", "W": 10.0, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Leitungswasser", "T_ein_C": 24, "T_aus_C": 11, "kuehlleistung_W": 37.3},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```