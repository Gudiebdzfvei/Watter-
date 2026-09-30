# Wasserleitung kühlen: geschlossener Verdunstungskreislauf mit Verdichter, Kaltwasserspeicher und Solarstrom

## 1. Kurzantwort

**Das Problem.** Ein geschlossener Kreislauf mit nur einem Druck ist ein Wärmerohr. Er transportiert Wärme, erzeugt aber keine Kälte. Verdampfer und Kondensator haben dieselbe Temperatur, und die Kondensationswärme ist genau die Verdunstungswärme. Ohne Antrieb müsste der Kondensator kälter sein als das Wasser, und das gibt es draußen bei 32 °C nicht.

**Die Lösung.** Der Kreislauf braucht zwei Druckniveaus:
- Ein Verdichter hebt den Dampf auf ~14 bar. Dort kondensiert er erst bei 42 °C, also wärmer als die Luft (32 °C).
- Ein Expansionsventil ersetzt den "Regen" und senkt den Druck des Kondensats wieder ab.
- Das ist eine kleine Kältemaschine. Unten verdunstet ein Fluid an der Wand, oben kondensiert es. Es fehlte nur die Druckpumpe dazwischen.

**Wo bleibt die Kondensationswärme?** Im Kondensator bei 42 °C. Von dort fließt sie ganz normal von warm nach kalt an die 32 °C warme Luft: **924 W**. Das sind 729 W Kälteleistung (Wasser + Speicherverluste + Pumpe) plus 225 W Verdichterarbeit, abzüglich 30 W, die das Verdichtergehäuse direkt an die Luft abgibt. Die Wärme kommt aus dem Wasser (bei ~5,5 °C aufgenommen), und der Verdichter pumpt sie ~37 K bergauf.

**Ergebnis für den Auslegungsfall:**
- 50 l/h gehen von 24 °C auf **12 °C**, das sind 20 K unter Lufttemperatur. Die Kühlleistung beträgt 697 W, der Wasserverlust 0.
- Der Strombedarf beträgt **275 W** (Bandbreite 255–325 W), die Leistungszahl des Gesamtsystems ~2,5. Die mittlere Tagesleistungszahl über 24 h liegt bei ~3,3.
- Für den Strom braucht man **2 PV-Module à 400 Wp** und Netz oder Batterie für die Nacht. Eine stromfreie Lösung gibt es physikalisch nicht (Abschnitt 2).

**Neu gegenüber der letzten Fassung:**
- Ein 150-l-Kaltwasserspeicher trennt Kältemittel und Trinkwasser doppelt, schützt vor Einfrieren und puffert Zapfung und Wolken.
- Der Strom ist als Bereich gerechnet, mit PV-Reserve, Heißtag- und Nachtfall.
- Kondensator und Verdampfer sind nachgerechnet.
- Sorption, Wasserdampfverdichtung und Erdreich sind mit konsistenten Zahlen bewertet.

## 2. Warum der einfache Loop nichts bringt

| Größe (32 °C, 40 % r. F.) | Wert |
|---|---|
| Kühlgrenztemperatur ("nasser Lappen", offen) | 22,1 °C |
| Taupunkt | 17,2 °C |
| Sättigungsdruck Wasser bei 5,5 / 42 °C | 0,90 / 8,2 kPa |

- **Offen (Lappen):** Die Verdunstungswärme verlässt das System mit dem Dampf. Die Grenze ist die Kühlgrenze von 22,1 °C, das Leitungswasser hat aber schon 24 °C. Möglich sind 1–2 K, und es gehen ~1 l/h Wasser verloren (697 W ÷ 2450 kJ/kg). Das ist keine Lösung.
- **Geschlossen, ein Druck:** netto null Kühlung.
- **Passiver Thermosiphon** (Kondensator oben, Schwerkraft-Rücklauf) funktioniert nur, wenn der Kondensator kälter als das Wasser ist:
  - Tagsüber ist die Luft mit 32 °C wärmer als das Wasser (24 °C).
  - Nachts (20 °C) ginge es mit Strahlung zum Himmel, aber die Nettoleistung liegt bei nur ~25–40 W/m². Für 697 W bräuchte man 25–35 m², und das Wasser käme nur auf ~18–20 °C.
