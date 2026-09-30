# Wasserleitung kühlen mit einem geschlossenen Verdampfungskreislauf: Verdichter, Kaltwasserspeicher und Erdvorkühlung

## 1. Kurzantwort

**Das Problem.** Ein geschlossener Kreislauf mit nur einem Druck ist ein Wärmerohr. Es transportiert Wärme, erzeugt aber keine Kälte. Verdampfer und Kondensator hätten dieselbe Temperatur, und die Kondensationswärme wäre exakt die aufgenommene Verdunstungswärme.

**Die Lösung.** Der Kreislauf braucht zwei Druckniveaus, denn Wärme fließt von selbst nur von warm nach kalt:
- **Unten (kalt, niedriger Druck):** Das Kältemittel verdampft bei ca. 4,5 °C an der Wand und nimmt die Wärme des Wassers auf. Das ist die Verdunstungskälte des nassen Lappens.
- **Verdichter:** Er hebt den Dampf auf ca. 13,7 bar, und dort kondensiert er erst bei ca. 40 °C. Damit ist der Kondensator wärmer als die Luft (32 °C).
- **Oben (warm, hoher Druck):** Der Dampf kondensiert bei 40 °C und gibt seine Wärme an die 32 °C warme Luft ab. Das geht ganz von selbst.
- **Expansionsventil:** Es ersetzt den „Regen“ und senkt den Druck des Kondensats wieder ab. Danach verdampft es unten erneut.

**Wo bleibt die Kondensationswärme?** Im Kondensator bei 40 °C, und von dort fließt sie an die Umgebungsluft:

| Anteil | Leistung |
|---|---|
| Wärme aus dem Wasser (über Speicher und Verdampfer) | 355 W |
| Verdichterarbeit, die als Wärme im Gas steckt | 99 W |
| **Kondensatorleistung an die Luft** | **454 W** |

Weitere 13 W gibt das Verdichtergehäuse direkt an die Luft ab. Die Kondensationswärme ist also größer als die Verdunstungswärme, und der Unterschied ist die Antriebsarbeit. Der Verdichter pumpt die Wärme von 4,5 °C auf 40 °C hinauf.

**Erdvorkühlung.** Ein Teil der Kühllast (378 von 698 W) muss gar nicht gepumpt werden. Das Erdreich hat 11–12 °C und ist damit eine echte kalte Senke. Ein Solekreis mit 20 W Pumpe kühlt das Wasser von 24 auf 17,5 °C vor. Erst die letzten 5,5 K macht die Kältemaschine.

**Ergebnis für den Auslegungsfall (32 °C, 40 % r. F., 800 W/m², 50 l/h):**

| Größe | Wert |
|---|---|
| Wasser | 24 °C → **12 °C** (20 K unter Lufttemperatur), Kühlleistung **698 W** |
| Wasserverlust | 0 |
| Strombedarf mit Erdvorkühlung | **≈ 166 W** (Bandbreite 140–210 W), Leistungszahl ≈ 4,2 |
| Strombedarf ohne Bohrung (Grundausbau) | **≈ 295 W** (260–350 W), Leistungszahl ≈ 2,4 |
| Tagesbedarf 24 h Dauerbetrieb | ≈ 3,5 kWh (mit Erde) bzw. ≈ 5,8 kWh (ohne) |
| Strom | 2 PV-Module à 400 Wp plus Netz oder Batterie für die Nacht |

Ohne Strom oder Wärme hoher Temperatur kommt man nur so weit, wie eine kalte Senke reicht: Erdreich, Grundwasser oder nachts der Himmel. Mit 100 m Erdsonde und 20 W Pumpe sind ca. 15 °C erreichbar (Abschnitt 8b). Für 12 °C und Dauerbetrieb braucht man den Verdichter.

## 2. Ehrlich vorab: Was vom Loop übrig bleibt

Das Ergebnis ist die konventionelle Antwort auf die Aufgabe, eine kleine Kältemaschine. Auch die Ausgangsidee bleibt in dieser Anordnung erkennbar:

| Ausgangsidee | Im Entwurf |
|---|---|
| Unten verdunstet Wasser an der Leitung | Verdampfer: Kältemittel verdampft an der Plattenwand |
| Dampf steigt auf | Sauggas zum Verdichter (eine Druckstufe dazwischen) |
| Oben kondensiert der Dampf | Kondensator im rechten Turm, bei 40 °C statt bei „kalt“ |
| Regen fällt zurück | Kondensat läuft über das Expansionsventil zurück |
| Zwei Türme | Linker Turm: Kälte (Speicher und Verdampfer), rechter Turm: Wärme raus (Kondensator) |

Es fehlte nur der Druckhub. Die einzige Variante, die ohne Verdichter als echter Zwei-Turm-Loop funktioniert, ist der passive Nachtloop (Abschnitt 8a).

## 3. Warum der einfache Loop nichts bringt

| Größe (32 °C, 40 % r. F.) | Wert |
|---|---|
| Kühlgrenztemperatur („nasser Lappen“, offen) | 22,1 °C |
| Taupunkt | 17,2 °C |
| Sättigungsdruck Wasser bei 4,5 / 40 °C | 0,83 / 7,4 kPa |

