# Zimmer kühlen: Nachthimmel-Kühler mit freiem Wasserumlauf (ohne Pumpe, ohne Strom). Muskelkraft nur als Reserve

## 1. Kurzfazit

- **Muskelkraft ist mit Wasser und Selbstbau kein Kälteerzeuger.** Jede Wattstunde Tretarbeit setzt 1,4 bis 2,6 Wh Körperwärme im Zimmer frei (Abschnitt 4). Kein DIY-Gerät mit Wasser liefert mehr Kälte pro Tretwatt. Die einzige Lösung, die das schaffen würde, ist der Wasserdampf-Verdichter. Der ist nicht selbst baubar und brächte nur etwa ein Zehntel der Nachtkälte.
- **Ansatzwechsel gegenüber Runde 3.** Dort lud das Treten eine Batterie für eine 1,5-W-Pumpe, also praktisch nur Dekoration. Jetzt läuft das Wasser **von selbst durch Schwerkraft** (Thermosiphon). Der Nachtkollektor sitzt höher als der Raumkühler, und das Auftriebsprinzip erledigt den Umlauf. Das ist zugleich eine **thermische Diode**: Tagsüber liegt der heiße Kollektor oben, das Wasser bleibt stabil geschichtet, und es fließt keine Wärme ins Zimmer.
- **Muskeln:** Im Normalbetrieb 0 Wh. Sie sind nur die **Reserve**, falls der freie Umlauf im Test zu schwach ist. Dann treibt eine Pumpe im Bypass, und das Treten kostet etwa 40 min pro Tag (Spanne 15 bis 70 min). Das setzt im Mittel ≈ 5 W Wärme im Zimmer frei und kostet ≈ 0,2 K.
- **Ertrag (Auslegungsnacht, klar, 10,5 h):** im Mittel 102 W, das sind ≈ **1,07 kWh pro Nacht** und **44,5 W** im 24-h-Mittel.
- **Zimmer (Modell mit Rückkopplung):** 24-h-Mittel **28,1 → 26,0 °C (−2,0 K)**. Die Spanne je nach Raum liegt bei −1,0 bis −3,2 K. Der Aufbau dauert 3 bis 4 Tage. Das Ziel ≤ 26 °C wird im Basisfall knapp erreicht, aber nicht mit Reserve.
- **Praxis:** Der Balkonteil wiegt ≈ 90 kg, dazu kommen ≈ 135 kg Heizkörper an der Zimmerwand. Die Kosten liegen bei ≈ 2,1 k€ (1,8 bis 2,5 k€), mit Muskel-Reserve ≈ 2,3 k€.
- **Größtes Risiko:** Der freie Umlauf hat nur ≈ 14 Pa Antrieb und ≈ 20 % Reserve. Luftpolster oder Engstellen stoppen ihn. Deshalb gibt es einen Abnahmetest und einen Pumpen-Bypass.

## 2. Was gegenüber Runde 3 korrigiert wurde

| Kritikpunkt | Änderung |
|---|---|
| Muskel nur Dekoration, Kennzahl „36 Wh/Wh" irreführend | Kennzahl gestrichen. Muskeln sind Reserve, nicht Kälteerzeuger. Direkt mechanischer Pumpenantrieb wird mit Zahlen geprüft (4.3). |
| Pumpenbedarf optimistisch | Im Normalbetrieb keine Pumpe. Für die Reserve gilt eine Spanne von 0,6 bis 4 W statt eines einzelnen Wertes. Der Wirkungsgrad der Kette ist ehrlich mit 0,5 angesetzt (vorher 0,68). |
| Innenkühler 45 W/K schöngerechnet | Ansatz **18 W/K je Typ-22-Körper** bei ΔT ≈ 2 K, zusammen 54 W/K für drei Körper (Herleitung in 6.3). |
| Nachtbilanz inkonsistent | **Drei Nachtblöcke** plus periodische Zimmersimulation. Die Raumtemperatur der Blöcke folgt aus dem Modell (Rückkopplung Raum ↔ Ertrag geschlossen). |
| Taupunkt/Luftfeuchte widersprüchlich | Der Taupunkt bleibt konstant bei 17,4 °C. Das entspricht nachts ≈ 73 % r. F. bei 22,5 °C, nicht 80 %. Der Raumtaupunkt liegt mit Schläfer bei ≈ 18,5 bis 20 °C, nicht bei 15 °C (Fehler in Runde 3). Die Kondensation wird in 6.6 behandelt. |
| Sensitivität G_a, Last, Wetter | Tabellen für G_a, Last, Himmelssicht und eine Wetterverteilung in 6.4 und 6.5. |
| Außen-Heizkörper heikel (liegend, Entlüftung, Korrosion) | Ersetzt durch **unverglaste Kupfer-Alu-Absorber in Harfenbauart** (Solar-Ersatzteil), weiß lackiert. Sie sind für Neigung und Entlüftung gebaut und für 6 bis 10 bar ausgelegt. Es gibt einen Vortest mit einem Modul. |
| Schweißwert 25 g, Nachlauf im Zimmer fehlt | Zimmerwärme als Spanne (35 bis 65 Wh je Runde) inklusive 5 min Abkühlen im Zimmer (4.1). |
| Rechenfehler Gewichtspumpe (0,5 Wh) | Korrigiert: hydraulisch nur 15 bis 40 J je Nacht (4.3). Der Wasserinhalt wird ausgewiesen (7). |
| Kühlziel verfehlt, Rollo und 3. Kühler „optional" | Drei Kollektoren, drei Raumkühler und das Außenrollo sind jetzt **Standardumfang**. |