- **Untere Schranke (2. Hauptsatz):** Das Wasser (Strom von 24 auf 12 °C, mittlere Temperatur 17,9 °C) bei Umgebung 32 °C zu kühlen, kostet mindestens W = 697 · (305,15/291,1 − 1) ≈ **34 W**. Ideale Kältemaschine bei 5,5/42 °C (Carnot): 729/7,6 ≈ **96 W**. Real sind es **225 W** am Verdichter. Der Rest sind Temperaturdifferenzverluste und Verdichterverluste.

## 3. Welche Antriebe kommen infrage?

Es gibt nur zwei Arten von Antrieb: Arbeit (Verdichter) oder Wärme hoher Temperatur (Sorption). Rechnung jeweils für 729 W Kälte bei Te = 5,5 °C, Tc = 42 °C:

| Weg | Was nötig wäre | Urteil |
|---|---|---|
| **Verdichter, R290 (gewählt)** | Hubvolumen ~1–1,3 m³/h, 225 W elektrisch | Serienteile verfügbar |
| Wasser selbst als Kältemittel + Verdichter | 0,31 g/s Dampf = **160 m³/h** Saugvolumen, Druckverhältnis 9 (0,9 → 8,2 kPa), Endtemperatur ohne Zwischenkühlung >200 °C. Isentrop ~120 W, also energetisch ähnlich wie R290. | Braucht einen mehrstufigen Radialverdichter mit sehr hoher Drehzahl. Für 0,7 kW kenne ich kein Serienteil. |
| Solare Sorption (Silikagel/Wasser) | siehe Rechnung unten | Größer, teurer, nachts tot, nicht stromfrei. Verworfen. |
| Nachthimmelsstrahlung | 25–35 m², nur nachts, Wasser nur auf ~18–20 °C | Nur als Ergänzung. Abschätzung. |
| Erdreich (10–14 °C) | Als Wärmesenke für den Kondensator sinnvoll (Abschnitt 7), als Ersatz für den 5-°C-Verdampfer nicht | Ausbaustufe |

**Sorption, konsistent gerechnet.** Mit Luftkühlung erreicht der Adsorber ~38 °C, und die Zahlen sind Abschätzungen.
- Relativdruck im Adsorber: p_s(5,5 °C)/p_s(38 °C) = 0,90/6,63 = **0,136**.
- Relativdruck im Desorber (Kondensation bei 42 °C, 8,2 kPa): bei 85 °C Heiztemperatur 8,2/57,8 = **0,142**, bei 100 °C 0,081, bei 110 °C 0,057.
- Bei 85 °C ist der Hub also null. Erst ab ~100–110 °C entsteht ein Hub von ~0,03–0,04 kg/kg (aus typischen Silikagel-Isothermen, herstellerabhängig ±50 %).
- Mit COP_th ≈ 0,25 sind das ≈ 2,9 kW Heizwärme bei ≥100 °C. Das bedeutet ~9–11 m² Vakuumröhren und ~9 kg Gel in Betten, dazu Vakuumtechnik und 100–150 W Hilfsstrom. Nachts liefert die Anlage nichts.

**Einwand "Das ist keine Verdunstungskühlung mit Wasser mehr".** Das Prinzip bleibt erhalten. Ein Fluid verdampft an der Wand des Kaltteils, der Dampf kondensiert woanders. Die Wasserspeicherung steckt im Zwischenkreis. Aber das Fluid muss nach dem 2. Hauptsatz einen Druckhub bekommen. Wasser als Arbeitsmittel scheitert im Kleinformat an Verdichter (160 m³/h) oder Sorption (10 m² Kollektor). R290 hat 12 % des Dampfvolumens und ist für kleine Kältekreise Standard, zum Beispiel in Kühlgeräten mit R600a.

## 4. Aufbau