- **Offen (Lappen):**
  - Die Grenze ist die Kühlgrenze von 22,1 °C, das Leitungswasser hat aber schon 24 °C. Möglich sind 1–2 K.
  - Für 698 W würden ~1 l/h Wasser verdampfen (698 W ÷ 2450 kJ/kg = 0,28 g/s).
- **Geschlossen, ein Druck:** Netto null Kühlung.
- **Passiver Thermosiphon** (Kondensator oben, Schwerkraft-Rücklauf) funktioniert nur, wenn die Senke oben kälter ist als das Wasser unten:
  - Tags ist die Luft mit 32 °C wärmer als das Wasser.
  - Nachts hat der Himmel eine effektive Temperatur von etwa 3 °C (Berdahl-Martin, Luft 20 °C, Taupunkt 12 °C). Ein Strahlungsregister bei 15 °C schafft dann netto ca. 40 W/m², bei 12 °C nur ca. 20 W/m² (mit Windschutzfolie, Abschätzung).
  - Für 698 W wären das 17–35 m², und das Wasser käme nur auf ~16–18 °C.
- **Untere Schranke (2. Hauptsatz):** Wasser von 24 auf 12 °C (mittlere Temperatur 291,1 K) bei einer Umgebung von 305,15 K zu kühlen, kostet mindestens W = 698 · (305,15/291,1 − 1) ≈ **34 W**.
  - Eine Carnot-Maschine für die Stufe 2 bräuchte 355 W / 7,8 = 45 W.
  - Real sind es 112 W am Verdichter.
  - Der Rest sind Temperaturdifferenzverluste, Verdichterverluste, Lüfter und Pumpen.
- **Präzisierung der Grenze:** Der 2. Hauptsatz verbietet nur Kühlung unter alle verfügbaren Senken. Mit einer kalten Senke (Erde 11–12 °C) sind 24 → ~15 °C ohne Verdichter möglich. Der Engpass ist dann die Leistungsdichte im Untergrund, nicht die Thermodynamik.

## 4. Antriebe und Senken im Vergleich

Rechnung jeweils für die Stufe 2 (355 W Kälte, Te = 4,5 °C, Tc = 40 °C). Es gibt drei Wege zur Kälte unter Umgebungstemperatur: Arbeit (Verdichter), Wärme hoher Temperatur (Sorption) oder eine vorhandene kalte Senke (Erde, Grundwasser, Nachthimmel).

| Weg | Was nötig wäre | Urteil |
|---|---|---|
| **Verdichter, R290 (gewählt)** | Saugvolumen 0,42 m³/h, Hubvolumen ~0,6 m³/h, 112 W elektrisch | Kleine Drehzahlverdichter mit 3–5 cm³ sind Kleinkälte-Standard, Integration prüfen (Abschnitt 5) |
| Wasser als Kältemittel + Verdichter | 0,14 g/s Dampf = **~80 m³/h** Saugvolumen, Druckverhältnis ~9 | R290 braucht mit 0,42 m³/h **nur ~0,5 % (rund 1/190)** des Saugvolumens. Für Wasserdampf kenne ich in dieser Größe kein Serienteil (mehrstufiger Hochdrehzahl-Radialverdichter), verworfen |
| Solare Sorption (Silikagel/Wasser) | Hub erst ab ~100–110 °C Heiztemperatur, COP_th ≈ 0,25, das sind ≈ 1,4 kW Heizwärme ≥100 °C, ~5 m² Vakuumröhren, ~4 kg Gel, Vakuumtechnik, 50–100 W Hilfsstrom | Nachts tot, aufwendig, nicht stromfrei, verworfen (Zahlen ±50 %) |
| **Erdreich 11–12 °C als Senke** | Solekreis + Doppelwand-Plattentauscher, 20 W Pumpe | **Gewählt als Vorkühlung** (Abschnitt 5) |
| Grundwasser/Brunnen (10–12 °C) | Wenn genehmigt: direkt über Doppelwandtauscher, kaum Bohraufwand | Billigste Variante, wo vorhanden |
| Nachthimmelsstrahlung | 10 m² Register, nur nachts | Ausbaustufe für Gelegenheitsnutzung (Abschnitt 8a) |

## 5. Aufbau und Rechnung