## 3. Prinzip

Die früheren Erkenntnisse gelten weiter. Ein geschlossener Verdunsten-Kondensieren-Kreis ohne Druckhub kühlt nicht, und offene Verdunstung verliert Wasser. Deshalb gibt es hier **keinen Phasenwechsel und keinen Druckhub**. Die Wärme fließt von selbst, weil eine kältere Senke existiert.

1. **Senke:** Nachts strahlt der weiße Absorber (ε ≈ 0,9) zum klaren Himmel (≈ 7 bis 14 °C) und gibt Wärme an die Nachtluft (26 → 20 °C) ab. Er liegt auf ≈ 22 bis 25 °C, also unter der Raumtemperatur von 25,7 bis 26,3 °C.
2. **Quelle:** Drei Heizkörper im Zimmer nehmen bei 21 bis 26 °C Wasser Wärme aus dem Raum auf. Mit Wasser über dem Taupunkt gibt es kaum Kondensat.
3. **Antrieb: Schwerkraft.** Der Raumkühler (Wärmequelle) liegt **unten** (Mitte ≈ 0,6 m), der Kollektor (Wärmesenke) **oben** (Mitte ≈ 2,3 m). Erwärmtes Wasser steigt zum Kollektor, gekühltes sinkt zurück.
4. **Diode:** Tagsüber erwärmt die Sonne den Kollektor auf ≈ 45 °C. Er liegt oben, das warme Wasser bleibt oben, und es entsteht keine Strömung. Es braucht weder Regler noch Ventil. Die Wärmeleitung über die Kupferrohre beträgt ≈ 0,7 W im Tagesmittel.
5. **Speicher:** Die Zimmerwände (≈ 3,5 MJ/K wirksam) speichern die Kälte. Der Effekt baut sich in 3 bis 4 Tagen auf.
6. **Muskel:** Nur als Rückfallebene (Pumpen-Bypass, Abschnitt 4.4).

## 4. Ist Muskelkraft sinnvoll? Ehrliche Bilanz

### 4.1 Bilanz des Tretenden (Runde 20 min, 75 W mechanisch)

| Größe | Wert |
|---|---|
| Stoffwechsel (η = 0,23) | 326 W, in 20 min 109 Wh |
| Körperwärme | 251 W, in 20 min 84 Wh |
| Im Körper gespeichert (Ø-Körpertemp. +0,4 bis +0,9 K, 72 Wh/K) | 29 bis 65 Wh, Mittel 43 Wh, geht ins Bad |
| Ans Zimmer während des Tretens | 19 bis 55 Wh, Mittel 41 Wh |
| Nachlauf im Zimmer (5 min Abkühlen, ≈ 80 W über Ruhe) | ≈ 6 Wh |
| **Körper → Zimmer je Runde** | **≈ 47 Wh (35 bis 65 Wh)** |

Schweiß: 60 bis 150 g werden abgegeben, davon verdunsten nur ≈ 25 bis 45 g im Zimmer (17 bis 30 Wh latent). Der Rest tropft, wird abgetrocknet oder geduscht. Energetisch steckt das schon in der Speicherung und im Bad. Die Feuchte (+0,5 bis 1 g/m³) ist bei einem Kondensat ableitenden Kühler unkritisch.

### 4.2 Nötige Leistungszahl (Zimmerwärme je Wh mechanisch, nur Körper)

| Runde | mech. | Wärme ans Zimmer | COP_min |
|---|---|---|---|
| 20 min, 75 W | 25 Wh | 47 Wh (35 bis 65) | **1,9** (1,4 bis 2,6) |
| 30 min, 100 W | 50 Wh | 110 Wh | 2,2 (1,8 bis 2,8) |
| 60 min, 100 W (Körper +1,5 K) | 100 Wh | 237 Wh | 2,4 (2,0 bis 3,0) |

Kurze Runden sind günstiger, weil der Körper anfangs viel Wärme speichert. Kettenverluste im Zimmer kommen zusätzlich hinzu. Ein Gerät muss also mehr als **≈ 2 bis 3 Wh Kälte je Wh Tretarbeit** liefern, damit sich das Treten lohnt.

### 4.3 Prüfung der Muskel-Optionen (Zahlen für 115 W Kälte, Nacht)

