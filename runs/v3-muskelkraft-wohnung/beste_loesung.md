# Zimmer kühlen: Was Muskelkraft mit reinem Wasser leisten kann

## 1. Kurzfazit

- **Muskelkraft ist mit den harten Vorgaben (nur Wasser, DIY) kein sinnvoller Kühlantrieb.** Die Physik erlaubt es, denn ein Wasserdampf-Verdichter hätte eine Leistungszahl von etwa 4 bis 5. Aber der dafür nötige Verdichter (≈ 60 bis 80 m³/h Saugvolumen bei 14 mbar) ist nicht selbst baubar. Alle anderen Muskel-Wege (Gewicht, Feder, Reibungswärme, Generator) liegen unter der nötigen Leistungszahl von ≈ 1,6 bis 2,7.
- **Treten belastet das Zimmer netto**, solange das Gerät keine Leistungszahl über ≈ 1,6 (20 min) bis 2,7 (60 min) erreicht. Die ehrliche Empfehlung lautet deshalb: nicht treten, um zu kühlen.
- **Beste baubare Lösung: Nachthimmel-Kältespeicher.** Ein geschlossener Wasserkreis mit Strahlungsabsorber, Wasserspeicher und Kühlkonvektor im Zimmer braucht weder Strom noch Vakuum noch Sonne. Er liefert etwa **0,8 kWh Kälte pro klarer Nacht** (33 W im 24-h-Mittel), wiegt etwa 250 kg und kostet etwa 1,1 bis 1,4 k€.
- **Gegenüber Durchlauf 2** (Zeolith, 470 kg, 12 bis 18 k€, nicht DIY) liefert er etwa 80 % der Kälte bei rund einem Zehntel der Kosten, ohne Vakuum. Der Kälteertrag ist dabei ein Abschätzwert (siehe Grenzen).

## 2. Ehrliche Bilanz des Tretenden

Annahmen: 100 W mechanisch, 20 min, Muskelwirkungsgrad 23 %.

| Größe | Wert |
|---|---|
| Stoffwechselleistung | 100 / 0,23 ≈ 435 W |
| Körperwärme | ≈ 335 W, in 20 min also 112 Wh |
| Im Körper gespeichert (Ø-Körpertemperatur +0,8 K, 75 kg × 3,47 kJ/kgK) | ≈ 58 Wh, geht mit ins Bad |
| **An das Zimmer abgegeben** | **≈ 54 Wh ≈ 160 W** (≈ 90 W fühlbar, ≈ 70 W latent durch Schweiß) |
| Mechanische Arbeit (33 Wh) | wird im Gerät zu Wärme, also draußen, nicht im Zimmer |

Die nötige Leistungszahl (Kälte am Zimmer pro mechanischer Wh) hängt von der Rundenlänge ab:

| Runde | mech. | ans Zimmer | COP_min |
|---|---|---|---|
| 20 min | 33 Wh | 54 Wh | **1,6** |
| 30 min | 50 Wh | ≈ 108 Wh | 2,2 |
| 60 min | 100 Wh | ≈ 270 Wh | 2,7 |

Kurze Runden sind günstiger, weil der Körper anfangs den größten Teil der Wärme speichert. Später speichert er kaum noch und gibt fast alles ans Zimmer ab.

## 3. Prüfung der Muskel-Optionen

| Option | Rechnung | Ergebnis |
|---|---|---|
| **Wasserdampf-Kolben/Membran/Roots-Verdichter** (Verdampfer 12 °C/14 mbar, Kondensator 38 °C/66 mbar, Druckverhältnis 4,7) | Isentrope Arbeit ≈ 253 kJ/kg, Kälte 2363 kJ/kg, ideal COP 9. Mit η_is 0,65 und Mechanik 0,85 ergibt sich COP ≈ 5, DIY-realistisch 2,5 bis 4. Für 400 W Kälte: 0,17 g/s × 93 m³/kg ≈ 16 l/s ≈ 57 m³/h. | Thermodynamisch gut, **Hardware nicht DIY.** Es braucht Vakuum-Wellendichtung, Klappenventile für 5 mbar Differenz, ≈ 80 m³/h Hubvolumen, korrosionsfeste Trockenläufer. |
| **Zeolith-Sorption mit Muskelwärme regenerieren** | 33 Wh Reibungswärme desorbieren etwa 0,04 kg Wasser, das sind ≈ 29 Wh Kälte, COP < 1 | Unter COP_min. Die Sonne liefert 50-mal mehr Wärme. |
| **Gewicht heben** | 100 kg × 2,3 m = 0,63 Wh; eine Runde (33 Wh) bräuchte 1,4 t | Unbrauchbar |
| **Feder spannen** | 33 Wh = 120 kJ; Stahlfeder ≈ 0,15 kJ/kg, also ≈ 800 kg | Unbrauchbar |
| **Generator + Peltier** | 60 W elektrisch × COP 0,5 bis 0,8 ≈ 40 W Kälte | Unter COP_min |
| **Pumpe/Lüfter treten** | Hydraulisch 10 bis 20 W nötig, aber 160 W Körperwärme kommen ins Zimmer | Nur Komfort, netto negativ |
| **Wasserstrahlpumpe** | Treibwasser-Dampfdruck (≥ 12 mbar bei 10 °C) blockiert das Vakuum | Funktioniert nicht für Kühlung unter Umgebung |
| **Barometrisches Vakuum** | Für 10 mbar braucht man ≈ 10 m Wassersäule, der Balkon hat 2,5 m | Unmöglich |