```
   Zulauf 24 °C (beschattet, gedämmt, < 3 l)
        │
 ┌──────▼──────────┐  Sole 30 % PG   ┌────────────────────┐
 │ ① VORKÜHLER     │◄────────────────┤ ERDSONDE 40 m      │
 │ Doppelwand-PWT  │─────────────────►  Doppel-U, 11,5 °C  │
 │ 24 → 17,5 °C    │  Pumpe 20 W     │ (Senke, kein       │
 └──────┬──────────┘                 │  Wasserverbrauch)  │
        │ 17,5 °C                    └────────────────────┘
 ┌──────▼─────────────────────────┐          ┌───────────────────────────────┐
 │ LINKER TURM: KÄLTE             │          │ RECHTER TURM: WÄRME RAUS      │
 │ ② SPEICHER 150 l · 10,8 °C     │          │ KONDENSATOR (Lamellen-WT)     │
 │ Glykol 30 %, dampfdicht gedämmt│          │ 40 °C · ~3,3 m² Außenfläche   │
 │ Trinkwasser-Wendel 32 m ► 12 °C│          │ Luft 32 → 36 °C · 0,10 m³/s   │
 └───▲───────────┬────────────────┘          │ EC-Lüfter 16 W                │
     │ 9,7 °C    │ 10,8 °C  (Pumpe 10 W)     └───▲──────────────────┬────────┘
     │           │                       Heißgas │ ~60 °C           │ flüssig 38 °C
 ┌───┴───────────▼───┐   Sauggas 8,5 °C  ┌───────┴──────┐    ┌──────▼─────────┐
 │ VERDAMPFER        ├──────────────────►│ VERDICHTER   │    │ Trockner + EEV │
 │ Platte, R290      │   5,3 bar         │ Drehzahl-    │    │ („Regen“)      │
 │ Te 4,5 °C, 0,3 m² │                   │ geregelt     │    └──────┬─────────┘
 └───────▲───────────┘                   │ 112 W        │           │
         │                               └──────────────┘           │
         └──────────── Nassdampf 5,3 bar (nach EEV) ────────────────┘
   R290 hermetisch, ~40–60 g, kein Verlust · Wasser nur in Zwischenkreis und Sole
```

**Warum Speicher und Glykol-Zwischenkreis?**
1. **Doppelte Trennung:** R290, Plattenwand, Glykol-Speicher, Wendelwand und Trinkwasser, also zwei Wände (Prinzip EN 1717, Details prüft ein Fachbetrieb). Propylenglykol ist gesundheitlich unkritisch, ein Leck der Wendel bleibt aber ein Fall für Fachbetrieb und Wartung.
2. **Frostschutz:** Der Verdampfer sieht Glykol statt Trinkwasser. Der Niederdruckschalter greift bei ~4,3 bar (Te ≈ −2 °C).
3. **Entkopplung:** Der Verdichter regelt auf die Speichertemperatur (6–12 °C), nicht auf den Durchfluss.
4. **Puffer:** Der Speicher überbrückt Zapfspitzen und Wolken.
5. **Hygiene:** Die Wendel enthält nur ~1,5 l Trinkwasser (Abschnitt 9).

**Kühllast:** ṁ = 50 l/h = 0,01389 kg/s, also 58,1 W/K und Q = 58,1 · 12 = **698 W**. Davon macht die Stufe 1 (Erde) 378 W (24 → 17,5 °C) und die Stufe 2 (Kältemaschine) 320 W (17,5 → 12 °C).

**Stufe 1: Erdvorkühlung**
- Doppelwand-Plattentauscher mit UA ≈ 90 W/K (~0,2 m²). Sole (30 % Propylenglykol) 300 l/h, das sind 322 W/K.
- NTU = 90/58,1 = 1,55, Wärmeübertragungsgrad ε = 0,76. Für Wasser 24 → 17,5 °C braucht man Sole-Eintritt 15,4 °C.
- **Erdsonde 40 m** (Doppel-U, λ = 2 W/mK, ungestörte Temperatur 11,5 °C):
  - Erdlast 378 W + 20 W Pumpe = 398 W, also 10 W/m.
  - Linienquellen-Rechnung nach 90 Tagen Dauerbetrieb: ΔT_Wand = q/(4πλ) · (ln(4αt/r_b²) − 0,577) = 0,40 K · 8,2 ≈ **+3,2 K**.
  - Dazu kommt ein Bohrlochwiderstand von 0,1 K/(W/m), also +1 K. Die Sole liegt im Mittel bei ~16 °C, das passt zur Annahme.
- **Warum 40 m und nicht 25 m:** Bei 25 m wären es 16 W/m und +5,2 K nach 90 Tagen, die Vorkühlung fiele auf ~19 °C.
  - Jede weitere Verdopplung der Laufzeit bringt nur ~+0,3 K.
  - Im Winter regeneriert der Untergrund, weil die Anlage dort nicht läuft. Die ersten Wochen sind kälter (Wasser ~15 °C).
  - Bei λ = 1,5 W/mK wäre die Sole ~1 K wärmer.
- Pumpe: 300 l/h bei ~0,7 bar Gesamtverlust sind 5,7 W hydraulisch, mit η ≈ 0,3 also ≈ 20 W.

**Speicher und Trinkwasser-Wendel**
- Wellrohr aus Edelstahl, 8 mm innen, Re ≈ 2100. Innen h ≈ 325 W/m²K (Wellrohr turbulenter, mehr möglich). Außen h ≈ 220 W/m²K (Glykol 30 %, zäh). Damit U ≈ 128 W/m²K.
- Für UA = 100 W/K braucht man 0,78 m², das sind ~**32 m** Wellrohr mit ~1,5 l Inhalt.
- NTU = 100/58,1 = 1,72. Der Auslauf ergibt sich zu T_aus = T_sp + 0,179 · (T_ein − T_sp). Mit T_ein = 17,5 °C und T_aus = 12 °C folgt die Speichertemperatur **T_sp = 10,8 °C**.
- Der Druckverlust in der Wendel liegt bei ca. 0,04 bar.