| Option | Ergebnis |
|---|---|
| **Wasserdampf-Verdichter** (Verdampfer 15 °C/17 mbar, Kondensator ≈ 27 °C) | Für 115 W Kälte sind ≈ 13 m³/h Saugvolumen nötig. Real COP ≈ 6 bis 8. Das ist die einzige Option über COP_min, aber **nicht DIY** (vakuumdichte Welle, Klappen für < 20 mbar, Verdichterrad). Je 20-min-Runde bringt sie nur ≈ +100 Wh netto, ein Zehntel der Nachtkälte des Kollektors. |
| Lüfter am Raumkühler (Kühler-Leitwert 54 → 94 W/K) | Mehrertrag ≈ +14 W = 147 Wh/Nacht. Kosten: 4 W Lüfter → 42 Wh el. → 84 Wh mech. → ≈ 2,3 Wh Zimmerwärme je Wh. Der Gewinn entspricht ≈ 2 Wh/Wh. Das ist **Nullsumme, nicht empfohlen**. Mehr Kollektorfläche ist besser. |
| Pumpe per Batterie (Runde 3) | Unnötig, solange der freie Umlauf läuft. Nur als Reserve (4.4). |
| **Direkt mechanischer Pumpenantrieb** (Gewicht, Feder, Schwungrad) | Hydraulisch braucht der Kreis nur ≈ 0,1 mW (14 Pa × 8 g/s) bzw. mit Pumpe (≈ 40 Pa × 25 g/s) ≈ 1 mW. Das sind **15 bis 40 J je Nacht**. Ein Gewicht von 20 kg × 1,8 m speichert 350 J, bei 10 % Wirkungsgrad genug. Physikalisch möglich, aber ein 10-h-Uhrwerk ist kein Anfänger-DIY. Eine Batterie ist einfacher, und der freie Umlauf braucht das alles nicht. |
| Sorption mit Muskelwärme regenerieren | 33 Wh Reibungswärme ergeben ≈ 29 Wh Kälte, COP < 1. |
| Generator + Peltier | 17 Wh el. × COP 0,5 bis 0,8 ergeben ≈ 10 Wh Kälte, weit unter COP_min. |
| Barometrisches Vakuum / Strahlpumpe | Unmöglich (10 m Wassersäule bzw. Dampfdruck des Treibwassers). |

**Ergebnis:** Muskelkraft als Kälteerzeuger ergibt mit Wasser und DIY eine negative oder allenfalls neutrale Bilanz. Die beste Lösung nutzt Schwerkraft und Nachthimmel und kommt ohne Treten aus.

### 4.4 Muskel-Reserve (nur wenn der Abnahmetest scheitert)

- **Pumpe:** bürstenlose 12-V-Kreiselpumpe (Aquaristik/Solar, 3 bis 5 W Nennleistung), per PWM oder Vorwiderstand gedrosselt. Der Bedarf liegt bei 0,6 bis 4 W, Ansatz 2 W. **Vor dem Kauf** am Multimeter die Leistung im Betriebspunkt messen (≈ 25 g/s, ≈ 40 Pa).
- **Energie pro Nacht:** 2 W × 10,5 h = 21 Wh, Regler (Arduino/ESP, ≈ 0,1 W) 2,4 Wh, zusammen ≈ 23,4 Wh elektrisch.
- **Kette:** Reibrad 0,95 × Generator 0,70 × Wandler 0,90 × AGM 0,80 ≈ **0,5**. Das ergibt 47 Wh mechanisch, also **≈ 37 min bei 75 W** (Spanne 15 bis 72 min für 0,6 bis 4 W).
- **Zimmerwärme:** Körper (Runde ≈ 37 min, +0,9 K) ≈ 100 Wh, dazu Kettenverluste im Zimmer ≈ 19 Wh, zusammen **≈ 120 Wh (100 bis 170)**, also ≈ 5 W im Mittel. Die Pumpenwärme (≈ 23 Wh) fällt draußen an.
- **Bilanz:** 1068 Wh Kälte gegen 120 Wh Wärme. Netto ≈ 39,5 W statt 44,5 W, das Zimmer wird ≈ 0,2 K wärmer als im Normalbetrieb.
- **Batterie:** 12 V 7 Ah (84 Wh) reicht für ≈ 3 Nächte. Alle 2 Tage 35 min statt täglich ist möglich.

## 5. Aufbau

