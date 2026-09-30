# Zimmerkühlung mit Leitungswasser: drei Panelheizkörper als drucklose Durchlaufkühlung

## 1. Kurzfazit

Der Wärmetauscher bleibt: drei in Reihe geschaltete Panelheizkörper, stromlos, nur drinnen. Neu ist der Wasserweg. Die Trinkwasserleitung endet jetzt **vorne** an einem freien Luftspalt, und die Heizkörper laufen **drucklos** im Brauchwasserkreis dahinter. Das löst Rückfluss, Druck, Gebrauchtmaterial und Leckagerisiko an der Wurzel.

Die Leistung der Heizkörper im Kühlbetrieb ist **ungemessen**. Ich setze deshalb nur 75 % des Wertes an, den die Heizkörper-Normformel liefern würde, und zeige, dass das Ergebnis robust ist.

Die Wärmelast ist eine Modellannahme (Abschnitt 6). Die Zahlen gelten für dieses Modell, ±0,3–0,5 K.

| Größe (Zimmer 20 m², Modell C = 1,0 kWh/K) | Zulauf 15 °C | Zulauf 18 °C |
|---|---|---|
| Leistung bei 27 °C Raumluft, 25 l/h | **≈ 228 W** | ≈ 163 W |
| Mittel 9–19 Uhr (Raum steigt von 25,5 auf 28 °C) | 218 W | 159 W |
| Kälte pro Tag (10 h) | 2,2 kWh | 1,6 kWh |
| Wasser pro Tag | 250 l | 250 l |
| Liter pro kWh Kälte | 114 | 157 |
| Wasserkosten (4,5 €/m³) | 1,13 €/Tag ≈ 0,51 €/kWh | ≈ 0,71 €/kWh |
| Strom | 0 W | 0 W |
| Spitze 19 Uhr, nur Gerät (ohne Gerät 30,3 °C) | 28,3 °C (−2,0 K) | 28,8 °C (−1,5 K) |
| Spitze mit Außenverschattung (ohne Gerät 28,0 °C) | **26,1 °C** | **26,7 °C** |
| Mittel 9–19 Uhr mit Außenverschattung + Gerät (ohne alles 27,7 °C) | 25,7 °C | 26,0 °C |

**Ehrlich dazu:**
- Das Ziel „Spitze ≤ 26 °C“ wird bei 15 °C Zulauf nur knapp verfehlt (26,1 °C). Bei 18 °C Zulauf bleibt es bei 26,7 °C. Das Tagesmittel liegt aber bei ≈ 25,7–26,0 °C.
- Die Kälte kostet 0,5–0,7 €/kWh. Ein Klimagerät liegt bei ≈ 0,12–0,20 €/kWh.
- Das Gerät lohnt sich nur, wenn Strom, Lärm und Abluftschlauch nicht infrage kommen und das Wasser weiterverwendet wird. Dann sind es netto ≈ 0,3–0,4 €/kWh.

**Rangfolge der Maßnahmen:**
1. **Nachtlüftung:** gratis, sie liefert den Start von 25,5 °C.
2. **Außenverschattung:** −2,3 K an der Spitze, so viel wie das Wassergerät.
3. **Wassergerät:** weitere −2,0 K. Erst beides zusammen bringt die Spitze an 26 °C.

Draußen wird nichts gebaut. Der Nachthimmel-Strahler (≈ 0,9 kWh/Nacht, ≈ 1.700 €) lohnt hier nicht, und der Balkon ist höchstens Ziel fürs Gießwasser.

## 2. Physik: Was steckt im Liter?

Wasser nimmt 1,163 Wh/(l·K) auf.

**Liter pro kWh = 860 / (T_aus − T_ein)**

Bei 15 → 23 °C sind das ≈ 108 l/kWh. Mehr Fläche macht das Wasser wärmer und spart Liter. Mehr Durchfluss bringt kaum noch etwas. Obergrenze bei 25 l/h und 12 K Spreizung sind 349 W.

| Aufbau (Raum 27 °C, Zulauf 15 °C, Planwert) | Leistung | T_aus | l/kWh |
|---|---|---|---|
| 1 Heizkörper, 12 l/h | 93 W | 21,7 °C | 129 |
| 2 Heizkörper, 16 l/h | 151 W | 23,1 °C | 106 |
| 2 Heizkörper, 25 l/h | 183 W | 21,3 °C | 137 |
| 3 Heizkörper, 18 l/h (Spar) | 189 W | 24,1 °C | 95 |
| **3 Heizkörper, 25 l/h (Auslegung)** | **228 W** | **22,9 °C** | **110** |
| 3 Heizkörper, 35 l/h (Turbo) | 265 W | 21,5 °C | 132 |

- Der Turbo bringt +16 % Leistung für +40 % Wasser.
- Der Spar-Betrieb mit 18 l/h bringt −17 % Leistung für −28 % Wasser.
- **Wasser pro Absenkung:** 1 K Absenkung der Spitze entspricht ≈ 1,1 kWh, also ≈ 120 l bei 15 °C Zulauf und ≈ 170 l bei 18 °C.

## 3. Prinzip und Aufbau: offen, drucklos, Trennung vorne