```
 RECHTER TURM: Wärme raus (im Schatten)          LINKER TURM: Kälte (dampfdicht gedämmt)
 ┌──────────────────────────────────┐            ┌────────────────────────────────────┐
 │ KONDENSATOR (Mikrokanal, 4 Reihen)│           │ KALTWASSERSPEICHER 150 l, 9,4 °C   │
 │ 42 °C, UA 150 W/K, ~4,7 m² außen │            │ (geschlossen, 1 bar, Ausdehnungsgef.)│
 │ Luft 32 → 36,4 °C, 0,18 m³/s     │            │  ┌───────────────────────────┐     │
 │ EC-Lüfter 30 W ▲                 │            │  │ Trinkwasser-Wendel        │◄ 24 °C
 └───▲──────────────────┬───────────┘            │  │ Edelstahl-Wellrohr, 21 m  │► 12 °C
     │ Heißgas ~65 °C   │ flüssig ~40 °C         │  │ (≈1,1 l Inhalt)           │     │
     │ 14,3 bar         │ 14,3 bar               │  └───────────────────────────┘     │
 ┌───┴───────────┐  ┌───▼────────────┐           └───▲───────────────────┬────────────┘
 │ VERDICHTER    │  │ Filtertrockner │               │ 7,8 °C            │ 9,4 °C
 │ DC-Inverter   │  │ + Expansions-  │ 5,6 bar       │   Pumpe 12 W ◄────┘ (400 l/h)
 │ 225 W aus PV  │  │ ventil         ├──────────►┌───┴─────────────────────┐
 │ 1,0–1,3 m³/h  │  │ ("Regen")      │  "Regen"  │ VERDAMPFER (Platten)    │
 └───▲───────────┘  └────────────────┘           │ R290 5,5 °C, ~0,2 m²    │
     └───────── Sauggas 5,5 °C, 5,6 bar ◄────────┴─────────────────────────┘
      R290 hermetisch, ~60–80 g, kein Verlust.  Wasser: nur im Zwischenkreis, kein Verlust.
```

**Warum Speicher und Zwischenkreis?**
1. **Trinkwasser-Schutz:** Zwischen R290 und Trinkwasser liegen zwei Wände (Plattenwand und Wendelwand) mit Speicherwasser dazwischen. Das ist die übliche Lösung nach EN 1717, die Details prüft ein Fachbetrieb.
2. **Frostschutz:** Das Trinkwasser hängt nicht mehr direkt am 5-°C-Verdampfer. Der Speicher wird bei 4,5 °C abgeschaltet, und der Niederdruckschalter greift bei ~4,7 bar (Te ≈ 0 °C).
3. **Zapfung unabhängig vom Verdichter:** Der Verdichter regelt auf die Speichertemperatur (Sollwert 6–10 °C), nicht auf den Durchfluss. Bei Zapfung 0 passiert nichts.
4. **Puffer:** Der Speicher gleicht Wolken und Zapfspitzen aus (Abschnitt 7).
5. **Hygiene:** Die Wendel enthält nur ~1,1 l Trinkwasser, das bei Stagnation auf Speichertemperatur (≤15 °C) bleibt. Das ist deutlich besser als eine Leitung, die in der Sonne 25–45 °C erreicht (Legionellen-Wachstum). Die Leitung hinter dem Speicher muss kurz (<3 l) und gedämmt sein.

**Regelung:**
- Der Verdichter folgt per Inverter dem PV-Angebot (MPPT).
- Der Lüfter ist temperaturgeführt.
- Die Umwälzpumpe läuft nur mit dem Verdichter.
- Hochdruckschalter bei 25 bar.
- Die Speicher- und Rohrdämmung ist diffusionsdicht (geschlossenzelliger Kautschuk), weil die Oberflächen unter dem Taupunkt von 17,2 °C liegen.

## 5. Rechnung (Auslegungsfall Tag: 32 °C, 800 W/m², 50 l/h)

**Kühllast Wasser:** ṁ = 50 l/h = 0,01389 kg/s. Q = 0,01389 · 4186 · (24 − 12) = **697 W**.

**Trinkwasser-Wendel im Speicher:**
- Rohr 8 mm innen, Re ≈ 2000, laminar bis Übergang. Nu ≈ 4,4 ergibt h_innen ≈ 325 W/m²K. Außen sind es durch die Pumpenströmung ~300 W/m²K.
- U ≈ 155 W/m²K. Für UA = 100 W/K braucht man 0,65 m², das sind ~21 m Wellrohr (das Wellrohr liefert zusätzlich Reserve).
- NTU = 100/58,1 = 1,72. Für den Auslauf von 12 °C ergibt sich eine Speichertemperatur von **9,4 °C**: T_aus = T_sp + 0,179 · (24 − T_sp).