```
 BALKON (außen)                Himmel (klar, Ø ≈ 9 °C)   ↑↑↑ Abstrahlung nachts
 ┌──────────────────────────────────────────────────────────┐ Mitte ≈ 2,3 m
 │ Pergola: 2 Absorber à 1,0 × 1,4 m (Harfe), weiß, 5° geneigt│ Hochpunkt:
 │ + Absorber 3 senkrecht an der Brüstung (außen)             │ Entlüfter + MAG
 └───────┬───────────────────────────────▲──────────────────┘
   Sammler unten (kalt)                   │ Sammler oben (warm)
   Cu 35×1,5, gedämmt, stetig fallend     │ Cu 35×1,5, gedämmt, stetig steigend
═════════╪════ Kernbohrung Ø 125 (Höhe ≈ 1,1 m) ═════════════╪═══════
 ZIMMER  ↓                                │
   kalte Verteilung ──┬───────┬───────┐   │ warme Sammelleitung (oben)
                      │       │       │   │
                   ┌──┴─┐  ┌──┴─┐  ┌──┴─┐ │  3 × Typ 22, H600 × L1800,
                   │ K1 │  │ K2 │  │ K3 │─┘  Anschluss diagonal:
                   └────┘  └────┘  └────┘    unten kalt ein, oben warm aus
         Unterkante 0,3 m · Tropfschale + Kondensatflasche darunter
         Reserve: Pumpe in Bypass (2 Vollstrom-Kugelhähne), 12 V AGM,
         Tretlader nur bei Bedarf
```

**Verlegeregeln (entscheidend, denn der Antrieb beträgt nur ≈ 14 Pa = 1,4 mm Wassersäule):**
- Die warme Leitung steigt stetig, die kalte fällt stetig. Gefälle jeweils ≥ 1 cm/m.
- Es gibt keine Wasser- oder Luftsäcke.
- Im Hauptstrang gibt es keine Rückschlagklappen, Schmutzfänger, Thermostatventile oder 15-mm-Engstellen. Nur Vollstrom-Kugelhähne sind erlaubt.
- Entlüfter sitzen an allen Hochpunkten, Entleerhähne an allen Tiefpunkten.

## 6. Rechnung

### 6.1 Senke in drei Nachtblöcken (Taupunkt konstant 17,4 °C)

Himmel nach Berdahl-Martin (ε_sky = 0,711 + 0,0056·T_d + 0,000073·T_d² + 0,013·cos(15t)). Die Absorberfläche hat ε = 0,9. Der Himmelssicht-Faktor beträgt 0,5 (Rest = Umgebung), die Konvektion h = 5 W/m²K.

| Block | Luft | Himmel | Umgebung (Fassade) | Nullfluss-Temperatur T₀ | h_eff |
|---|---|---|---|---|---|
| 1: 20:30–00:00 | 26 °C | 13,5 °C | 28 °C | 23,5 °C | 10,5 W/m²K |
| 2: 00:00–03:30 | 22 °C | 9,6 °C | 25 °C | 19,8 °C | 10,3 W/m²K |
| 3: 03:30–07:00 | 20,5 °C | 7,4 °C | 23 °C | 18,1 °C | 10,3 W/m²K |

Der Fluss je m² beträgt q = h_eff·(T_s − T₀). Beispiel Block 2: bei T_s = 23 °C sind es 33 W/m². Die Nachtluft-Mittelwerte (22,8 °C) stimmen mit Runde 3 überein.

**Absorberfläche:** 2 × 1,4 m² auf der Pergola plus 1,4 m² an der Brüstung (Himmelssicht 60 %). Das ergibt **A_eq = 3,64 m²**. Der Fin-Wirkungsgrad (Alu 0,4 mm, Teilung 100 mm) liegt bei F′ ≈ 0,9. Damit ist **UA_außen ≈ 34 W/K**.

### 6.2 Freier Umlauf (Thermosiphon)

- **Antrieb:** ρ·g·β = 2,5 Pa/(K·m), Höhenabstand der Wärmezentren H ≈ 1,6 m, also Δp_A = 4,0 Pa/K · ΔT_Kreis.
- **Widerstand** (laminar, bei 8 g/s):
  - Rohre Cu 35×1,5 (Innen-Ø 32 mm), 12 m: 0,47 Pa je g/s
  - Absorber-Harfe (30 Steigrohre, Innen-Ø 8 mm): 0,45 Pa je g/s
  - Heizkörper (drei parallel) 0,30, Verteiler und Fittings 0,20
  - Ansatz **R = 1,7 Pa je g/s** (konservativ, ≈ 20 % Reserve)
- **Gleichgewicht:** 4,0·Q/(4,18·ṁ) = 1,7·ṁ, also ṁ = 0,75·√Q (ṁ in g/s, Q in W). Bei Q = 117 W ergibt das ṁ = 8,1 g/s, ΔT_Kreis = 3,4 K und Δp ≈ 14 Pa.
- **Vergleich mit Runde 3:** Dort waren Rohr 20×2 (Reibung 100 Pa) und ein hoch hängender Kühler nötig, deshalb scheiterte der Umlauf. Hier sind die Rohre groß, der Kühler liegt tief und der Kollektor hoch.
- Fittings sind bei diesen Geschwindigkeiten (≈ 1 cm/s) vernachlässigbar (Staudruck 0,07 Pa).

### 6.3 Gleichgewicht je Block (ε-NTU-Modell, Raum aus 6.4)