Das Trinkwasser endet in einer Luftstrecke. Alles dahinter ist Brauchwasser, geführt im freien Gefälle.

```text
 Kaltwasser-Hahn (Waschmaschinen-/Spülmaschinenhahn, nur Kaltwasser)
   │ Gewebeschlauch (Aquastop), ≤ 1 m
 [1] Geräteventil mit Rückflussverhinderer (DVGW)          ┐ Trinkwasserseite,
 [2] Bewässerungsuhr (Batterie): 9–19 Uhr                  │ Totvolumen
 [3] Filter 130 µm                                         │ insgesamt ≈ 0,4 l
 [4] Druckminderer 2 bar                                   │
 [5] Verteilrohr 13 mm, 6 druckkompensierte Tropfer 4 l/h  ┘
   │ Tropfen fallen frei ≥ 30 mm durch Luft
 ══╪══ TRENNSTELLE (freier Auslauf Typ AA, geeignet bis Kat. 5) ══
   ▼
 ┌─────────┐ Eimer 10 l auf Brett, Boden ≥ 0,9 m hoch.
 │ Trichter│ Überlauf 19 mm, 10 cm unter Rand, → Wanne/Dusche/Abfluss
 └────┬────┘ (größer als der größte Zufluss)
      │ Schwerkraft, Schlauch gedämmt 13 mm (15 °C, schwitzt sonst)
      ▼ unten links
 ┌── HK 1  Typ 22, 600×1000 ─────────────────┐ Zulauf unten links,
 │  15 → 18,9 °C   ≈ 113 W                   │ Ablauf oben rechts (diagonal),
 └──────────────────────── oben rechts ──────┘ unten rechts Entleerhahn,
      │ Wellschlauch                            oben links Entlüfter
      ▼ unten links
 ┌── HK 2  18,9 → 21,3 °C  ≈ 70 W ───────────┐
 └──────────────────────── oben rechts ──────┘
      │
      ▼ unten links
 ┌── HK 3  21,3 → 22,9 °C  ≈ 45 W ───────────┐
 └──────────────────────── oben rechts ──────┘
      │
   T-Stück mit offenem Standrohr (Entlüftung, bricht Heberwirkung), Stand ≈ 0,75 m
      │ Schlauch 19 mm, fixiert, endet frei über der Tonne
      ▼
 ┌─ Sammeltonne 120 l mit Hahn (in Wanne/Duschtasse) ─┐
 │  Überlauf-Schlauch → Abfluss                       │
 └──── Kannen: WC, Zierpflanzen, Putzen ──────────────┘

 Kondensatwannen unter HK 1 und HK 2.  Wassermelder unter HK 1 und an der Tonne.
```

**Warum das besser ist als der alte Aufbau:**
- Der Netzdruck endet an den Tropfern. Die Heizkörper sehen nur den Schwerkraftdruck von wenigen Zentimetern Wasser. Es gibt keinen Berstdruck und keine Druckprobe auf 10 bar.
- Bei einem Leck an den Heizkörpern laufen höchstens 25–36 l/h aus (Tropferrate). Der Netzdruck kann dort nicht anliegen.
- Gebrauchte Heizkörper (Inhibitoren, Schlamm, Biofilm) sind kein Risiko für die Trinkwasserinstallation, weil der Luftspalt dazwischen liegt.
- Die Dosierung übernehmen druckkompensierte Tropfer. Sie brauchen kein Nadelventil, das driftet und verstopft.

**Zulauf unten, Ablauf oben:**
- Das passt zur Schichtung: Das kalte Wasser liegt unten, das erwärmte steigt nach oben.
- Die Raumluft fällt an der Heizkörperfläche nach unten. Luft und Wasser laufen also im Gegenstrom, was günstig für die Wärmeübertragung ist (ungemessen).

**Hydraulik:**
- Bei 25 l/h ist die Geschwindigkeit im 15-mm-Schlauch ≈ 4 cm/s. Der Druckverlust ist vernachlässigbar, schon wenige Zentimeter Gefälle reichen.
- Die Schlauchlänge zwischen Eimer und Heizkörpern darf mehrere Meter betragen. Der Eimer mit den Tropfern kann also im Bad am Hahn stehen und die Heizkörper im Wohnraum.
- **Geräusch:** Die Tropfen sollen an der Eimerwand entlanglaufen und nicht frei aufs Wasser oder den Boden fallen.

**Standfläche und Gewicht:**
- Bedarf: ≈ 3,1 m Wandlänge × 0,2 m Tiefe (Heizkörper plus 10 cm Wandabstand), also ≈ 0,6 m² Stellfläche.
- Typ 22 600×1000 wiegt trocken ≈ 30–38 kg und fasst ≈ 11 l. Gefüllt sind das ≈ 40–45 kg je Heizkörper, zusammen **≈ 130 kg**. Das entspricht etwa einem vollen Bücherregal und ist für normale Wohnungsdecken unkritisch.
- Die Tonne mit 120 l steht auf Fliesen in Wanne oder Duschtasse.
- **Platzsparende Variante:** 2 × Typ 33, 600×1000 (≈ gleiche Fläche, 2 m Wand, zusammen ≈ 120 kg). Die Leistung ist in meiner Schätzung ähnlich, aber ungemessen.
- **Kippsicherung:** Die Heizkörper mit einem Gurt verbinden und an einem Wandpunkt fixieren. Kinder nicht an die Heizkörper lassen.