**Selbst im besten Fall bringt Muskelkraft wenig.** Bei COP 4 liefert eine 20-min-Runde 133 Wh Kälte und belastet das Zimmer mit 54 Wh, netto also +79 Wh. Bei COP 2,5 sind es nur +29 Wh. Für drei Runden am Tag wären das im Idealfall +0,24 kWh, gegen ein Hardware-Risiko, das kein Laie beherrscht.

## 4. Empfohlene Lösung: Nachthimmel-Kältespeicher (Muskelkraft optional)

**Prinzip:** Nachts strahlt ein schwarzer Absorber unter dünner Folie zum klaren Himmel (effektiv ≈ 4 °C) ab und kühlt einen Wasserspeicher auf ≈ 16 °C. Tagsüber fließt die Kälte per Schwerkraft zum Kühlkonvektor im Zimmer. Der Kreis ist geschlossen und hat keinen Verlust. Die Kältequelle ist der Nachthimmel, ein Antrieb im engeren Sinn ist nicht nötig.

```
        Nachthimmel (klar, ≈ 4 °C)   ↑ ↑ ↑ Strahlung (nachts)
   ┌────────── LDPE-Folie (Windschutz, IR-durchlässig) ───────────┐
   │ ▓▓▓▓▓▓▓▓ schwarzer Absorber 2,7 m², leicht geneigt ▓▓▓▓▓▓▓▓ │  h ≈ 2,3 m
   └──────┬────────────────────────────────────────┬──────────────┘
    kalt ↓ sinkt                            warm ↑ steigt
          │   (Verbundrohr 32×3, Schwerkraft)      │
     ┌────┴────────────────────────────────────────┴────┐
     │   Speicher 150 L, 15 cm gedämmt, auf Rahmen      │   h ≈ 1,2 m
     └────┬────────────────────────────────────────┬────┘
    kalt ↓   ── Fenster-/Balkontür-Durchführung ──   ↑ warm
     ┌────┴────────────────────────────────────────┴────┐
     │   Kühlkonvektor im Zimmer + Tropfschale          │   h ≈ 0,1–0,5 m
     └──────────────────────────────────────────────────┘
 Tagsüber: Absorber mit reflektierender Plane abdecken. Ist er warm, steht der Kreis still.
 Der Absorber liegt oben, also stoppt der Umlauf von selbst (Schwerkraftbremse).
```

### Rechnung (klare Nacht, 24-h-Mittel)

- **Strahlung** bei Wasser 16 bis 22 °C: brutto ≈ 50 bis 80 W/m². Mit Folie (τ ≈ 0,8) und Konvektionsgewinn abzüglich Reserve bleiben netto ≈ 35 bis 40 W/m². Bei 2,7 m² und 9 h ergibt das ≈ 0,9 kWh, davon etwa 0,8 kWh nutzbar nach Speicherverlusten von ≈ 4 W.
- **Speicher:** 150 L mit 5 K Hub speichern 150 × 4,19 × 5 ≈ 0,87 kWh. Passend.
- **Kühlkonvektor:** Typ 33, 600 × 1400 mm, hat bei 9 K Übertemperatur etwa 235 W (2,2 kW × (9/50)^1,3). Das reicht für den Abruf von 60 bis 100 W.
- **Kondensation:** Unter ≈ 16 bis 17 °C Oberfläche (Taupunkt Zimmer) kondensiert Feuchte am Register. Das entfeuchtet zusätzlich und wird in der Tropfschale gesammelt. Der Kühlkreis bleibt dicht.
- **Schwerkraftumlauf** (Grenzfall):
  - Nachts: Δp_Antrieb ≈ 6 Pa, Reibung in 6 m Rohr (ID 26) bei 15 g/s ≈ 8 Pa.
  - Tags: ≈ 9 Pa Antrieb, ≈ 8 Pa Reibung.
  - Der Umlauf liegt also gerade an der Grenze. Er wird zuerst getestet, sonst gilt der Fallback.