**Verdampfer (Plattentauscher Wasser/R290, Zwischenkreis 400 l/h):**
- Last: 697 W + Pumpe 12 W + Speicherverluste 20 W (Dämmung ~1 W/K, im Schatten) = **729 W**.
- Wasser 9,4 → 7,8 °C, Verdampfung Te = 5,5 °C. ΔT_log = 3,0 K, UA = 240 W/K, mit U ≈ 1200 W/m²K ergibt das **≈ 0,2 m²**. Der Abstand zum Gefrierpunkt beträgt >5 K.

**Kreisprozess R290** (Näherungswerte aus Stoffdaten, ±5 %):
- Te = 5,5 °C (5,6 bar), Tc = 42 °C (14,3 bar), Druckverhältnis 2,6.
- Kälteeffekt: h_g(5,5 °C) − h_f(42 °C) = 580 − 310 = 270 kJ/kg. Massenstrom ṁ = 729/270 = **2,7 g/s**.
- Saugvolumen 0,23 l/s = 0,82 m³/h, also Hubvolumen ~1,0 m³/h. Ich empfehle einen Verdichter mit 1,2–1,4 m³/h und Inverter: Reserve für die Erstabkühlung und für 10 °C Auslauf.
- Isentrope Verdichtung ~46 kJ/kg, also 124 W. Bei Gesamtwirkungsgrad **0,55** (realistisch für einen kleinen, PV-direkt betriebenen Inverterverdichter; Bereich 0,45–0,60) sind das **225 W** (Bereich 206–275 W).
- COP Verdichter = 729/225 = 3,2, das sind ~43 % von Carnot. Heißgas ~60–70 °C.
- Ein reales Kennfeld eines R290-Verdichters (Hersteller-Software) sollte vor dem Kauf gegengerechnet werden.

**Kondensator** (Luft 32 °C):
- Wärme: Q_c = 729 + 225 − 30 (Gehäuse direkt an Luft) = **924 W**.
- Luft 0,21 kg/s (0,18 m³/s), Erwärmung 32 → 36,4 °C. ΔT_log = 7,6 K, erforderlich UA = 122 W/K.
- **Eingebaut UA = 150 W/K (+23 % Reserve).** Bezogen auf die Außenfläche mit U ≈ 32 W/m²K (Mikrokanal-Kondensatoren erreichen typisch 40–60, ich rechne konservativ) ergeben sich ~4,7 m². Das ist ein Register von ~0,3 × 0,3 m Stirnfläche, 4 Reihen, ~100 mm tief.
- Die Auslegung rechnet bewusst mit Tc = 42 °C. Im sauberen Neuzustand liegt Tc bei ~40,6 °C, und der Verdichter braucht ~5 % weniger.
- Lüfter: 0,18 m³/s · 70 Pa = 12,6 W hydraulisch, EC-Lüfter η ≈ 0,4, also **≈ 30 W**.

**Strom (ehrlich):**

| Verbraucher | W | Bandbreite |
|---|---|---|
| Verdichter | 225 | 206–275 |
| Lüfter | 30 | 25–40 |
| Umwälzpumpe | 12 | 10–15 |
| Regelung, Ventile, Sensoren | 8 | 5–10 |
| **Summe** | **275** | **255–325** |

Leistungszahl Gesamtsystem = 697/275 = 2,5.

**Empfindlichkeit gegenüber warmer Ansaugluft** (Rückströmung, heißer Untergrund): Der Verdichterstrom steigt um ~3,7 % je K höherer Kondensationstemperatur.
- +3 K: +25 W
- +5 K: +45 W

Darum gilt:
- Ansaugung von der Nordseite und nicht über Asphalt oder Blech.
- Abluft senkrecht nach oben (36 °C, leicht aufsteigend).
- Abstand zum PV-Feld ≥ 3 m. Das Feld gibt ~2,3 kW Abwärme ab, und seine Hinterlüftung muss frei bleiben.
- Windschutz an der PV-Seite.
- Direkte Sonne auf das Gehäuse gibt nur ~40–80 W, hat also geringen Einfluss, ein Schattendach ist trotzdem sinnvoll.