## 4. Wärmeübertragung ohne Strom

**Planwert (Annahme, nicht gemessen):**
- Die Normleistung Typ 22 600×1000 beträgt 1.200 W bei ΔT 50 K. Mit Exponent 1,3 ergibt das Q = 7,46·ΔT^1,3.
- Dieser Exponent stammt aus dem Heizbetrieb. Im Kühlbetrieb mit ΔT = 4–12 K ist die Strahlung kleiner und die Konvektion fällt nach unten, die Wärmeübertragung ist also schwächer.
- Ich setze deshalb **75 % an: Q = 5,6 W/K^1,3 · ΔT^1,3**. ΔT ist Raumluft minus mittlere Wassertemperatur.

| ΔT Raum − mittleres Wasser | 4 K | 6 K | 8 K | 10 K | 12 K |
|---|---|---|---|---|---|
| je Heizkörper, Planwert | 34 W | 58 W | 84 W | 112 W | 142 W |
| je Heizkörper, Normformel | 45 W | 77 W | 111 W | 149 W | 189 W |

**Reihenrechnung (Raum 27 °C, Zulauf 15 °C, 25 l/h, Wasserbilanz geschlossen):**
- HK 1 nimmt 113 W auf (15 → 18,9 °C).
- HK 2 nimmt 70 W auf (→ 21,3 °C).
- HK 3 nimmt 45 W auf (→ 22,9 °C).
- Summe: 29,08 W/K × 7,85 K = **228 W**.

**Leistung in Abhängigkeit von der Raumtemperatur** (25 l/h, Zulauf 15 °C):

| Raum | 25 °C | 27 °C | 28 °C |
|---|---|---|---|
| Leistung | 183 W | 228 W | 249 W |

Das entspricht Q ≈ 228 W + 21,5 W/K · (T_Raum − 27 °C).

**Warum die Zahl robust ist:**
- Das Wasser begrenzt die Leistung, nicht die Fläche. Wenn die Heizkörper nur 55 % statt 75 % leisten, sinkt Q von 228 auf ≈ 200 W, und T_aus fällt von 22,9 auf ≈ 21,9 °C.
- Das Ergebnis liegt also zwischen ≈ 180 und 255 W, je nach Wärmeübertragung und Aufstellung.
- **Die Messung bestätigt es:** Q = 1,163 × V̇[l/h] × (T_aus − T_ein). Beispiel: 25 × 1,163 × 7,9 K = 230 W.

**Reicht natürliche Konvektion?** Ja, ein Lüfter ist nicht nötig. Sie liefert im Planfall 228 W aus ≈ 1,8 m² Frontfläche.

**Strahlung:** Die 17–22 °C kalten Flächen senken zusätzlich die empfundene Temperatur, vermutlich um 0,3–0,5 K. Das ist nicht eingerechnet.

**Kaltluftabfall:** Der Luftabfall vor den Heizkörpern ist spürbar (≈ 0,1–0,2 m/s). Das Bett und der Sitzplatz gehören nicht direkt davor.

**Option mit Lüfter (Schätzung, nicht gemessen):**
- Ein Lüfter ändert nichts am Wasserbedarf pro kWh, er macht nur das Wasser wärmer am Austritt.
- Wenn zwei 140-mm-PC-Lüfter (zusammen 2–3 W, mit Steckernetzteil) oben auf den Heizkörpern nach unten blasen und die Wärmeübertragung dadurch ×1,5 steigt, leisten **2 Heizkörper ≈ 234 W**, also so viel wie 3 Heizkörper ohne Lüfter.
- Der Gewinn wäre ein Heizkörper weniger (−50…100 €, −45 kg, −1 m Wand), bezahlt mit 2–3 W Strom.
- Nur sinnvoll, wenn es nach dem Probebetrieb nötig erscheint. Dann ist der Stromverbrauch klein, aber nicht null.

## 5. Kondensation und Entfeuchtung

Der Taupunkt liegt bei 28 °C/50 % bei 16,7 °C und bei 28 °C/65 % bei 20,4 °C. Die Blechoberfläche liegt ≈ 0,3 K über der Wassertemperatur.

**Berechnung:**
- Der Stoffübergang ist mit Lewis-Zahl 1 gerechnet. Der konvektive Anteil der Wärmeübertragung beträgt 75 %.
- Die latente Wärme **kommt zur sensiblen dazu**. Das Wasser nimmt die Gesamtleistung auf und tritt deshalb wärmer aus. Sie ist nicht Teil einer festen Gesamtleistung.
- Die Austrittstemperatur ist je Fall über die Wasserbilanz neu gerechnet: T_aus = T_ein + Q_gesamt / 29,08 W/K.