**Last am Verdampfer (Stufe 2):**

| Anteil | Leistung |
|---|---|
| Wasser | 320 W |
| Speicher-Wärmegewinn (1,2 W/K · 21,2 K, Schatten, diffusionsdichte Dämmung) | 25 W |
| Zwischenkreis-Pumpe (nasslaufend, Verlust bleibt im Glykol) | 10 W |
| **Summe** | **355 W** |

**Verdampfer** (Platten-Wärmetauscher R290/Glykol, 300 l/h):
- Glykol 10,8 → 9,7 °C.
- Direktverdampfer mit elektronischem Expansionsventil (EEV) und **4 K Sauggas-Überhitzung**. Bei Te = 4,5 °C liegt das Sauggas am Austritt bei 8,5 °C, das ist 2,3 K unter dem Glykoleintritt. Das ist knapp, aber machbar.
- Fläche in zwei Zonen:
  - Zweiphasig: 355 W / (U 750 W/m²K · ΔT 5,2 K) ≈ 0,09 m².
  - Überhitzung: ~12 W bei ΔT_log ~2,2 K, mit U ≈ 200 W/m²K gibt das ≈ 0,03 m².
  - Rechnerisch also ~0,12–0,15 m².
- **Gebaut: 0,3 m².** Die Reserve wird für den Grundausbau (Last 735 W) und den 10-°C-Fall gebraucht. Im Auslegungsfall hebt sie Te real um ~1 K und spart ~4 % Strom.
- Druckverluste sind im Kennfeld enthalten und liegen für Kleinsysteme bei ≤ 0,2 K Te-Verlust.

**Kreisprozess R290** (Näherungswerte aus Stoffdaten, ±5 %):

| Größe | Wert |
|---|---|
| Verdampfung Te / Druck | 4,5 °C / ≈ 5,3 bar |
| Kondensation Tc / Druck | 40 °C / ≈ 13,7 bar |
| Druckverhältnis | 2,6 |
| Flüssig nach Kondensator | 38 °C (2 K Unterkühlung) |
| Kälteeffekt inkl. Überhitzung | 587 − 305 = 282 kJ/kg |
| Massenstrom | 355 / 282 = **1,26 g/s** |
| Saugvolumen (ρ ≈ 10,7 kg/m³) | 0,118 l/s = **0,42 m³/h** |
| Hubvolumen bei η_vol ≈ 0,75 | ~0,6 m³/h |
| Isentrope Verdichtung | ~46 kJ/kg, das sind **58 W** |
| Gesamtwirkungsgrad η (Motor, Umrichter, Mechanik) | 0,52 (Bereich 0,42–0,60) |
| **Elektrische Leistung** | **112 W** (Bereich 97–139 W) |
| Heißgas | ~55–65 °C |

- Der Kälte-COP des Verdichters beträgt 355/112 = 3,2, das sind ~40 % von Carnot (7,8).
- Der Verdichter gibt 13 W (12 %) über das Gehäuse direkt an die Luft ab. Damit steckt 99 W Arbeit im Gas.

**Verdichterwahl (ehrlich):**
- Ein passender Typ ist ein Drehzahlverdichter für R290 mit 3–5 cm³ Hubvolumen und 2000–4500 U/min. Solche Größen gibt es in der Kleinkälte (z. B. bei Secop, Embraco/Nidec, Highly).
- Ein konkretes Modell nenne ich nicht, weil ich kein Datenblatt geprüft habe. Vor dem Kauf muss der Kältebauer Kennfeld, Mindestdrehzahl und Ölrückführung mit Hersteller-Software gegenrechnen.
- Mindestdrehzahl und Takten: Bei ~40 % Teillast (Mindestdrehzahl) ist Schluss mit Modulation. Darunter läuft der Verdichter im Ein/Aus-Takt über die Speichertemperatur (Band z. B. 9,5–12,5 °C, ~0,5 kWh, das sind ~4 h Zyklus, also nur ~6 Starts pro Tag).
- Die Saugleitung ist kurz (< 3 m) und leicht steigend, das hilft der Ölrückführung.
- **Netzgekoppelt betreiben:** Der Verdichter hängt am Hausnetz, die PV speist parallel ein (Steckersolar, ≤ 800 VA). Damit gibt es kein PV-Direktproblem bei Wolken und keine Sonderintegration am MPPT.

**Kondensator** (Lamellen-Wärmetauscher, Klimagerätebauart, kein Sonderteil):
- Wärmeleistung Q_c = 355 + 99 = **454 W**. Luft 0,10 m³/s = 0,115 kg/s, das sind 116 W/K, Erwärmung 32 → 35,9 °C.
- ΔT_log = 5,8 K, erforderliches UA = 78 W/K.
- **Eingebaut UA = 96 W/K** (+23 % Reserve für Verschmutzung). Mit U ≈ 30 W/m²K bezogen auf die Außenfläche sind das ~3,3 m² (Lamellenpaket ca. 0,45 × 0,45 m Stirnfläche, 2–3 Reihen).
- Im sauberen Neuzustand stellt sich Tc ≈ 39 °C ein, die Auslegung rechnet konservativ mit 40 °C.
- Lüfter: 0,10 m³/s · 55 Pa = 5,5 W hydraulisch, EC-Lüfter mit η ≈ 0,35 gibt **≈ 16 W**.