- **Zimmereffekt** (Zimmer 20 m², heißer Tag, Außenrollladen, Wärmelast Nachmittag ≈ 300 bis 400 W, Gesamt-UA ≈ 25 W/K, grob geschätzt): Ohne Gerät liegt der Tagesmittelwert bei ≈ 27,5 °C und die Abendspitze bei 29 bis 30 °C. **Mit Gerät sinkt er um 33 W / 25 W/K ≈ 1,3 K im 24-h-Mittel auf ≈ 26,2 °C.** In der Abendspitze sind es −2 bis −3 K (Abschätzung mit Speichermasse). Die Zielmarke ≤ 26 °C wird knapp verfehlt und **nicht garantiert**.

### Rolle der Muskelkraft

Das Fahrrad wird nicht gebraucht. Jede 20-min-Runde belastet das Zimmer mit 54 Wh (≈ 2 W im 24-h-Mittel, ≈ 0,09 K wärmer) und bringt keine Kälte. Sie ist also kein Kühlmittel, sondern Sport mit einem Preis von etwa 6 % der Nachtkälte.

**Ausbaustufe B (Experiment, nicht in der Stückliste):** Wer dennoch will, kann einen Wasserdampf-Verdichter mit Muskelantrieb an den Kaltwasserspeicher koppeln, etwa einen umgebauten Roots-Lader oder Membranverdichter. Er bräuchte ≈ 80 m³/h bei 14 mbar, eine vakuumdichte Welle und Klappenventile. Erwartung: netto +30 bis +80 Wh pro Runde. Das ist kein Laienprojekt.

### Strom
Basisfall 0 W. Fallback: Zirkulator 4 W × 9 h ≈ 36 Wh pro Nacht aus 20-W-PV-Modul mit 12-V/7-Ah-Akku, nur wenn der Schwerkrafttest scheitert. Im 24-h-Mittel wären das ≈ 1,5 W, ehrlich beziffert.

## 5. Gewicht und Balkonlast

| Position | kg |
|---|---|
| Speicher 150 L (gefüllt) | ≈ 190 |
| Absorber mit Wasser | ≈ 15 |
| Rahmen, Rohre, Wasser im Rohr | ≈ 35 |
| Plane, Kleinteile | ≈ 10 |
| **Summe Balkon** | **≈ 250** |

Das sind 2,5 kN auf 3 m², also ≈ 0,8 kN/m² im Mittel. Wohnungsbalkone sind für ≈ 4 kN/m² ausgelegt (DIN EN 1991-1-1, Kategorie Z). Der Speicher steht auf einer Lastverteilplatte (Multiplex 0,8 × 1,0 m), also ≈ 2,3 kN/m² lokal. Bei Zweifeln, Altbau oder Vermieter: Statik und Vermieter vorher klären.

## 6. Stückliste (ungefähre Preise)

| Teil | € |
|---|---|
| Schwimmbad-Solarabsorber (EPDM/PP) 2,7 m² | 150 |
| LDPE-Folie (IR-durchlässig, keine IR-Sperrfolie) + Latten | 30 |
| Tragrahmen (Holz/Alu) + Wandanker | 120 |
| Emaillierter/Edelstahl-Speicher 150 L + 15 cm Dämmung | 450 |
| Kompaktheizkörper Typ 33 als Kühler + Tropfschale | 170 |
| Verbundrohr 32×3 (≈ 8 m) + Pressfittings | 100 |
| Rohrdämmung, Durchführung Fenster/Balkontür | 70 |
| MAG 8 L, Sicherheitsventil 3 bar, Entlüfter, Kugelhähne, Manometer | 130 |
| Thermometer/Logger (mind. 4 Sensoren) | 30 |
| Abdeckplane (Alu/weiß), Schattiernetz | 25 |
| Kleinteile | 50 |
| **Summe Basis** | **≈ 1.150** |
| Optional Fallback: 4-W-Pumpe, 20-W-PV-Modul, Regler, Akku | ≈ 90 |
| **Summe mit Fallback** | **≈ 1.250** |

## 7. Bauanleitung