| Fall (25 l/h, 3 Heizkörper) | nasse Fläche | sensibel | latent | gesamt | T_aus | Kondensat |
|---|---|---|---|---|---|---|
| 27 °C/50 %, Zulauf 15 °C | praktisch keine | 226 W | ≈ 2 W | 228 W | 22,9 °C | < 0,05 l/Tag |
| 28 °C/50 %, Zulauf 15 °C | Eintrittsende HK 1 | 249 W | ≈ 5 W | ≈ 254 W | 23,7 °C | ≈ 0,1 l/Tag |
| 28 °C/65 % (schwül), Zulauf 15 °C | HK 1 ganz | 217 W | 49 W | 267 W | 24,2 °C | ≈ 0,7 l/Tag |
| 28 °C/50 %, Zulauf 12 °C | HK 1 fast ganz | ≈ 300 W | ≈ 21 W | ≈ 321 W | 23,0 °C | ≈ 0,3 l/Tag |

**Einordnung:**
- Bei Schwüle sinkt die **sensible** Leistung von 249 auf 217 W, die Gesamtleistung steigt von 254 auf 267 W. Die Lufttemperatur wird also etwas weniger gesenkt als bei trockener Luft. Dafür wird die Luft trockener.
- Die Menge ist klein: ≈ 0,7 l/Tag sind gegen einen Luftentfeuchter (≈ 10 l/Tag) wenig. Die Entfeuchtung ist ein kleiner Komfortbonus und kein Haupteffekt. Sie entspricht etwa der Feuchteabgabe einer Person.
- Für die Temperaturbilanz setze ich nur die sensible Leistung an.

**Wohin mit dem Kondensat:**
- Es läuft an den Platten ab und tropft am unteren Rand. Zwei flache Wannen (je ≈ 100 × 30 × 3 cm) unter HK 1 und HK 2 fassen es locker.
- Es ist reines Wasser und darf zum Gießen.
- Die Zulaufschläuche (15 °C) bekommen 13-mm-Dämmung, sonst beschlagen sie. Die Verbindungen zwischen den Heizkörpern haben ≥ 19 °C und bleiben trocken.

## 6. Wärmelast und Raumtemperatur (Modell)

**Annahmen (alle Schätzungen):**
- Zimmer 20 m², 2,5 m hoch, mittleres Geschoss.
- 2 m² Südwest-Fenster mit Innenvorhang.
- Speichermasse C = 1,0 kWh/K (mittelschwer).
- Hülle und Fugen G = 17,6 W/K gegen T_Außen + 1,5 K.
- Person, Laptop und Licht: 110 W.
- Betriebszeit 9–19 Uhr. Die Feuchte von Person und Küche betrifft nur die Luftfeuchte.
- Außentemperatur stündlich von 9 Uhr: 25, 26, 27, 28, 29, 29,5, 30, 30, 29,5, 28,5 °C.
- Sonne durch das Fenster (W) stündlich von 9 Uhr: 150, 200, 250, 300, 350, 400, 450, 450, 420, 330.
- Start 25,5 °C nach Nachtlüftung.
- Außenverschattung nimmt 75 % der Sonne, Innenfolie 40 %.
- Modell: C · dT/dt = Sonne + 110 W + G · (T_Außen + 1,5 K − T) − Q_Gerät(T), mit 1-h-Schritten.
- Für den Fehler des Modells selbst gelten ±0,3–0,5 K. Die Differenzen zwischen den Fällen sind zuverlässiger als die Absolutwerte.

**Raumtemperatur zu Beginn der Stunde (°C):**

| Uhr | nichts | nur Gerät 15 °C | nur Gerät 18 °C | nur Außen | Außen + Gerät 15 °C | Außen + Gerät 18 °C |
|---|---|---|---|---|---|---|
| 9 | 25,5 | 25,5 | 25,5 | 25,5 | 25,5 | 25,5 |
| 11 | 26,1 | 25,9 | 26,1 | 25,9 | 25,5 | 25,7 |
| 13 | 27,0 | 26,5 | 26,8 | 26,4 | 25,6 | 25,9 |
| 15 | 28,1 | 27,3 | 27,7 | 27,2 | 25,9 | 26,3 |
| 17 | 29,3 | 28,1 | 28,6 | 27,8 | 26,1 | 26,6 |
| 19 | **30,3** | **28,3** | **28,8** | **28,0** | **26,1** | **26,7** |

**Energie und Mittelwerte:**
- Das Gerät (15 °C) führt 2,19 kWh ab. Seine Leistung steigt von 196 W um 9 Uhr auf 251 W um 18 Uhr, im Mittel 218 W. Das 24-h-Mittel sind 91 W.
- Mittlere Raumtemperatur 9–19 Uhr: 27,7 °C ohne Gerät, 26,7 °C mit Gerät (−1,0 K).
- Mit Außenverschattung und Gerät sind es 25,7 °C (15 °C Zulauf) bzw. 26,0 °C (18 °C Zulauf).
- Pro abgeführter kWh sinkt die Spitze um ≈ 0,9 K.

**Schwere und leichte Bauweise (Raum um 19 Uhr, Zulauf 15 °C):**