**Strom (ehrlich):**

| Verbraucher | W | Bandbreite |
|---|---|---|
| Verdichter | 112 | 97–139 |
| Lüfter | 16 | 12–22 |
| Zwischenkreis-Pumpe | 10 | 8–12 |
| Sole-Pumpe (nur bei Zapfung/Betrieb) | 20 | 16–25 |
| Regelung, EEV, Sensoren | 8 | 5–10 |
| **Summe** | **166** | **140–210** |

Leistungszahl des Gesamtsystems = 698/166 = **4,2**.

**Grundausbau ohne Erdvorkühlung** (gleiche Methodik, 24 → 12 °C direkt im Speicher, T_sp = 9,4 °C):
- Last am Verdampfer 735 W (698 + 27 + 10), Te ≈ 3,5 °C, Tc ≈ 41 °C (Kondensator UA 96, Luft 0,18 m³/s).
- Massenstrom 2,64 g/s, isentrop 128 W, mit η = 0,52 elektrisch **246 W**.
- Dazu Lüfter 30 W, Pumpe 10 W, Regelung 8 W, zusammen **≈ 295 W** (260–350 W), Leistungszahl 2,4.
- Das sind 20 W mehr als in der letzten Fassung (275 W). Der Unterschied kommt aus dem realistischeren Verdampfer (Überhitzung, tieferes Te) und aus η = 0,52 statt 0,55.

**PV:** Ein 400-Wp-Modul (1,95 m²) liefert bei 800 W/m² und ~57 °C Zelltemperatur, mit 0,96 (Verschmutzung) und 0,96 (MPPT/Wechselrichter), etwa **262 W**. Für die Last von 166 W braucht man rechnerisch 1,24 m² PV-Fläche. Zwei Module (~524 W) decken die Last schon ab ~35 % Einstrahlung.

## 6. Energiebilanz (Tag, stationär)

Die PV-Zeile beschreibt den Flächenanteil (1,24 m²), der die Last deckt. Der Überschuss der Module wird eingespeist und ist nicht Teil der Bilanz.

| Zufuhr aus der Umgebung | W |
|---|---|
| Sonne, netto auf PV (1,24 m²) | 912 |
| Wärme aus Leitungswasser | 698 |
| Wärmegewinn Speicher aus Luft | 25 |
| **Summe** | **1635** |

| Abfuhr | W |
|---|---|
| Erdreich (378 Wasser + 20 Pumpe) | 398 |
| PV-Abwärme an Luft | 746 |
| Kondensator an Luft | 454 |
| Verdichtergehäuse an Luft | 13 |
| Lüfter und Regelung an Luft | 24 |
| **Summe** | **1635** |

Die Wärme der Zwischenkreis-Pumpe (10 W) landet im Speicher und geht mit der Verdampferlast in den Kondensator.

## 7. Grenzfälle und Betrieb

**Wind (0–3 m/s) und Rezirkulation am Kondensator:**
- Der Lüfter hat ~55 Pa, der Staudruck bei 3 m/s beträgt nur ~5 Pa. Gegenwind kostet also nur ~8 % Luftstrom.
- Der größere Effekt ist Rezirkulation der 36 °C warmen Abluft:

| Fall | ΔTc | Mehrstrom |
|---|---|---|
| Windstill, Ansaugung Nordseite, Abluft senkrecht nach oben | ±0 (Auslegung) | 0 |
| 3 m/s von vorn, 30 % Rezirkulation, −8 % Luftstrom | ≈ +1,6 K (+2 K) | ≈ +8 W |
| Schlechtester Fall (Windstau, 60 % Rezirkulation, Blech in der Sonne) | ≈ +5 K | ≈ +21 W Verdichter, +4 W Lüfter, **Gesamt ≈ 190 W** |

Die Empfindlichkeit beträgt ~3,7 % Verdichterstrom je K Tc, das sind ~4 W/K.
- Gegenmaßnahmen: Ansaugung von der Nordseite, nicht über Asphalt oder Blech; Abluft senkrecht nach oben; Windschutzblende auf der Luv-Seite; Abstand zum PV-Feld ≥ 3 m (das Feld gibt ~2 kW Abwärme ab); Schattendach (direkte Sonne aufs Gehäuse bringt nur ~40–80 W).

**Heißer Tag (40 °C, 900 W/m²):**
- Tank-Gewinn 35 W, Last am Verdampfer ~363 W.
- Tc ≈ 48 °C (16,5 bar), Verdichter ≈ 151 W, Heißgas ~75 °C.
- **Gesamt ≈ 210 W** (185–250 W), Leistungszahl ≈ 3,3.