1. **Standort und Freigabe:** freie Himmelssicht prüfen (ein Balkon direkt darüber halbiert den Ertrag), Tragfähigkeit klären, Vermieter fragen.
2. **Rahmen** aus Kantholz oder Alu bauen und mit ≥ 4 Wandankern sichern. Windsog auf 3 m² beträgt ≈ 2 bis 3 kN, jeder Anker muss ≥ 1 kN Zug aufnehmen.
3. **Absorber** leicht geneigt montieren, Folie 2 bis 3 cm darüber spannen (Windschutz).
4. **Speicher** auf der Lastverteilplatte aufstellen, 15 cm dämmen.
5. **Rohrleitung** mit Pressfitting (Zange leihen) verlegen. Die Leitungen müssen stetig steigen oder fallen, damit Luft entweichen kann. Entlüfter an den Hochpunkten.
6. **Kühlkonvektor** im Zimmer möglichst tief hängen, Tropfschale darunter. Durchführung durch Fensterspalt oder Balkontür-Dichtprofil, alternativ Kernbohrung.
7. **Befüllen** mit Leitungs- oder VE-Wasser ohne Zusätze und entlüften. **Druckprobe** mit Wasser bei 3 bar über 30 min. Dichtheit mit Hausmitteln prüfen: Manometer beobachten, Fittings mit trockenem Papier kontrollieren.
8. **Betrieb:** ca. 20:30 Plane ab, ca. 7:00 Plane drauf. Ab Mittag Kugelhahn zum Register öffnen.
9. **Test:** Schwerkraft-Umlauf prüfen (Temperaturdifferenz Vor-/Rücklauf, Wärmebilanz). Wenn der Durchfluss < 30 l/h ist, Fallback-Pumpe einbauen.

**Sicherheit:**
- **Absturz und Wind:** Rahmen und Absorber gegen Windsog fest verankern.
- **Stagnation:** Ein unabgedeckter Absorber kann tagsüber bis ≈ 80 °C heiß werden. Deshalb Plane, Sicherheitsventil und MAG, Ventil-Ablass zum Boden.
- **Legionellen:** Kreiswasser nie als Trinkwasser nutzen.
- **Frost:** im Herbst entleeren.
- **Schimmel:** Register-Tropfschale täglich leeren.

## 8. Grenzen und Vergleich mit Durchlauf 2

| | Durchlauf 2 (Zeolith) | Nachthimmel-Speicher |
|---|---|---|
| Kälte/Tag | ≈ 1 kWh | ≈ 0,8 kWh (0,5 bis 1,2) |
| Gewicht | 470 kg | ≈ 250 kg |
| Kosten | 12 bis 18 k€ | 1,1 bis 1,4 k€ |
| Vakuum | ja, Helium-Lecktest | nein |
| DIY | nein | ja |
| Wetterabhängigkeit | klarer Tag | klare, trockene Nacht + freier Himmel |
| Muskel nötig | nein | nein |

**Grenzen:**
- Der Ertrag hängt an einer freien Himmelssicht und an trockener Luft. Bei Schwüle oder Bewölkung fällt er auf 0,3 bis 0,5 kWh.
- Der Schwerkraftumlauf ist rechnerisch grenzwertig und muss vor Ort getestet werden.
- Das Ergebnis reicht für spürbare −1 bis −3 K, nicht für Klimaanlagen-Niveau.
- Muskelkraft trägt nichts zur Kühlung bei, wie in Abschnitt 2 und 3 belegt.

## 9. Energiebilanz (24-h-Mittel, klare Sommernacht; Luft = Mittel aus Tag 32 °C und Nacht 20 °C)

```json
{
  "knoten": {
    "Wohnung": {"T_C": 27.5, "rolle": "umgebung"},
    "Luft": {"T_C": 26, "rolle": "umgebung"},
    "Himmel": {"T_C": 4, "rolle": "umgebung"},
    "Speicher": {"T_C": 20, "rolle": "komponente"},
    "Nachtstrahler": {"T_C": 17, "rolle": "komponente"}
  },
  "stroeme": [
    {"von": "Wohnung", "nach": "Speicher", "W": 33, "art": "waerme"},
    {"von": "Luft", "nach": "Speicher", "W": 4, "art": "waerme"},
    {"von": "Speicher", "nach": "Nachtstrahler", "W": 37, "art": "waerme"},
    {"von": "Luft", "nach": "Nachtstrahler", "W": 12, "art": "waerme"},
    {"von": "Nachtstrahler", "nach": "Himmel", "W": 49, "art": "strahlung"}
  ],
  "nutzen": {"knoten": "Wohnung", "T_ein_C": 27.5, "T_aus_C": 26.2, "kuehlleistung_W": 33},
  "luft_T_C": 26,
  "wasserverlust_l_pro_tag": 0
}
```