| Speichermasse | nichts | nur Gerät | Absenkung | Außen + Gerät |
|---|---|---|---|---|
| 0,5 kWh/K (Dachgeschoss, Leichtbau) | 34,5 | 30,4 | −4,1 K | 26,7 |
| 1,0 kWh/K | 30,3 | 28,3 | −2,0 K | 26,1 |
| 1,5 kWh/K (Massivbau) | 28,8 | 27,4 | −1,4 K | (nicht gerechnet) |

Im Leichtbau ist die Sonne das eigentliche Problem. Dort kommt die Außenverschattung zuerst. Sie allein bringt 34,5 °C nicht unter 30 °C.

**Empfindlichkeit Zulaufwassertemperatur** (27 °C Raumluft, 25 l/h, Planwert):

| Zulauf | Leistung | T_aus | l/kWh | Spitze, nur Gerät | mit Außenverschattung |
|---|---|---|---|---|---|
| 12 °C | ≈ 300 W (davon ≈ 18 W latent) | ≈ 22,3 °C | ≈ 83 | ≈ 27,7 °C | ≈ 25,6 °C |
| **15 °C** | **228 W** | **22,9 °C** | **110** | **28,3 °C** | **26,1 °C** |
| **18 °C** | **163 W** | **23,6 °C** | **154** | **28,8 °C** | **26,7 °C** |
| 20 °C | 122 W | 24,2 °C | 205 | ≈ 29,1 °C | ≈ 27,0 °C |

Die Werte für 15 und 18 °C sind simuliert, die für 12 und 20 °C interpoliert.

**Laufzeit und Vorkühlung:**
- **Späterer Start (12 statt 9 Uhr):**
  - spart 75 l (175 statt 250 l/Tag);
  - Spitze um 19 Uhr +0,6 K mit Außenverschattung, +0,8 K ohne (28,3 → 29,1 °C).
- **Vorkühlen am frühen Morgen (6–9 Uhr):**
  - bringt nur etwa −0,4 K am Abend (das Wasser kühlt die Masse, die über den Tag wieder warm wird);
  - kostet +75 l;
  - Wasser ist nachts nicht kälter, der Raum ist kühler, also bei ΔT ≈ 9 K etwa 150 l/kWh statt 110. Die Nachtlüftung ist die bessere Vorkühlung.
- **Kältestes Wasser:**
  - Die Zulauftemperatur ist der Hebel: +3 K Zulauf bedeuten −30 % Leistung.
  - Deshalb Zulauftemperatur um 7, 12 und 17 Uhr messen (Kontaktthermometer am Schlauch) und Hahn an der kürzesten, kältesten Leitung wählen.
  - Ist das Wasser morgens ≥ 2 K kälter, lohnt ein früherer Start.
- **Kleine Stellschrauben für die letzten Zehntelgrade:**
  - Nachtlüftung bis 24,5 °C Start: −0,7 K.
  - Laptop und Licht aus (−50 W): −0,3 K.
  - Turbo (9 Tropfer) 14–19 Uhr: −0,2 K für +50 l.

## 7. Sicherer Trinkwasseranschluss

1. **Nur Kaltwasser-Abgang, nur Schlauchanschluss.** Geeignet ist ein Waschmaschinen-/Spülmaschinenhahn mit freiem Abgang. Kein Eingriff in fest verlegte Leitungen. Das ist wie bei einer Waschmaschine.
2. **Rückfluss:** Der **freie Auslauf Typ AA** (Tropfer ≥ 30 mm über der Überlaufkante des Eimers) trennt vollständig und gilt bis Flüssigkeitskategorie 5. Er schützt damit auch vor Kategorie 3 (Heizungswasser, Biofilm), die das Gebrauchtmaterial mitbringen kann. Ein Systemtrenner ist **nicht** nötig.
   Zusätzlich sitzt direkt am Hahn ein Geräteventil mit Rückflussverhinderer (DVGW). Es ist der zweite Schutz.
3. **Jährlich vor der Saison:** Rückflussverhinderer prüfen (Sicht- und Funktionsprobe, Schlauchseite drucklos, darf nicht nachlaufen) oder ein neues Ventil (≈ 15 €) einsetzen.
4. **Tauchfall:**
   - Der Zulauf endet nur in Luft, nie im Wasser: Tropfer ≥ 30 mm über dem Überlauf, Schläuche am Eimerrand fixiert, nie auf dem Eimerboden.
   - Der Überlauf (19 mm, freies Gefälle) ist größer als der größte Zufluss.
   - Der Ablaufschlauch hängt frei über der Tonne.
   - Wassermelder stehen unter HK 1 und an der Tonne.
5. **Stagnation und Legionellen:**
   - Die Trinkwasserseite hat nur ≈ 0,4 l Totvolumen. Sie wird täglich durchströmt und bleibt ≤ 20 °C.
   - Morgens laufen ≈ 2 l vor, dann startet die Uhr. Bei Abwesenheit Hahn zu.
   - Das Gerät erwärmt die Kaltwasserleitung nicht, weil das erwärmte Wasser nie zurückfließt. Der Dauerfluss frischt die Stichleitung eher auf.
   - Die Brauchwasserseite bleibt ≤ 25 °C und wird nicht versprüht. Kein Duschen, kein Vernebeln, kein Trinken.
   - Länger als 3 Tage aus: Heizkörper entleeren, vor dem Neustart 10 min spülen.