**Nacht (Luft 20 °C, klarer Himmel):**
- Lüfter gedrosselt (0,07 m³/s, 6 W), Tc ≈ 28 °C.
- Verdichter ≈ 72 W (η ≈ 0,48 bei kleinem Druckverhältnis).
- **Gesamt ≈ 115 W** (100–140 W), Leistungszahl ≈ 6.

**24-h-Dauerbetrieb bei 50 l/h (1200 l/Tag):**
- 10 h Tag zu ~175 W plus 14 h Nacht/Übergang zu ~125 W sind ≈ **3,5 kWh/Tag** für 16,7 kWh Kälte. Die mittlere Leistungszahl liegt bei 4,8.
- Grundausbau ohne Erde: 10 h · 295 W + 14 h · 200 W ≈ 5,8 kWh/Tag, also 40 % mehr.
- Kosten bei 0,30 €/kWh: 1,05 €/Tag, das sind rund 0,09 ct pro Liter (ohne Erde 1,74 €/Tag).

| Versorgung | Aufbau | Ergebnis |
|---|---|---|
| **A: Netz + 2 Module** | Steckersolar 2 × 400 Wp am Hausnetz | PV-Ertrag ~4,4 kWh/Tag bei 3,5 kWh Bedarf: bilanziell gedeckt, nachts ~1,75 kWh aus dem Netz (~0,5 €/Tag) |
| B: Inselbetrieb | 2 Module + ~2,5 kWh LiFePO₄ + Wechselrichter für den Verdichter | Nur an klaren Tagen zuverlässig, ≈ 1,0–1,4 k€ Batterie und Technik |
| C: Nur bei Bedarf | Speicher als Puffer, z. B. 200 l/Tag | 2,8 kWh Kälte, ≈ 0,6 kWh Strom, ein Modul reicht ohne Batterie |

**Auslauftemperatur und Strom** (Bandbreite ±20 %):

| Auslauf | Kälte Stufe 2 | Te | Strom gesamt |
|---|---|---|---|
| 14 °C | 236 W | ≈ 8,5 °C | ≈ 110 W |
| **12 °C** | **355 W** | **4,5 °C** | **≈ 166 W** |
| 10 °C | 474 W | ≈ 3,7 °C (Verdampfer 0,3 m²) | ≈ 230 W (größerer Lüfter) |

Unter 10 °C wird Te knapp und die Wendel mit 32 m zu klein. Für 8 °C bräuchte man ~45 m Wendel und Glykol mit tieferem Gefrierpunkt, bei rund 300 W Strom.

**Zapfbetrieb:**

| Speichertemperatur | Auslauf bei 50 l/h |
|---|---|
| 6 °C | 8,1 °C |
| 10,8 °C (Auslegung) | 12,0 °C |
| 15 °C | 15,4 °C |

- Bei 20 l/h kommt das Wasser praktisch mit Speichertemperatur heraus (~11 °C). Bei 100 l/h sind es ~14,6 °C, und die Kälteleistung reicht kurzfristig durch Drehzahl-Erhöhung.
- **Ohne Verdichter** (Wolken, Ausfall) erwärmt sich der Speicher mit ~2 K/h (355 W bei 174 Wh/K). Der Auslauf bleibt etwa 3 h unter 17 °C. Voraussetzung ist, dass die Sole-Pumpe weiterläuft (20 W).
- **Erstabkühlung** von 24 auf 10,8 °C: 2,3 kWh Kälte, ~4 h ohne Zapfung.
- Der Speicher fasst zwischen 6 und 15 °C 1,57 kWh Kälte.

## 8. Ausbaustufen

**a) Passiver Nachtloop: der echte Zwei-Turm-Loop ohne Strom**

Wasser selbst als Arbeitsmittel funktioniert hier, wenn die Senke oben kälter ist als die Quelle unten:
- Unten sitzt im Speicher ein Rieselfilm-Verdampfer, oben ein schwarzes Strahlungsregister aus Rohren und Lamellen (~10 m², Dachfläche, Windschutzfolie aus PE).
- Betrieb als Wärmerohr mit Wasser im Vakuum bei ~14 °C und ~1,6 kPa.
- Die Dampfströmung bei 300 W (0,12 g/s, 12 l/s) läuft mit ~6 m/s in DN50 und braucht praktisch keinen Druckabfall. Die Sättigungsdruck-Empfindlichkeit von ~0,1 kPa/K macht das tolerierbar.
- Das ist eine Wärmediode: Tags stoppt der Fluss von selbst, wenn oben wärmer ist als unten.
- Leistung nachts: 10 m² · 25–35 W/m² ≈ 250–350 W, das sind 2–2,8 kWh je Nacht.
- Der Speicher kommt damit auf ~15–16 °C, tiefer nicht. Bei ≤ 100–150 l/Tag Gelegenheitszapfung liefert das stromfrei Wasser mit ~16 °C.
- Im Dauerbetrieb (1200 l/Tag) trägt der Loop nur ~15 % der Kälte bei und spart nachts etwa 0,6 kWh von ~5,8 kWh. Das lohnt nicht.
- Der Knackpunkt ist die jahrelange Vakuumdichtheit. Ein kleines Leck ruiniert den Loop. Das ist eine Planungsskizze, kein durchgerechneter Entwurf.