Der Raumkühler hat 3 × 18 = 54 W/K. Begründung: Der Exponentenansatz n = 1,3 gibt 17,5 W/K je Körper (Nennwert ≈ 2,3 kW bei ΔT_ln = 50 K). Die Zerlegung in Strahlung (≈ 11 W/K, linear) und Konvektion (≈ 14 W/K) gibt ≈ 25 W/K. Ich nehme 18 W/K, also den unteren Wert (Spanne 15 bis 26 W/K).

Formel: Q = C·(T_R − T₀)/(1/ε_R + 1/ε_A − 1), mit C = ṁ·c und ε = 1 − exp(−UA/C).

| Block | Raum | ṁ | ΔT_Kreis | Kühler ein/aus | **Q** |
|---|---|---|---|---|---|
| 1 | 26,3 °C | 5,0 g/s | 2,1 K | 24,0 / 26,2 °C | **45 W** |
| 2 | 26,1 °C | 8,1 g/s | 3,4 K | 21,8 / 25,2 °C | **117 W** |
| 3 | 25,7 °C | 9,0 g/s | 3,8 K | 20,7 / 24,5 °C | **143 W** |

- Nachtmittel: **101,7 W × 10,5 h = 1,07 kWh**, im 24-h-Mittel **44,5 W**.
- Der Kollektor-Sensitivitätsfaktor gegen die Raumtemperatur beträgt ≈ 22 W/K (im Nachtbetrieb) bzw. 9,6 W/K im 24-h-Mittel. Er ist die Rückkopplung Raum ↔ Ertrag.

### 6.4 Zimmerwirkung (periodische Rechnung mit Rückkopplung)

**Zimmer:** 20 m², mittleres Geschoss, Westfenster 3 m² mit Außenrollo (g_ges ≈ 0,12).

**Wärmelast:** Sonne im Mittel 37 W, innen (Schläfer nachts 70 W, Geräte) 33 W, zusammen ≈ 72 W.

**Parameter:**
- Wirksame Masse 3,5 MJ/K
- G_a = 22 W/K (Transmission 12, Lüftung 5, Nachbarräume 5)
- Wirksame Außentemperatur 24,8 °C im Mittel (Blöcke: 24,3 / 23,4 / 23,6 / 25,6 °C)

Es gilt für vier Blöcke (drei Nachtblöcke plus Tag 07:00–20:30). Die Zeitkonstante beträgt nachts 22 h und tagsüber 44 h.

| Zeitpunkt | ohne Gerät | mit Gerät (eingeschwungen) |
|---|---|---|
| 20:30 (Abendspitze) | 28,2 °C | 26,4 °C |
| 07:00 (Frühminimum) | 27,9 °C | 25,5 °C |
| **24-h-Mittel** | **28,1 °C** | **26,0 °C (−2,0 K)** |

- Die Luft liegt tagsüber ≈ 0,3 bis 0,6 K über der Masse (Spitze der Sonnenlast gegen 17 Uhr). Der Tagesgang der Luft ist entsprechend etwas größer als in der Masse-Rechnung.
- **Aufbau:** Tag 1 ≈ −1,0 K, Tag 2 ≈ −1,55 K, Tag 3 ≈ −1,8 K, danach −2,0 K (bei durchgehend gleichem Wetter).

**Sensitivität (24-h-Mittel, Gerät reagiert auf die Raumtemperatur):**

| Fall | ohne Gerät | mit Gerät | Δ |
|---|---|---|---|
| Basis (G_a 22 W/K, 72 W) | 28,1 °C | 26,0 °C | −2,0 K |
| G_a = 15 W/K (gut gedämmt) | 29,6 °C | 26,4 °C | −3,2 K |
| G_a = 40 W/K (viel Lüftung) | 26,6 °C | 25,6 °C | −1,0 K |
| Last 100 W (heißer Raum) | 29,4 °C | 26,9 °C | −2,4 K |
| Last 50 W | 27,1 °C | 25,4 °C | −1,7 K |
| Himmelssicht 0,3 (Balkon darüber) | 28,1 °C | 26,4 °C | −1,7 K |
| Himmelssicht 0,7 (freier Dachbalkon) | 28,1 °C | 25,7 °C | −2,4 K |
| ohne Brüstungsmodul (2 Kollektoren) | 28,1 °C | ≈ 26,3 °C | ≈ −1,8 K |

**Ehrlich zum Ziel ≤ 26 °C:** Es wird im Basisfall knapp erreicht. In heißen, schlecht gedämmten oder verschatteten Räumen liegt man bei 26,4 bis 26,9 °C. Das Außenrollo ist in der Lastannahme schon enthalten (ohne Rollo etwa +0,5 K). Ein Fenster nachts zu öffnen (wo erlaubt) ist meist wirksamer als jedes Wassergerät und ergänzt die Anlage.

### 6.5 Wetter