6. **Kein Totstrang:**
   - Die Geräteleitung ist nur ein Schlauch am bestehenden Hahn, kein neues T-Stück in der festen Installation.
   - Ein Doppel-Eckventil nur, wenn kein freier Abgang existiert (Totraum ≤ 3 cm).
   - Nach der Saison Schlauch abnehmen.
7. **Korrosion:**
   - Stahl im sauerstoffreichen Frischwasser rostet, schätzungsweise ≈ 0,1 mm/Jahr. Bei 1,2–1,5 mm Blech reicht das bei 40 Betriebstagen/Jahr für Jahre.
   - Wechsel nass/trocken verkürzt das Leben. Deshalb während der Saison **nicht täglich entleeren**, sondern gefüllt lassen.
   - Zum Saisonende entleeren und trocknen, Stopfen offen.
   - Gebrauchte Heizkörper: nur ohne Rostdurchbrüche nehmen und vor dem Einbau mit 1–2 bar (Gartenschlauch, Blindstopfen) 30 min auf Dichtheit prüfen.
   - Vor der Erstnutzung ≥ 10 Füllungen (≈ 100 l) durchspülen. Dieses Spülwasser ist auch in den ersten Tagen bräunlich, nicht für Pflanzen.
8. **Leckageschutz im Haus:** Wasserstopp-Systeme können bei Dauerverbrauch ansprechen. Vorher prüfen, ob 25 l/h zulässig sind.
9. **Größtes Alltagsrisiko ist ein Wasserschaden:** Aquastop-Schlauch, Wassermelder, Hahn zu bei Abwesenheit und Zeitbegrenzung per Uhr.

## 8. Wasser, Kosten, Weiterverwendung

| Größe | Wert (Auslegung, 10 h, Zulauf 15 °C) |
|---|---|
| Durchfluss | 6 Tropfer à 4 l/h = 24 l/h → **240–250 l/Tag** |
| Kälte | 2,2 kWh/Tag |
| Wasser + Abwasser (4,5 €/m³) | 1,13 €/Tag |
| Saison 20–30 Hitzetage | 23–34 € |
| Strom | 0 W |
| in die Luft verdunstet | 0 l |

**Weiterverwendung, ehrlich (Wasser ≈ 23 °C, Brauchwasser):**

| Verwendung | l/Tag |
|---|---|
| WC-Spülung (2 Personen, 8–10 Spülungen) mit Kanne | 40–60 |
| Zierpflanzen, Balkon | 20–30 |
| Putzen, Wischen, Handwäsche | 15–20 |
| **Summe** | **≈ 95–110** |

- Der Rest (≈ 140–155 l) läuft über den Überlauf ab: 0,6–0,7 €/Tag netto statt 1,13 €. Das Wasser gehört dann zu ≈ 60 % zum Verlust.
- Mit Garten oder Kleingarten lässt sich mehr nutzen. Dort können ≈ 100 % verwendet werden, die Kosten sinken auf ≈ 0.
- **Nicht** für Gemüse und Obst, weil Gebrauchtheizkörper Reste enthalten können. Für Zierpflanzen ist es nach gründlicher Spülung unkritisch (Rost = Eisen).
- Nicht in Dusche, Waschmaschine oder Trinkwasser. Das verbietet die Kreuzverbindung, und es fehlt der Netzdruck.
- Tonne täglich leeren (Mücken, Keime) und abdecken. Kennzeichnung „Kein Trinkwasser“.

**Varianten ohne Badewanne:** Die Tonne (120 l, mit Hahn) steht in der Dusche oder Badewanne. Ihr Überlaufschlauch hängt über dem Abfluss, und die Duschwanne bleibt für die Dusche nutzbar, wenn man die Tonne kurz beiseitestellt. Ein Waschbecken mit Überlauf geht ebenso.

**Direkt in den WC-Spülkasten:**
- Geht nur bei einem niedrigen Aufputz-Spülkasten, dessen Deckel tiefer liegt als der Wasserstand im Standrohr, sonst läuft es nicht im Gefälle.
- Dann den Eckhahn des Spülkastens zudrehen, und der Kasten wird vom Gerät gefüllt. Der Kastenüberlauf wirkt als Überlauf.
- Die Anlage ist dann Regenwasseranlage mit Nachspeisung (freier Auslauf) und muss gekennzeichnet sein.
- Bei Unterputzkästen geht das nicht.

**Recht (keine Rechtsberatung):**
- **Vermieter:** Zustimmung einholen. Es werden nur vorhandene Hähne genutzt und nichts gebohrt (Bodenkonsolen). Gewicht und Wasserschaden mit Haftpflicht und Hausrat klären.
- **Wasserversorger/Satzung:** Viele Versorger schließen Durchlaufkühlung mit Trinkwasser aus oder verlangen eine Genehmigung. Vor dem Bau nachfragen.
- **Trockenheit:** Kommunen können Trinkwasser für Kühlzwecke per Allgemeinverfügung verbieten. Dann nicht betreiben.
- **Abrechnung:** Verbrauch und meist auch Abwasser laufen über den Wohnungszähler. Gießwasser wird mitbezahlt. Nur bei Gartenzähler-Regelung wird das Abwasser abgezogen.
- **Anschluss:** Nur Schlauchanschluss am vorhandenen Hahn nach den anerkannten Regeln (Rückflusssicherung), kein Eingriff in fest verlegte Leitungen.