**PV:**
- Ein 400-Wp-Modul (1,95 m²) liefert bei 800 W/m² und Zelltemperatur ~57 °C, mit 0,96 für Verschmutzung und Mismatch und 0,96 für MPPT, etwa **262 W**.
- Ein Modul deckt die 275 W also nicht ganz. **Zwei Module (524 W)** decken die Last ab ~420 W/m² Einstrahlung, also etwa von 9 bis 17 Uhr an einem klaren Tag. Der Überschuss lädt Batterie oder geht ins Netz.

## 6. Energiebilanz (Tag, stationär)

Die PV-Zeile beschreibt den Flächenanteil (2,05 m²), der die Last deckt. Der Überschuss des zweiten Moduls ist nicht Teil der Bilanz.

| Zufuhr aus der Umgebung | W |
|---|---|
| Sonne, netto auf PV (2,05 m²) | 1509 |
| Wärme aus Leitungswasser | 697 |
| Wärmegewinn Speicher aus Luft | 20 |
| **Summe** | **2226** |

| Abfuhr an die Luft | W |
|---|---|
| PV-Abwärme | 1234 |
| Kondensator (729 Kälte + 225 Arbeit − 30) | 924 |
| Verdichtergehäuse | 30 |
| Lüfter und Regelung | 38 |
| **Summe** | **2226** |

Die Pumpenwärme (12 W) landet im Speicher und geht mit der Verdampferlast in den Kondensator.

## 7. Grenzfälle, Betrieb, Varianten

**Heißer Tag (40 °C, 900 W/m²):**
- Speicherverlust 31 W, Last am Verdampfer ~740 W.
- Kondensationstemperatur ≈ 49 °C (gleicher Kondensator, gleicher Luftstrom), Verdichter ≈ 290 W (Bereich 267–320 W).
- **Gesamt ≈ 340 W** (315–375 W), Leistungszahl ≈ 2,05. Heißgas ~80 °C, unkritisch.
- Zwei Module liefern dann ~560 W, das reicht.

**Nacht (Luft 20 °C, klarer Himmel):**
- Lüfter auf ~70 % (10 W), Tc ≈ 30 °C.
- Verdichter ≈ 145 W, **gesamt ≈ 175 W**, Leistungszahl ≈ 4,0.

**24-h-Dauerbetrieb bei 50 l/h (1200 l/Tag):**
- Rechnung: 10 h Tag zu ~260 W + 14 h Nacht zu ~175 W ≈ **5,0 kWh/Tag** für 16,7 kWh Kälte, mittlere Leistungszahl ≈ 3,3.
- Kosten bei 0,30 €/kWh: ≈ 1,50 €/Tag. Das sind rund 0,13 ct pro Liter gekühltes Wasser.
- PV-Ertrag: ~2,2 kWh pro Modul und klarem Sommertag.

| Versorgung | Aufbau | Ergebnis |
|---|---|---|
| **A: Netz + 2 Module** | Tag aus PV, Nacht aus Netz | Netzbezug ≈ 2,5 kWh/Tag ≈ 0,75 €/Tag, ~600–800 € für PV und Wandler |
| B: Inselbetrieb | 3 Module + 3 kWh LiFePO₄ + MPPT | Nur an klaren Tagen zuverlässig, ≈ 1400–1800 € |
| C: Nur bei Bedarf | 1–2 Module, Speicher als Puffer | Reicht für reale Zapfung (unten) |

**Betrieb mit zeitweiser Zapfung.** Reale Zapfung ist viel geringer als 50 l/h rund um die Uhr. Bei ~200 l/Tag sind das 2,8 kWh Kälte, also ~0,9 kWh Strom. Das schaffen ein Modul und der Speicher ohne Batterie.

| Speichertemperatur | Auslauf bei 50 l/h |
|---|---|
| 6 °C | 9,2 °C |
| 9,4 °C (Auslegung) | 12,0 °C |
| 15 °C | 16,6 °C |

- Bei 20 l/h kommt das Wasser praktisch mit Speichertemperatur heraus (~9,6 °C), bei 100 l/h mit ~15,6 °C. Bei 100 l/h reicht dann die Verdichterleistung nicht ganz, und der Speicher erwärmt sich langsam.
- **Ohne Verdichter** (Wolken, kein Strom) erwärmt sich der Speicher bei 50 l/h um ~4 K/h. Der Auslauf bleibt etwa 1,4 h unter 17 °C. Speicherinhalt Kälte zwischen 6 und 15 °C: 1,57 kWh, das sind ~105 l Trinkwasser um 12 K gekühlt.
- **Erstabkühlung** von 24 auf 9,4 °C: 2,6 kWh Kälte, ~3,5 h bei ~730 W ohne Zapfung.