Ertrag relativ zur Basis (44,5 W) bei festem Raum, mit stationärer Raumtemperatur:

| Nacht | rel. Ertrag | Zimmer 24-h |
|---|---|---|
| klar, trocken (Taupunkt 12 °C) | ≈ 1,12 | 25,9 °C |
| **klar, Auslegungsfall** | **1,00** | **26,0 °C** |
| halb bewölkt (Himmel ≈ +5 K) | ≈ 0,8 | 26,3 °C |
| bedeckt, Nachtluft wie Basis | ≈ 0,6 | 26,6 °C |
| klar, Tropennacht (Luft +3 bis 4 K, T_d 19 °C) | ≈ 0,55 | 26,7 °C |
| bedeckt und Tropennacht | ≈ 0,1 | 27,3 °C |

Entscheidend ist nicht nur der Himmel, sondern der Abstand zwischen Raum und Nachtluft von ≈ 4 K oder mehr. **Wochenmittel** bei einer Hitzewelle (50 % Basis, 15 % trocken, 15 % halb bewölkt, 10 % bedeckt, 10 % Tropennacht): ≈ 0,89 × 44,5 W ≈ 40 W, Zimmer ≈ 26,2 °C.

### 6.6 Kondensation und Feuchte

Der Raumtaupunkt liegt bei ≈ 18,5 bis 20 °C (Außen-Taupunkt 17,4 °C plus Schläfer und Lüftung 0,3 bis 0,5/h). Der kälteste Kühler-Eintritt liegt in Block 3 bei 20,7 °C. **Die Marge beträgt damit 0,7 bis 2,7 K**, bei sehr feuchten Nächten kann Kondensat entstehen.

- Unter jedem Heizkörper sitzt eine **Tropfschale mit Kondensatflasche** (der Kühlkreis bleibt geschlossen, das Kondensat stammt aus der Raumluft).
- Regel: Ein Hygrometer im Raum zeigt den Taupunkt. Bei Raumtaupunkt ≥ 20 °C wird das Brüstungsmodul über die Kugelhähne abgesperrt (weniger Fläche, wärmeres Wasser).
- Der Kollektor liegt mit ≥ 20 °C meist über dem Außen-Taupunkt. Tau darauf mindert den Ertrag nur leicht.

## 7. Gewicht, Wasser, Balkonlast

| Position | kg |
|---|---|
| 3 Absorber inkl. Rahmen und PIR-Rückseite | 30 |
| Rahmen/Pergola (Alu/Holz) | 25 |
| Außen-Rohre (≈ 4 m Cu 35, gedämmt) | 6 |
| Wasser Balkonteil (≈ 7 L) | 7 |
| Kleinteile, MAG, Entlüfter, Anker | 22 |
| **Summe Balkon betriebsbereit** | **≈ 90** |

- **Wasser gesamt ≈ 29 L:** Absorber 3,6 L, Heizkörper 15,6 L, Rohr 9,6 L (0,8 L/m). Einzufüllen sind ≈ 30 L VE-Wasser.
- **Balkonlast:** ≈ 0,9 kN auf 3 m² entsprechen ≈ 0,3 kN/m² gegenüber ≈ 4 kN/m² Auslegungslast (Wohnungsbalkon, Kategorie Z). Der Rahmen steht auf vier Punkten mit Lastverteilern (je ≈ 0,25 kN). Bei Altbau oder Zweifel vorher Vermieter und Statik klären.
- **Windsog:** Böe 25 m/s, c_p ≈ 1,2 ergibt ≈ 1,3 kN Abhebekraft auf der Pergola. Nötig sind **6 Verbundanker M10**, jeder ≥ 1,5 kN Zug mit Sicherheit 1,5.
- **Innen:** 3 Heizkörper à ≈ 45 kg = **135 kg** an Massivwand (Voll- oder Hochlochziegel, Beton) mit je ≥ 4 Schwerlastkonsolen. Trockenbau ist ungeeignet.

## 8. Stückliste (ungefähre Preise)