## 9. Speicher oder Dauerdurchfluss?

**Dauerdurchfluss.**
- Ein Speicher am Eingang ist unhygienisch (Stagnation) und braucht eine Pumpe.
- Ein Wasservorrat im Raum (200 l aus 15 °C, Tonnenoberfläche ≈ 1,7 m², UA ≈ 12 W/K) gibt in 10 h nur ≈ 1,1 kWh ab, weil er sich an die Raumluft angleicht. Er liefert im Mittel ≈ 110 W, braucht aber dieselben 200 l und mehr Stellfläche.
- Die Sammeltonne am Ausgang ist kein Kälte­speicher, sie dient nur der Weiterverwendung.

## 10. Ausbaustufen und Stückliste

| Stufe | Inhalt | Leistung (15 °C, 27 °C) | Wasser/Tag | Kosten | Spitzenabsenkung |
|---|---|---|---|---|---|
| **Einstieg** | 1 HK, 3 Tropfer (12 l/h), Eimer statt Tonne | 93 W | 120 l | ≈ 290 € (ohne Uhr 260 €) | ≈ −0,9 K |
| **Basis** | 2 HK, 4 Tropfer (16 l/h) | 151 W | 160 l | ≈ 460 € | ≈ −1,3 K |
| **Voll (Auslegung)** | 3 HK, 6 Tropfer (24 l/h) | ≈ 222–228 W | 240–250 l | ≈ 570 € | −2,0 K |
| Turbo | 3 HK, 9 Tropfer (36 l/h) | ≈ 265 W | 360 l | wie Voll + 3 € | ≈ −2,3 K |

Die Absenkung ist aus der Faustregel ≈ 0,9 K pro kWh (C = 1,0, Zulauf 15 °C) abgeleitet.

**Stückliste Voll (gebrauchte Heizkörper):**

| Teil | € |
|---|---|
| 3 × Panelheizkörper Typ 22, 600×1000, gebraucht (30–70 € je) | 150 |
| 3 Paar Bodenkonsolen | 60 |
| 4 × Wellschlauch ½" (≈ 10 €) + Nippel/Dichtungen | 65 |
| 3 Entlüfter, 3 Entleerhähne, 3 Blindstopfen | 42 |
| T-Stück/Standrohr + Ablaufschlauch 19 mm, 3 m | 16 |
| Eimer 10 l mit 2 Tankdurchführungen (Auslauf + Überlauf) | 20 |
| Sammeltonne 120 l mit Hahn | 35 |
| Trinkwasserseite: Geräteventil mit Rückflussverhinderer 15, Filter 10, Druckminderer 2 bar 15, Aquastop-Gewebeschlauch 12 | 52 |
| Verteilrohr 13 mm, 6 Tropfer 4 l/h, Verbinder | 18 |
| Bewässerungsuhr (Batterie) | 30 |
| Rohrisolierung 13 mm | 8 |
| 2 Kondensatwannen | 16 |
| 2 Wassermelder | 20 |
| 2 Thermometer, 1 Hygrometer | 24 |
| Kippsicherung, Schellen, PTFE-Band | 15 |
| **Summe** | **≈ 570** |

- Mit neuen Heizkörpern (≈ 115 € je) kommen ≈ +195 € dazu, also ≈ 765 €.
- Sparbetrieb: ohne Uhr (−30 €) und ohne Tonne (−35 € bei Eimer und Kanne), zusammen ≈ 505 €.
- Für die Zusatzoption mit Lüfter: 2 PC-Lüfter und Steckernetzteil ≈ 25 €.

## 11. Bauanleitung

1. **Standort:**
   - Innenwand, nicht in der Sonne.
   - Mit 10 cm Wandabstand, 3 m Wand frei. Nicht vor Bett oder Sitzplatz.
   - Nah am Kaltwasserhahn und in der Nähe von Wanne/Dusche für die Tonne.
2. **Heizkörper prüfen:**
   - Dichtheit mit Blindstopfen und 1–2 bar prüfen (30 min).
   - Rostdurchbrüche aussortieren.
   - ≥ 10 Füllungen spülen (in den Abfluss).
   - Pro Heizkörper einsetzen: Zulauf unten links, Ablauf oben rechts, Entleerhahn unten rechts, Entlüfter oben links.