**Auslauftemperatur** (gleiche Bauteile, Bandbreite ±15 %):

| Auslauf | Kälte | Te | Strom gesamt |
|---|---|---|---|
| 14 °C | 581 W | ≈ 8,6 °C | ≈ 205 W |
| **12 °C** | **697 W** | **5,5 °C** | **≈ 275 W** |
| 10 °C | 814 W | ≈ 2,4 °C | ≈ 345 W |

Unter 10 °C geht es mit dieser Wendel und diesem Plattentauscher nicht, weil Te an 0 °C stößt. Für 8 °C bräuchte man ~32 m Wendel und etwas mehr Plattenfläche, bei rund 400 W Strom.

**Sparvarianten** (Zahlen als Abschätzung):
- **Größerer Kondensator** (Tc ≈ 38 °C, UA ≈ 260 W/K, ~8 m² Außenfläche, Lüfter ~40 W): Verdichter ≈ 194 W, gesamt ≈ 255 W. Das spart nur ~8 % für 1,7-fache Fläche und lohnt kaum.
- **Erdreich als Wärmesenke** (geschlossener Solekreis, Erdsonde ~25 m, Sole ~20–22 °C, Kondensation bei ~26 °C): Verdichter ≈ 125 W, Solepumpe ~20 W, kein Kondensatorlüfter, gesamt ≈ 165 W (±25 W). Das spart ~40 %, die Bohrung kostet aber ~1,5–2,5 k€. Sinnvoll nur bei Dauerbetrieb. Das Trinkwasser geht dabei nicht durchs Erdreich, also gibt es keine Hygieneprobleme.
- **Abwärme nutzen:** Die 924 W bei 42 °C könnten Brauchwasser vorwärmen. Dann fällt der Lüfter weg.

## 8. Grenzen, Sicherheit, Kosten

- **Ohne Strom oder Hochtemperaturwärme gibt es keine Kühlung unter Umgebung.** Ideal wären 34 W, realistisch sind 275 W.
- **R290 ist brennbar.** Die Füllmenge liegt bei ~60–80 g (Mikrokanal-Kondensator, kleiner Plattentauscher) und damit unter 150 g. Das ist im Freien bei hermetischem Kreis gängige Praxis (EN 378, IEC 60335-2-89). Propan ist schwerer als Luft, also nicht in Keller oder Gruben aufstellen. Montage und Befüllung gehören in einen Kältefachbetrieb. Alternativen wie R134a oder R513A sind unbrennbar, haben aber hohes GWP und ~1,6-fach größeren Verdichter.
- **Kondensation:** Kalte Flächen sind unter dem Taupunkt. Diffusionsdichte Dämmung ist Pflicht.
- **Wolken:** Bei 400 W/m² liefern zwei Module ~260 W, der Verdichter dreht langsamer, die Kälteleistung sinkt. Der Speicher überbrückt ~1–2 h.
- **Trinkwasser:** Speicherwasser ohne Zusätze (kein Glykol), Rohr hinter dem Speicher kurz und gedämmt, bei Nichtnutzung alle 3 Tage spülen (VDI 6023).
- **Kosten (grob):**
  - Bauteile Kältekreis ~1,8–2,8 k€ (Verdichter, Platten- und Kondensator-Tauscher, Speicher 150 l, Wendel, Pumpe, Regelung).
  - PV + Wandler 600–800 €.
  - Montage und Inbetriebnahme durch Fachbetrieb ~0,8–1,5 k€.
  - Gesamt **≈ 3–5 k€** (Version A), mit Batterie ~1 k€ mehr.
- **Wartung:** Lamellen jährlich reinigen, Zwischenkreis-Wasser und Ausdehnungsgefäß prüfen. Der hermetische Verdichter hält bei sauberer Kondensatorluft 10–15 Jahre.
- **Unsicherheiten:** Stoffwerte ±5 %, Verdichter-Gesamtwirkungsgrad 0,45–0,60, U-Werte ±30 %, Sorptionsisothermen ±50 %. Die Angaben zu Erdsonde, Nachthimmelsstrahlung und Kosten sind Größenordnungen.