| Teil | € |
|---|---|
| 3 unverglaste Kupfer-Alu-Absorber, Harfe, ID Steigrohr ≥ 8 mm, ≈ 1,4 m² (Solar-Ersatzteil/B-Ware) | 480 |
| Weißlack (PU/Alkyd, UV-fest, Alu-Grundierung), 2 L | 40 |
| PIR 30 mm alukaschiert, ≈ 5 m² | 60 |
| Rahmen/Pergola, Winkel, 6 Schwerlastanker | 180 |
| 3 × Heizkörper Typ 22, H600 × L1800, PN 6 bis 10 bar | 510 |
| Schwerlastkonsolen, Dübel | 60 |
| Kupferrohr 35×1,5, ≈ 12 m | 190 |
| Pressfittings/Übergänge 35 mm und 15 mm (Zange leihen) | 140 |
| Rohrdämmung 30 mm, UV-fest außen | 60 |
| 4 Vollstrom-Kugelhähne, 3 Entlüfter, Füll-/Entleerhähne | 90 |
| MAG 8 L, Sicherheitsventil 3 bar, Manometer | 45 |
| VE-Wasser ≈ 30 L | 25 |
| 4 Temperaturfühler (DS18B20) + Logger, Hygrometer | 40 |
| Tropfschalen, Kondensatflaschen | 40 |
| Kernbohrung Ø 125 (Leihgerät) + Durchführungsrohr, Kleinteile | 100 |
| **Summe Basis (ohne Muskel-Reserve)** | **≈ 2.060** |
| Muskel-Reserve: Pumpe 12 V, Bypass (2 Kugelhähne, T), Regler (Arduino + MOSFET), AGM 7 Ah + Sicherung | 125 |
| Tretlader: 24-V-Motor als Generator, Reibrad, DC/DC 24→14 V, Sicherung | 130 |
| Falls Rollentrainer nötig | +150 |
| **Summe mit Reserve (Rad vorhanden)** | **≈ 2.315** |

## 9. Bauanleitung

1. **Standort und Freigabe:** Himmelssicht prüfen (mindestens ⅔ frei, Balkon darüber senkt den Ertrag auf ≈ 75 %). Tragfähigkeit und Vermieter/WEG klären (Kernbohrung, Fassadenanbau).
2. **Vortest (empfohlen):** 1 Absorber + 1 Heizkörper + kurze Rohre bauen und in einer klaren Nacht messen. Erwartung: ΔT_Kreis 3 bis 5 K bei Q ≈ 40 W (± 15 W). Ist ΔT deutlich größer, ist die Strömung zu schwach (Luft, Gefälle, Engstellen) oder die Anlage muss auf Pumpenbetrieb.
3. **Rahmen/Pergola** in ≈ 2,2 m Höhe bauen und mit 6 Ankern sichern. Zwei Absorber nebeneinander mit ≈ 5° Neigung. Der **warme Sammler liegt am höheren Ende**, der kalte am tieferen. Der Entlüfter sitzt am höchsten Punkt. Das dritte Modul kommt senkrecht außen an die Brüstung.
4. **Absorber:** entfetten, Alu-Grundierung, 2 Schichten weißer Lack. Rückseite mit 30 mm PIR dämmen.
5. **Innen:** 3 Heizkörper mit Unterkante ≈ 0,3 m an die Massivwand hängen. Anschluss **diagonal: unten kalt ein, oben warm aus**. Die Tropfschalen kommen darunter.
6. **Rohrleitung** aus Cu 35 mit Pressfittings. Die warme Leitung steigt stetig, die kalte fällt stetig, jeweils ≥ 1 cm/m. Entlüfter an allen Hochpunkten, Entleerhähne an allen Tiefpunkten. Alles dämmen, außen UV-fest.
7. **Durchführung:** eine Kernbohrung Ø 125 mm in ≈ 1,1 m Höhe mit Wanddurchführungsrohr (Vermieter fragen). Alternative für Mieter: zwei Edelstahl-Wellrohre DN25 (Solar) durch eine Fensterdurchführungsplatte. Der Mehrwiderstand liegt bei ≈ 1 Pa, also unkritisch.
8. **Befüllen:** VE-Wasser von unten einfüllen, an allen Hochpunkten entlüften. Ein Druck von 1,0 bar kalt am Manometer der Heizkörperebene ergibt ≈ 0,85 bar oben. **Druckprobe mit Wasser** 2,5 bar über 60 min, Fittings mit Papier prüfen. Nach 24 h nochmals entlüften.
9. **Abnahmetest, erste klare Nacht** (Logger an Kollektor-Ein/Aus und Raum): Erwartung um 03:00 Kühler ein/aus ≈ 20,7 / 24,5 °C, ΔT_Kreis ≈ 3,8 K, Q ≈ 143 W.
   - ΔT_Kreis > 6 K: Entlüften, Gefälle, Ventilstellung prüfen, Kondensat kontrollieren.
   - Bleibt es dabei, den Pumpen-Bypass (Muskel-Reserve, 4.4) einbauen und öffnen.
10. **Betrieb:** Nichts schalten. Bei Raumtaupunkt ≥ 20 °C das Brüstungsmodul absperren. Kondensatflasche gelegentlich leeren.
11. **Winter:** Vor Frost komplett entleeren (Entleerhähne, Entlüfter oben öffnen).

## 10. Sicherheit