3. **Aufstellen** auf Bodenkonsolen, Kippsicherung, Kondensatwannen unter HK 1 und HK 2.
4. **Verschlauchen:** Wellschlauch von oben rechts (HK 1) nach unten links (HK 2), ebenso von HK 2 nach HK 3.
5. **Ablauf:** Am Ausgang von HK 3 ein T-Stück mit offenem Standrohr (oben ≈ 0,9 m). Der Seitenabgang geht in den 19-mm-Schlauch, frei über der Tonne fixiert.
6. **Eimer** auf ein Brett (Eimerboden ≥ 0,9 m). Auslauf unten → gedämmter Schlauch → HK 1 unten links. Überlauf 10 cm unter dem Rand mit 19-mm-Schlauch zum Abfluss.
7. **Trinkwasserseite:**
   - Reihenfolge am Hahn: Geräteventil mit Rückflussverhinderer → Bewässerungsuhr → Filter → Druckminderer → Aquastop-Schlauch → Verteilrohr.
   - Die Tropfer enden **≥ 30 mm über der Überlaufkante**, die Tropfen laufen an der Eimerwand entlang.
8. **Erstbefüllung:** Heizkörper über den Eimer füllen und an den Entlüftern entlüften. Verschraubungen 30 min beobachten.
9. **Dosieren:**
   - 6 Tropfer à 4 l/h geben ≈ 24 l/h. Am Ablauf mit 1-l-Messbecher und Uhr prüfen (≈ 1 l in 2,5 min).
   - Regelgröße ist **T_aus = 22–24 °C**. Liegt sie über 25 °C, einen Tropfer zusetzen. Liegt sie unter 21 °C, weniger Wasser oder ein Heizkörper mehr Fläche, weil der Wärmetauscher besser ist als geplant.
   - Tropfer jährlich ersetzen (1 € je), Filter reinigen.
10. **Uhr:** Startzeit 9 Uhr, Laufzeit 10 h. An sehr heißen Tagen Turbo (9 Tropfer) ab 14 Uhr.
11. **Messen:** Zulauftemperatur nach 30 min und nach 3 h. Ab 18 °C gilt der Sommer-Realfall, ab 20 °C lohnt der Betrieb nicht mehr. Dann Leistung nachrechnen: Q = 1,163 × V̇ × (T_aus − T_ein).
12. **Tagesroutine:**
    - Morgens ≈ 2 l vorlaufen lassen und aufbewahren.
    - Uhr läuft. Abends Hahn zu, Tonne leeren und abdecken.
    - Wöchentlich Wannen und Eimer reinigen.
13. **Saisonende:** Heizkörper entleeren und trocknen, Schlauch abnehmen, Stopfen offen lagern.

## 12. Grenzen, ehrlich

- **Wasser ist ein dünner Kälteträger:** 110 l/kWh bei 15 °C, 154 l/kWh bei 18 °C. Das kostet 3–5-mal so viel wie ein Klimagerät.
- **Die Heizkörperleistung im Kühlbetrieb ist ungemessen.** Der Planwert steht als Annahme, die Bandbreite ist ≈ 180–255 W. Die Messung nach dem Aufbau klärt es.
- **Die Modellwerte (Sonne, Masse, Hülle) sind Schätzungen.** Das Ziel ≤ 26 °C an der Spitze wird bei 15 °C knapp verfehlt (26,1 °C) und bei 18 °C deutlicher (26,7 °C).
- **Mehr Leistung kostet überproportional Wasser:** +16 % Leistung brauchen +40 % Wasser.
- **Etwa 60 % des Wassers gehen ohne Garten verloren.** Das sind ≈ 0,6–0,7 €/Tag netto.
- **Gewicht und Platz:** ≈ 130 kg und 3 m Wand. Die Stückliste liegt bei ≈ 570 €.
- **Gerät aus** bei Trockenheitsverbot, Zulauf ≥ 20 °C, Wasserstopp-Anlage im Haus oder Verbot durch den Versorger.
- Wer das Gerät nur wenige Tage im Jahr braucht, nimmt besser die Einstiegsstufe. Wer mehr Leistung braucht, nimmt ein Klimagerät.

## 13. Energiebilanz

Die Bilanz gilt als **Mittel der Betriebszeit 9–19 Uhr**, Auslegungsfall Gerät allein ohne Verschattung, Zulauf 15 °C, 25 l/h.

- Die Raumluft liegt im Mittel ohne Gerät bei 27,7 °C und mit Gerät bei 26,7 °C.
- Die Kühlleistung beträgt 218 W (24-h-Mittel ≈ 91 W).
- Das Wasser tritt im Mittel mit ≈ 22,5 °C aus. Die mittlere Wassertemperatur in den Heizkörpern liegt bei ≈ 19,5 °C.
- Der Leitungswasserverbrauch beträgt 250 l/Tag. In die Luft verdunstet nichts (Kondensat < 0,1 l/Tag fällt an).

```json
{
  "knoten": {
    "Wohnung": {"T_C": 26.7, "rolle": "umgebung"},
    "Heizkoerper": {"T_C": 19.5, "rolle": "komponente"},
    "Leitungswasser": {"T_C": 15, "rolle": "umgebung"}
  },
  "stroeme": [
    {"von": "Wohnung", "nach": "Heizkoerper", "W": 218, "art": "waerme"},
    {"von": "Heizkoerper", "nach": "Leitungswasser", "W": 218, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Wohnung", "T_ein_C": 27.7, "T_aus_C": 26.7, "kuehlleistung_W": 218},
  "luft_T_C": 30,
  "wasserverlust_l_pro_tag": 0
}
```