**b) Nur Erde, ganz ohne Verdichter**
- Bei 100 m Sonde (5 W/m, ΔT_Wand ≈ +1,7 K nach 90 Tagen) und einem größeren Vorkühler (UA 150 W/K, ε ≈ 0,9) liefert Sole von ~13,3 °C einen Auslauf von **~14,5–16 °C**.
- Strom: 20 W Solepumpe, Leistungszahl ~25. Kosten der Bohrung schätzungsweise 5–8 k€.
- Für 12 °C reicht das nicht, denn die Sole kann nicht unter Bohrlochtemperatur kühlen.

**c) Weitere Sparhebel**
- Sauggas-Flüssigkeits-Wärmetauscher im Kältekreis, dann genügt 1–2 K Überhitzung im Verdampfer und Te steigt (~−6 % Strom).
- Größerer Kondensator (Tc ≈ 38 °C, ~2 × Fläche): ~−8 % Strom, lohnt kaum.
- Abwärme (454 W bei 40 °C) zur Brauchwasser-Vorwärmung: Der Lüfter entfällt dann.

## 9. Betrieb, Winter, Hygiene, Sicherheit, Kosten

**Winter und Frostschutz:**
- Zwischenkreis und Sole enthalten 30 % Propylenglykol (Gefrierpunkt ≈ −13 °C, Berstschutz bis ≈ −20 °C). Das R290-System ist frostunempfindlich.
- Trinkwasser-Wendel, Vorkühler-Zweig und Zulauf werden im Winter entleert (Saisonbetrieb, Entleerventile mit Belüftung, Wendel ausblasen). Ohne Entleerung friert die Trinkwasserseite.

**Trinkwasser-Hygiene:**
- Der Zulauf vor dem Vorkühler ist beschattet, gedämmt und kurz (< 3 l) und wird von der Hausleitung her regelmäßig durchströmt. Die Wendel enthält ~1,5 l bei Speichertemperatur ≤ 15 °C, das ist deutlich besser als eine sonnenbeschienene Leitung mit 25–45 °C.
- Nach > 72 h Stillstand wird mit dem 3-fachen Wendelinhalt gespült (Magnetventil, automatisch, VDI 6023). Kaltwasser soll ≤ 25 °C haben (DIN 1988-200).
- Kein Glykol im Trinkwasser, Wendel und Vorkühler bleiben doppelt getrennt (Doppelwandtauscher).

**R290-Sicherheit:**
- R290 ist brennbar. Die Füllmenge liegt bei ~40–60 g (Mikrokanal- oder Lamellen-Kondensator, kleiner Plattentauscher) und damit weit unter 150 g. Das entspricht gängiger Praxis im Freien bei hermetischem Kreis (EN 378, IEC 60335-2-40).
- Propan ist schwerer als Luft, also nicht in Keller oder Gruben aufstellen. Montage und Befüllung gehören in einen Kältefachbetrieb.
- Unbrennbare Alternativen (R134a, R513A) haben hohes GWP und einen ~1,6-fach größeren Verdichter.
- Hochdruckschalter bei 25 bar, Niederdruckschalter bei ~4,3 bar.

**Kondensation und Dämmung:** Speicher und Rohre liegen unter dem Taupunkt (17,2 °C). Diffusionsdichte Dämmung (geschlossenzelliger Kautschuk) ist Pflicht.

**Kosten (grob, ±30 %):**
- Kältekreis (Verdichter, Platten- und Kondensator-Tauscher, EEV, Speicher 150 l, Wendel, Pumpe, Regelung): ~1,5–2,5 k€.
- PV und Wechselrichter: ~0,6–0,8 k€.
- Montage und Inbetriebnahme durch Fachbetrieb: ~0,8–1,5 k€.
- **Grundausbau gesamt ≈ 3–5 k€.**
- **Erdvorkühlung** (40 m Sonde, Vorkühler, Sole, Pumpe): zusätzlich ~2,5–4 k€.

**Wirtschaftlichkeit der Erde (ehrlich):**
- Die Erde spart ~2,3 kWh/Tag, das sind ~0,7 €/Tag oder ~100 € je Sommer.
- Die Bohrung amortisiert sich über den Strompreis allein nie.
- Sie lohnt sich, wenn ohnehin eine Sonde oder ein Brunnen vorhanden ist, im Inselbetrieb (spart Batterie und Module, ~1 k€), oder wenn Strom knapp ist.
- Sonst gilt der Grundausbau (295 W).

**Wartung:** Lamellen jährlich reinigen, Glykol- und Solekonzentration und Ausdehnungsgefäße prüfen. Ein hermetischer Verdichter hält bei sauberer Kondensatorluft 10–15 Jahre.

**Unsicherheiten:**
- Stoffwerte ±5 %, Verdichterwirkungsgrad 0,42–0,60, U-Werte ±30 %.
- Bodenparameter (λ 1,5–2,5 W/mK, Grundwasserfluss).
- Sorptionsisothermen ±50 %.
- Nachthimmelsstrahlung und Kosten sind Größenordnungen.
- Der Verdichter ist kein durchgerechnetes Serienteil: Kennfeld vor dem Kauf prüfen.