- **Absturz und Wind:** Rahmen und Absorber fest verankern. Kein Aufenthalt bei Sturm unter der Pergola.
- **Wandlast innen:** Heizkörper ≈ 45 kg je Stück nur an Massivwand mit Schwerlastkonsolen.
- **Stagnation:** Der weiße Absorber erreicht in der Sonne ≈ 45 °C. Das ist mit PN 6 bar, MAG und Sicherheitsventil unkritisch, das Ablassrohr des Ventils führt zum Boden.
- **Wasserschaden:** Kernbohrung sauber abdichten (Rohrdurchführung). Tropfschalen unter jedem Heizkörper kontrollieren. Vor dem Bohren Leitungen orten.
- **Elektrik** (nur bei Reserve): Kleinspannung (Generator ≤ 30 V Leerlauf), 15-A-Sicherung in der Batterieleitung. AGM statt Blei-Säure wegen Gasung im Zimmer.
- **Sport:** 20 bis 40 min bei 75 W sind mäßig. Trinken, danach duschen. Bei Herz-Kreislauf-Vorerkrankung vorher ärztlich klären.
- **Korrosion:** Geschlossener Kreis mit entgastem VE-Wasser, Cu-Rohr, Stahlheizkörper (wie eine normale Heizungsanlage). Nachfüllen nur bei Bedarf (Druckabfall = Leck suchen).

## 11. Grenzen und Vergleich

**Grenzen:**
- Der Umlauf ist die schwächste Stelle: 14 Pa Antrieb und ≈ 20 % Reserve. Luftpolster, Wassersäcke oder Engstellen stoppen ihn. Darum gibt es Vortest, Abnahmetest und Pumpen-Bypass.
- Die Rechnung ist eine Handrechnung mit ±30 % Unsicherheit. Am stärksten wirken Himmelssicht, Nachtluft und Raumdaten (G_a, Last). Das Zimmermodell ist ein Ein-Knoten-Modell mit Masse. Tageszeitliche Luftspitzen sind etwas höher.
- Der Ertrag hängt an einem Nachtabstand ≥ 4 K zwischen Raum und Luft. In Tropennächten mit Bedeckung sinkt er auf ≈ 10 %.
- **Klimaanlagen-Niveau (−5 K) ist damit nicht erreichbar.** Das Ziel ≤ 26 °C wird nur knapp erfüllt.
- **Muskelkraft trägt nichts bei.** Wer trotzdem tritt, macht Sport, keine Kühlung: 20 min am Tag kosten ≈ 2 W Zimmerwärme (≈ 0,1 K).

| | Durchlauf 2 (Zeolith) | Runde 3 (Muskelpumpe) | **Diese Lösung (freier Umlauf)** |
|---|---|---|---|
| Kälte/Tag | ≈ 1 kWh (Klartag) | ≈ 0,9 kWh (klare Nacht) | **≈ 1,07 kWh** (klare Nacht) |
| Zimmer 24-h-Mittel | — | −1,6 K (ohne Rückkopplung) | **−2,0 K** (mit Rückkopplung) |
| Antrieb | Sonne | Nachthimmel + 25 Wh Muskel | **Nachthimmel + Schwerkraft** |
| Muskel nötig | nein | 20 min/Tag | **nein** (Reserve ≈ 40 min/Tag) |
| Gewicht Balkon | 470 kg | ≈ 100 kg | ≈ 90 kg (+ 135 kg innen) |
| Kosten | 12 bis 18 k€ | ≈ 1,7 k€ | ≈ 2,1 k€ (2,3 k€ mit Reserve) |
| Vakuum/Sonderteile | ja | nein | **nein** |
| DIY | nein | ja | ja |

## 12. Energiebilanz (24-h-Mittel, Auslegungsfall)

Alle Werte sind 24-h-Mittel des Auslegungstags. Die Nachtwerte sind auf die 10,5 h Betriebszeit umgerechnet (Faktor 0,4375), tagsüber ist der Umlauf gesperrt (Diode, Leckwärme ≈ 0,7 W vernachlässigt). Der Tretlader ist im Normalbetrieb aus und daher nicht enthalten. Sein Reservebetrieb ist in 4.4 beziffert. Die Knotentemperaturen sind flussgewichtete Nachtmittel.

```json
{
  "knoten": {
    "Wohnung": {"T_C": 26.0, "rolle": "umgebung"},
    "Raumkuehler": {"T_C": 23.3, "rolle": "komponente"},
    "Kollektor": {"T_C": 22.8, "rolle": "komponente"},
    "Himmel": {"T_C": 9.1, "rolle": "umgebung"},
    "Nachtluft": {"T_C": 21.9, "rolle": "umgebung"},
    "Balkonumfeld": {"T_C": 24.5, "rolle": "umgebung"}
  },
  "stroeme": [
    {"von": "Wohnung", "nach": "Raumkuehler", "W": 44.5, "art": "waerme"},
    {"von": "Raumkuehler", "nach": "Kollektor", "W": 44.5, "art": "waerme"},
    {"von": "Balkonumfeld", "nach": "Kollektor", "W": 8.7, "art": "strahlung"},
    {"von": "Kollektor", "nach": "Himmel", "W": 50.0, "art": "strahlung"},
    {"von": "Kollektor", "nach": "Nachtluft", "W": 3.2, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Wohnung", "T_ein_C": 28.1, "T_aus_C": 26.0, "kuehlleistung_W": 44.5},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```