## 9. Was sich gegenüber Runde 2 geändert hat

- **Verdichterwirkungsgrad:** Statt 0,64 wird mit 0,55 gerechnet, der Strom ist als Bereich 255–325 W angegeben, und der Heißtag mit 40 °C ist ergänzt.
- **PV-Reserve:** Zwei Module statt eines, Netz oder Batterie für die Nacht, MPPT- und Verschmutzungsverluste eingerechnet.
- **Kondensator:** Der widersprüchliche Text zur "6-K-Reserve" ist ersetzt durch eine nachvollziehbare Rechnung (Luft, LMTD, UA mit 23 % Aufschlag, begründetes U) und die Empfindlichkeit gegenüber warmer Ansaugluft (+25 bis +45 W).
- **Verdampfer und Trinkwasser:** Kaltwasserspeicher mit Zwischenkreis statt doppelwandigem Direktverdampfer. Damit sind Frostschutz, doppelte Trennung und Legionellenschutz sauber gelöst, der Durchfluss ist vom Verdichter entkoppelt.
- **Zapfbetrieb:** Speicher mit Größe, Verlusten und Betriebsweise in der Hauptauslegung, dazu Auslauf-Tabelle für verschiedene Speichertemperaturen und Durchflüsse.
- **24-h-Bilanz:** Nacht durchgerechnet (175 W), Tagesverbrauch 5 kWh, Kosten für Netz-, Insel- und Realbetrieb.
- **Sorption und Erde:** Konsistente Relativdrücke (0,136 gegen 0,142 bei 85 °C) und als Abschätzung gekennzeichnet. Erde nur noch als geschlossener Solekreis für die Kondensatorseite, keine Trinkwasserleitung im Boden mehr.
- **Wasser als Kältemittel:** Wasserdampfverdichtung mit Zahlen bewertet (160 m³/h, Druckverhältnis 9) und begründet verworfen.

```json
{
  "knoten": {
    "Sonne": {"T_C": 5500, "rolle": "umgebung"},
    "Luft": {"T_C": 32, "rolle": "umgebung"},
    "Leitungswasser": {"T_C": 24, "rolle": "umgebung"},
    "PV": {"T_C": 57, "rolle": "komponente"},
    "Verdichter": {"T_C": 65, "rolle": "komponente"},
    "Kondensator": {"T_C": 42, "rolle": "komponente"},
    "Verdampfer": {"T_C": 5.5, "rolle": "komponente"},
    "Speicher": {"T_C": 9.4, "rolle": "komponente"},
    "Pumpe": {"T_C": 14, "rolle": "komponente"},
    "Luefter_Regelung": {"T_C": 40, "rolle": "komponente"}
  },
  "stroeme": [
    {"von": "Sonne", "nach": "PV", "W": 1509, "art": "strahlung"},
    {"von": "PV", "nach": "Luft", "W": 1234, "art": "waerme"},
    {"von": "PV", "nach": "Verdichter", "W": 225, "art": "arbeit"},
    {"von": "PV", "nach": "Luefter_Regelung", "W": 38, "art": "arbeit"},
    {"von": "PV", "nach": "Pumpe", "W": 12, "art": "arbeit"},
    {"von": "Luefter_Regelung", "nach": "Luft", "W": 38, "art": "waerme"},
    {"von": "Pumpe", "nach": "Speicher", "W": 12, "art": "waerme"},
    {"von": "Leitungswasser", "nach": "Speicher", "W": 697, "art": "waerme"},
    {"von": "Luft", "nach": "Speicher", "W": 20, "art": "waerme"},
    {"von": "Speicher", "nach": "Verdampfer", "W": 729, "art": "waerme"},
    {"von": "Verdampfer", "nach": "Verdichter", "W": 1027, "art": "stoff"},
    {"von": "Verdichter", "nach": "Kondensator", "W": 1222, "art": "stoff"},
    {"von": "Verdichter", "nach": "Luft", "W": 30, "art": "waerme"},
    {"von": "Kondensator", "nach": "Verdampfer", "W": 298, "art": "stoff"},
    {"von": "Kondensator", "nach": "Luft", "W": 924, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Leitungswasser", "T_ein_C": 24, "T_aus_C": 12, "kuehlleistung_W": 697},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```