## 10. Was sich gegenüber Runde 3 geändert hat

- **Fehler „12 % des Dampfvolumens“** korrigiert: R290 braucht ~0,5 % des Saugvolumens von Wasserdampf (0,42 statt ~80 m³/h), das Argument gegen Wasserverdichtung wird stärker.
- **Absolutaussage entschärft:** „Ohne kalte Senke oder Antrieb keine Kühlung unter Umgebung“. Es gibt drei Wege (Arbeit, Hochtemperaturwärme, vorhandene Senke), Erde und Nachthimmel sind ausdrücklich bewertet.
- **Erdvorkühlung** gerechnet und als Hybrid in den Auslegungsfall aufgenommen (166 statt 295 W). Die Erdsonde ist mit 40 m und Langzeitdrift (+3,2 K nach 90 Tagen) statt 25 m und Wunschtemperaturen ausgelegt, und die Wirtschaftlichkeit ist ehrlich benannt.
- **Verdampfer** mit EEV, 4 K Überhitzung, zwei Flächenzonen und 0,3 m² gebaut.
- **Verdichter:** Kennfeld-Vorbehalt, Mindestdrehzahl, Takten über den Speicher, Ölrückführung. Netzbetrieb mit Einspeisung statt PV-Direktkopplung.
- **Winter und Zulauf:** Glykol-Zwischenkreis, entleerbare Trinkwasserseite, beschatteter Zulauf, Spülung nach Stillstand.
- **Nachtstrahlung** konsistent gerechnet (17–35 m² für 698 W). Der passive Nachtloop ist als Wasser-Vakuum-Wärmerohr skizziert.
- **Wind:** Gegenwind- und Rezirkulationsfälle quantifiziert (+2 bis +5 K auf Tc, Gesamtstrom bis ~190 W).
- **Kondensator:** als übliches Lamellenregister beschrieben.
- **Ehrlichkeit:** Die Lösung ist die konventionelle Kältemaschine. Die Abbildung auf die Ausgangsidee steht in Abschnitt 2.

```json
{
  "knoten": {
    "Sonne": {"T_C": 5500, "rolle": "umgebung"},
    "Luft": {"T_C": 32, "rolle": "umgebung"},
    "Leitungswasser": {"T_C": 24, "rolle": "umgebung"},
    "Erdreich": {"T_C": 14, "rolle": "umgebung"},
    "PV": {"T_C": 57, "rolle": "komponente"},
    "Verdichter": {"T_C": 60, "rolle": "komponente"},
    "Kondensator": {"T_C": 40, "rolle": "komponente"},
    "Verdampfer": {"T_C": 4.5, "rolle": "komponente"},
    "Speicher": {"T_C": 10.8, "rolle": "komponente"},
    "Pumpe_Zwischenkreis": {"T_C": 14, "rolle": "komponente"},
    "Pumpe_Sole": {"T_C": 18, "rolle": "komponente"},
    "Luefter_Regelung": {"T_C": 40, "rolle": "komponente"}
  },
  "stroeme": [
    {"von": "Sonne", "nach": "PV", "W": 912, "art": "strahlung"},
    {"von": "PV", "nach": "Luft", "W": 746, "art": "waerme"},
    {"von": "PV", "nach": "Verdichter", "W": 112, "art": "arbeit"},
    {"von": "PV", "nach": "Luefter_Regelung", "W": 24, "art": "arbeit"},
    {"von": "PV", "nach": "Pumpe_Zwischenkreis", "W": 10, "art": "arbeit"},
    {"von": "PV", "nach": "Pumpe_Sole", "W": 20, "art": "arbeit"},
    {"von": "Luefter_Regelung", "nach": "Luft", "W": 24, "art": "waerme"},
    {"von": "Pumpe_Zwischenkreis", "nach": "Speicher", "W": 10, "art": "waerme"},
    {"von": "Pumpe_Sole", "nach": "Erdreich", "W": 20, "art": "waerme"},
    {"von": "Leitungswasser", "nach": "Erdreich", "W": 378, "art": "waerme"},
    {"von": "Leitungswasser", "nach": "Speicher", "W": 320, "art": "waerme"},
    {"von": "Luft", "nach": "Speicher", "W": 25, "art": "waerme"},
    {"von": "Speicher", "nach": "Verdampfer", "W": 355, "art": "waerme"},
    {"von": "Verdampfer", "nach": "Verdichter", "W": 487, "art": "stoff"},
    {"von": "Verdichter", "nach": "Kondensator", "W": 586, "art": "stoff"},
    {"von": "Verdichter", "nach": "Luft", "W": 13, "art": "waerme"},
    {"von": "Kondensator", "nach": "Verdampfer", "W": 132, "art": "stoff"},
    {"von": "Kondensator", "nach": "Luft", "W": 454, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Leitungswasser", "T_ein_C": 24, "T_aus_C": 12, "kuehlleistung_W": 698},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```