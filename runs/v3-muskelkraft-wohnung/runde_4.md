# Zimmer kühlen mit Muskelkraft: Nachtstrahler-Kreis mit muskelgeladener Pumpe (Runde 4)

## 1. Kurzfazit

- **Ehrliche Rollenverteilung:** Mit reinem Wasser und Selbstbau ist Muskelkraft kein Kälteerzeuger. Die Kälte kommt zu 100 % aus dem klaren Nachthimmel und der kühleren Nachtluft. Die Muskeln treiben nur die Umwälzpumpe und den Regler an, also die Rolle des Schalters, nicht die der Kältemaschine. Die Kennzahl „Wh Kälte je Wh Tretarbeit“ aus Runde 3 wird gestrichen, weil sie eine Leistungszahl vortäuscht. Aussagekräftig ist nur die Netto-Bilanz des Zimmers (Abschnitt 5.5 und 5.6).
- **Gerät:** Ein geschlossener Wasserkreis verbindet drei weiße Flachheizkörper auf dem Balkon (2,7 m², 20° geneigt, nachts Strahler) mit drei Heizkörpern im Zimmer. Die Pumpe läuft nur nachts, aus einer 12-V-Batterie, die auf dem Fahrrad geladen wird. Es gibt keinen Dampf, kein Vakuum und keinen Wasserverlust. Tagsüber steht die Pumpe.
- **Ertrag der klaren Auslegungsnacht:** ≈ 1,05 kWh in 10,5 h (Spanne 0,6 bis 1,3 kWh). Das sind 44 W im 24-h-Mittel.
- **Tretaufwand (Basisfall):** 1× täglich 40 min bei 90 W (60 Wh mechanisch). Die Spanne ist 27 bis 60 min, je nach Pumpe (1,5 bis 4 W).
- **Wärme des Tretenden im Zimmer:** ≈ 172 Wh pro Runde (Spanne 100 bis 260 Wh), also 7,2 W im 24-h-Mittel. Das ist 6-mal weniger als die abgeführte Kälte.
- **Zimmer:**

  | Bedingung | Mittel ohne Gerät | Mittel mit Gerät | Effekt |
  |---|---|---|---|
  | Klare Nächte, Dauerzustand nach ≈ 3 Tagen | 28,0 °C | **≈ 26,3 °C** | −1,7 K |
  | Gemischtes Wetter (Wochenmittel) | 28,0 °C | ≈ 26,7 °C | −1,3 K |

  Das Ziel ≤ 26 °C wird knapp verfehlt. Mit der Ausbaustufe (5.6) ergibt sich ≈ 26,1 °C, mit gut gedämmtem Zimmer ≈ 25,9 °C. Nachts lüften ist wirksamer als jedes Wassergerät, wo es geht.
- **Praxis:** Der Balkonteil wiegt ≈ 100 kg. Die Kosten liegen bei ≈ 1,6 k€ (1,4 bis 2,0 k€). Das Gerät ist selbst baubar, ohne Löten, Vakuum oder Druckbehälter.

## 2. Was gegenüber Runde 3 korrigiert wurde

| Kritikpunkt | Änderung |
|---|---|
| Muskel „nur Dekoration“, Kennzahl 36 Wh/Wh irreführend | Kennzahl gestrichen. Die Rolle ist klar benannt: Muskel = Pumpenantrieb. Direktmechanische Antriebe (Gewicht, Uhrwerk) sind mit korrigierter Rechnung geprüft (5.7), ebenso der Nutzen von Zusatz-Tretarbeit. |
| Pumpenbedarf optimistisch, „Motorwirkungsgrad 0,3 %“ falsch benannt | Hydraulik ≈ 5 mW, Gesamtwirkungsgrad der Pumpe 0,2 bis 0,5 %. Basis 2,5 W, Spanne 1,5 bis 4 W, Messpflicht mit 12-V-Strommesser. Tretzeit als Spanne. |
| Innenkühler 45 W/K schöngerechnet | Rechnung nach Exponentengesetz (n = 1,3): ≈ 20 W/K je Typ 22 bei ΔT 2,5 K. Standard sind 3 Körper (60 W/K). Die 2-Körper-Variante ist als Sensitivität gerechnet. |
| Nachtbilanz nicht geschlossen | Drei Zeitblöcke (Abend, Mitternacht, Morgen) mit eigener Luft-, Himmels- und Raumtemperatur. Die Raumrückkopplung ist in der Formel in 5.6 geschlossen. |
| Taupunkt inkonsistent | Wasserdampfgehalt konstant, Taupunkt ≈ 17 °C. Die r. F. steigt von 45 % (28 °C) auf 81 % (20 °C). Der Himmel wird pro Block nach Berdahl-Martin gerechnet. |
| Sensitivität auf G_a, Last, Himmelssicht, Wetter fehlte | Tabellen in 5.6. Die 3-Tage-Annahme „nur klare Nächte“ wird durch ein Wochenmittel mit Wetterverteilung ersetzt. |
| Außenheizkörper: liegend, Entlüftung, Fläche | Kleinere Körper (3 × H900 × L1000, 20° geneigt, Sammelleitung am Hochpunkt, je Körper ein Entlüfter). Fläche 2,7 m², passt in 1 × 3 m. 15 % der Fläche sind als nicht durchströmt abgezogen. Erst ein Prototyp mit 1 Körper (Bauschritt 1), dazu eine Alternative. |
| Tretenden-Bilanz zu glatt | Schweiß 100 g verdunstet (nicht 25 g), Nachlaufwärme im Zimmer, alles als Spanne. |
| Rechenfehler Gewicht-Pumpe (0,5 Wh) | Korrigiert: hydraulisch 0,07 Wh/Nacht, mechanisch bei η = 15 % ≈ 0,5 Wh = 50 kg × 3,6 m. |
| Wasserinhalt unklar, Regler nicht beschaffbar | Inhalt ≈ 33 L, gekauft werden 40 L. Regler als Arduino/ESP32 mit Pseudocode. |
| Ziel verfehlt | Rollo und Ausbaustufe sind als Mindestausstattung für das Ziel benannt. |

## 3. Prinzip

Zwei frühere Erkenntnisse bleiben bestehen. Ein geschlossener Verdunsten-Kondensieren-Kreis ohne Druckhub kühlt nicht, und offene Verdunstung verliert Wasser. Deshalb gibt es hier **keinen Phasenwechsel**. Es ist reine Wärmeübertragung von einer wärmeren Quelle (Zimmer, 25 bis 28 °C) an eine kältere Senke (Nachthimmel und Nachtluft, effektiv ≈ 18 bis 23 °C). Ein Druckhub ist nicht nötig, denn die Wärme fließt von selbst bergab.

1. **Senke:** Eine weiße Fläche (ε ≈ 0,9 im Fenster 8 bis 13 µm) strahlt nachts zum Himmel. Der Himmel ist wegen des Taupunkts ≈ 17 °C nur 3 bis 15 K kälter als die Luft. Zusammen mit der Konvektion wirkt die Fläche wie ein Trockenkühler, der 2 bis 3 K unter Luftniveau kühlt.
2. **Transport:** Der Wasserkreis holt die Wärme aus den Raumkühlern und bringt sie zu den Strahlern.
3. **Speicher:** Die Kälte wird in der Bausubstanz des Zimmers (≈ 3,5 MJ/K) und in der Batterie gespeichert (Chemie, für die Pumpe). Der Effekt wirkt weiter, wenn der Tretende längst im Bad ist.
4. **Tagsperre:** Tagsüber steht die Pumpe. Die weiße Fläche heizt sich in der Sonne auf ≈ 45 bis 55 °C. Weil die Strahler **höher hängen als die Raumkühler**, entsteht keine Schwerkraftzirkulation in die falsche Richtung. Heißes Wasser bleibt oben.
5. **Muskel:** Er lädt die Batterie. Die Batterie treibt Pumpe und Regler nachts.

**Warum nicht mehr Muskel?** In Abschnitt 5.7 sind Wasserdampf-Verdichter, Sorption, Peltier, Lüfter und Gewichtsantrieb durchgerechnet. Nur die Pumpe ergibt netto Sinn.

## 4. Aufbau

```
 BALKON (1 × 3 m)                 Seitenansicht
        Himmel (klar, Ø ≈ 10 °C)   ↑ ↑ ↑ Abstrahlung nachts
              ╱ ╱ ╱   3 × Typ 10, H900 × L1000, weiß, ca. 20° geneigt
   ┌──────────────────────┐   Hochpunkt = Sammelleitung + je Körper ein Entlüfter
   │ Strahler 2,7 m²      │   Rückseite 30 mm PIR gedämmt
   └──┬─────────────┬─────┘   Tiefpunkt der Strahler ≥ 2,0 m über Boden
 Vorlauf (kalt)   Rücklauf (warm)   PEX-Al 20×2, gedämmt, Tichelmann-Verteilung
      │             ▲
  ┌───┴───┐         │   Pumpe 12 V (Ziel ≤ 2,5 W, PWM), Regler (ESP32),
  │ Pumpe │◄ 3 Fühler   MAG 5 L, Sicherheitsventil 3 bar, Manometer
  └───┬───┘         │   Kreis im Balkonteil ≈ 12 L
══════╪═════════════╪══════ Fensterspalt / Balkontür / Kernbohrung ═══
 ZIMMER ▼           │
  ┌──────────────────┴──────────┐  3 × Typ 22, H600 × L1600, weiß,
  │ Raumkühler, Unterkante ≥1,2m│  auf 2 Wände verteilt, Massivwand,
  │ Oberkante ≤ 1,8 m (unter    │  Hochpunkt unter dem Strahler-Tiefpunkt
  │ dem Strahler-Tiefpunkt)     │  Kaltluft fällt in den Raum
  └─────────────────────────────┘
 Muskelseite (im Zimmer):
 Rollentrainer → Reibrad → 24-V-PM-Gleichstrommotor als Generator
   → Sicherung/Diode → DC/DC-Wandler (CC/CV, 14,4 V) → AGM 12 V 12 Ah → Pumpe/Regler
```

**Regelung (ESP32 oder Arduino, 3 DS18B20, MOSFET/PWM), Pseudocode:**
```
T_S = Strahler-Auslauf,  T_R = Raumkühler-Rücklauf,  T_V = Raumkühler-Vorlauf
Pumpe EIN wenn  T_S < T_R − 1,0 K  UND  T_S < 26 °C  UND  Batterie > 11,8 V
Pumpe AUS wenn  T_S > T_R − 0,5 K  ODER  T_V < 19 °C (Kondensschutz) ODER Batterie < 11,5 V
Tagsüber: T_S > T_R → Pumpe AUS (Sperre)
Sicherheit: T_S > 60 °C → Pumpe AUS und Fehlermeldung
Durchfluss über PWM auf ≈ 50 L/h einstellen (einmalig per Eimer und Stoppuhr)
```
Fertige 12-V-Differenzregler gibt es in Online-Shops, die Qualität schwankt. Übliche solarthermische Regler sind 230-V-Geräte und für Kleinspannung ungeeignet. Ein Arduino-Aufbau ist deshalb die ehrlichere Lösung.

## 5. Rechnung

### 5.1 Luft, Feuchte, Himmel (Zeitblöcke der Auslegungsnacht)

Wasserdampfdruck tagsüber: 40 % × 47,6 hPa = 19,0 hPa. Das ergibt einen **Taupunkt von ≈ 17 °C**, der sich nachts kaum ändert. Die r. F. steigt von 45 % (28 °C) auf 81 % (20 °C).

Himmelstemperatur nach Berdahl-Martin: ε_Himmel = 0,711 + 0,56·(T_d/100) + 0,73·(T_d/100)² + 0,013·cos(2π·t/24) ≈ 0,83 bis 0,84.

| Block | Zeit | Luft | Himmel | Umgebung (Fassade) | Dauer |
|---|---|---|---|---|---|
| A Abend | 20:30–23:30 | 26,0 °C | 13,1 °C | 27,0 °C | 3,0 h |
| B Nacht | 23:30–03:30 | 22,5 °C | 9,9 °C | 25,0 °C | 4,0 h |
| C Morgen | 03:30–07:00 | 20,5 °C | 7,2 °C | 23,5 °C | 3,5 h |
| Mittel | | 22,8 °C | 9,9 °C | 25,2 °C | 10,5 h |

### 5.2 Strahlungs- und Konvektionssenke (je m², horizontal)

**Annahmen:** ε = 0,9, Himmelssichtfaktor 0,5, Konvektion h = 6 W/m²K (Wind 0 bis 3 m/s). Der Strahlungsanteil der Umgebung ist mitgerechnet.

Aus q = 0,9·σ·[0,5·(T_p⁴ − T_Himmel⁴) + 0,5·(T_p⁴ − T_Umg⁴)] + h·(T_p − T_Luft) = 0 folgt die Nullstelle **T_ref**. Die Steigung liegt bei ≈ 11,3 W/m²K.

| Block | T_ref (q = 0) | Steigung |
|---|---|---|
| A | 23,3 °C | 11,3 W/m²K |
| B | 20,3 °C | 11,1 W/m²K |
| C | 18,3 °C | 11,1 W/m²K |

Bei einer Plattentemperatur von 23,8 °C ergeben sich 39,6 W/m². Das passt zur Tabelle aus Runde 3 (31 W/m² bei 23 °C, 42 W/m² bei 24 °C).

**Kein Tau:** Die Platte liegt in Block C bei ≥ 22 °C, der Taupunkt ist 17 °C. Kondensation an den Strahlern ist damit ausgeschlossen. Der Regler sperrt den Vorlauf bei < 19 °C (Raumkühler-Taupunkt).

### 5.3 Kreislauf (NTU-Rechnung, Durchfluss 50 L/h, C = 58 W/K)

- **Außenseite:** G_out = 2,7 m² × 11,3 W/m²K × 0,85 = **25,9 W/K**. Der Faktor 0,85 berücksichtigt nicht durchströmte Zonen und Wasserkurzschluss. Damit ist ε_out = 1 − exp(−25,9/58) = 0,360.
- **Innenseite:** Bei 3 × Typ 22 (Nenn ≈ 2,5 kW bei ΔT_ln = 49,8 K) ist G = Q_N/ΔT_N · (ΔT/ΔT_N)^0,3 ≈ 20,4 W/K je Körper bei ΔT 2,5 K. Für 3 Körper sind das **G_in = 60 W/K** und ε_in = 1 − exp(−60/58) = 0,644.
- **Kreislauf in Reihe (Ableitung):** Q = C·ΔT_ges · ε_in·ε_out / (ε_in + ε_out − ε_in·ε_out) = 58 × 0,300 × ΔT_ges = **17,4 W/K × (T_Raum − T_ref)**. Der Grenzwert bei unendlichem Durchfluss ist 18,1 W/K.

| Block | T_Raum (mit Gerät) | T_Raum − T_ref | Q | Energie |
|---|---|---|---|---|
| A | 27,2 °C | 3,9 K | 68 W | 204 Wh |
| B | 26,4 °C | 6,1 K | 106 W | 424 Wh |
| C | 25,4 °C | 7,1 K | 124 W | 432 Wh |
| **Nacht** | | | Ø 101 W | **1.060 Wh** |

Abzüglich ≈ 10 Wh für die Pumpenabwärme im Wasser ergeben sich **1.050 Wh je Nacht** und **43,8 W im 24-h-Mittel**.

**Gegenprobe der Strahler (Blockweise):** Bei den Plattentemperaturen 25,5 / 23,8 / 22,4 °C gilt:
- Abstrahlung zum Himmel: 85 / 94 / 100 W
- Konvektion: −8 / +21 / +31 W
- Umgebungsstrahlung (Gewinn): 11 / 9 / 8 W
- Netto: 67 / 106 / 123 W, also gleich Q.

**Wassertemperaturen im Betrieb (Block B):** Vorlauf zum Raumkühler 23,6 °C, Rücklauf 25,4 °C, Mittel 24,4 °C. Die Platte liegt bei 23,8 °C. Der Morgen (Block C) ist am kältesten (Vorlauf ≈ 22,1 °C, immer über dem Kondensschutzlimit 19 °C).

**Kein Klimagerät-Niveau:** 100 W entsprechen 0,35 kW Kälte pro Stunde Betrieb, also etwa einem kleinen Splitgerät im Standby. Der Nutzen liegt in den 10,5 Betriebsstunden pro Nacht bei null Netzstrom.

### 5.4 Pumpe und Muskelenergie

- **Hydraulik:** Rohr 20×2 (Innendurchmesser 16 mm), 20 m, laminar bei v = 0,069 m/s (Re ≈ 1.200): 7,8 Pa/m → 156 Pa. Dazu Körper (parallel) ≈ 80 Pa und Formstücke ≈ 100 Pa, Summe ≈ 350 Pa. P_hyd = 13,9·10⁻⁶ m³/s × 350 Pa ≈ **5 mW**.
- **Gesamtwirkungsgrad kleiner Pumpen:** 0,2 bis 0,5 %, das sind 1,5 bis 4 W elektrisch. Ein Handelsprodukt ist nicht vorgeschrieben, verlangt ist: 12-V-Bürstenlospumpe mit PWM-Eingang, Nennleistung 4 bis 8 W, gedrosselt auf 50 L/h. Die Aufnahme wird mit einem 12-V-Strommesser (≈ 15 €) geprüft. Sollwert ≤ 2,5 W. Ein Durchfluss von 30 statt 50 L/h senkt Q um ≈ 15 % und die Pumpenleistung deutlich.
- **Regler:** ≈ 0,2 W × 24 h = 4,8 Wh.
- **Kette Muskel → Pumpe:** Reibrad 0,95 × Generator 0,72 × DC/DC 0,90 × Laden 0,92 = 0,566, dann Entladen 0,92, gesamt **η = 0,52**.

| Fall | Pumpe | el./Nacht | mech./Tag | Tretzeit (90 W) |
|---|---|---|---|---|
| günstig | 1,5 W | 20,6 Wh | 40 Wh | 26 min |
| **Basis** | **2,5 W** | **31,1 Wh** | **60 Wh** | **40 min** |
| ungünstig | 4,0 W | 46,8 Wh | 90 Wh | 60 min (besser 2 × 30) |

**Batterie:** AGM 12 V 12 Ah (144 Wh, nutzbar 50 % ≈ 72 Wh) trägt ≈ 2,3 Nächte. Trotzdem ist täglich kurz treten besser als selten lang (Körperspeicher, 5.5).

**Notbetrieb:** Fällt das Treten aus (Krankheit, Urlaub), bleibt die Pumpe stehen, das Zimmer wird nicht wärmer als ohne Gerät. Ein 10-W-Solarmodul am Balkon wäre die Ausnahmelösung, die Vorgabe erlaubt sie nur, wenn es nicht anders geht. Hier geht es anders, also ist keins eingebaut.

### 5.5 Ehrliche Bilanz des Tretenden (Basisfall: 40 min, 90 W)

| Größe | Wert |
|---|---|
| Mechanische Arbeit | 90 W × 40 min = 60 Wh |
| Umsatz bei η = 0,23 | 391 W, 260,9 Wh |
| Körperwärme | 301 W, 200,9 Wh |
| Im Körper gespeichert (75 kg × 3,47 kJ/kgK = 72 Wh/K, Ø-Körpertemperatur +0,9 K; Spanne 50 bis 80 Wh) | 65 Wh, geht ins Bad |
| Abgabe im Zimmer während des Tretens | 136 Wh (203 W): fühlbar ≈ 68 Wh, latent ≈ 68 Wh entsprechend ≈ 100 g verdunstetem Schweiß (insgesamt 100 bis 150 g Schweiß, der Rest tropft in Handtuch und Kleidung und geht mit ins Bad) |
| Nachlauf beim Absteigen und Abtrocknen im Zimmer (5 bis 10 min) | 10 Wh (Spanne 5 bis 20 Wh) |
| Kette Reibrad/Generator/Wandler/Batterie im Zimmer (60 − 31,3 Wh) | 28,7 Wh |
| **Wärme ins Zimmer je Runde** | **≈ 175 Wh** (Spanne 140 bis 230 Wh) |
| Mit ins Bad | ≈ 55 Wh (65 Wh gespeichert, 10 Wh gleich danach im Zimmer abgegeben) |

Im 24-h-Mittel sind das **7,3 W**. Die verdunstete Schweißmenge erhöht die Luftfeuchte um ≈ 1,7 g/m³ (≈ +7 % r. F. kurzzeitig). Der Kondensschutz (Vorlauf ≥ 19 °C) bleibt deshalb wichtig.

**Spannen je nach Pumpe:**

| Fall | Mech. | Zeit | Wärme ins Zimmer |
|---|---|---|---|
| günstig | 40 Wh | 26 min | ≈ 105 Wh |
| Basis | 60 Wh | 40 min | ≈ 175 Wh |
| ungünstig, 1 Runde | 90 Wh | 60 min | ≈ 260 Wh |
| ungünstig, 2 × 30 min | 90 Wh | 2 × 30 min | ≈ 210 Wh |

Kürzere Runden sind günstiger, weil der Körper am Anfang viel Wärme speichert.

**Nötige Leistungszahl** (Zimmerwärme je Wh Tretarbeit, Break-even über den ganzen Ablauf):

| Fall | COP_min |
|---|---|
| günstig | 2,6 |
| Basis | 2,9 |
| ungünstig (1 Runde) | 2,9 |
| ungünstig (2 Runden) | 2,3 |
| Zusatzarbeit (Grenznutzen bei verlängerter Runde) | ≈ 3,7 |

Eine echte Kältemaschine mit Muskelantrieb müsste mehr als 3 W Kälte je W Tretleistung liefern. Das schafft nur ein Verdichter mit Wasserdampf oder Sorption, beides ist nicht DIY (5.7).

**Was das Gerät stattdessen liefert:** 1.050 Wh Kälte je Nacht bei 175 Wh Zimmerwärme des Tretens, also ein Verhältnis von **≈ 6 : 1** (netto +875 Wh je 24 h). Das ist keine Leistungszahl der Maschine, sondern der Nutzen eines sparsamen Antriebs für einen passiven Strahler.

**Tipp:** Wer morgens (ab 06:30) bei geöffnetem Fenster tritt, lüftet Körperwärme und Schweißfeuchte hinaus, solange draußen ≈ 20 °C herrschen. Die Zimmerlast sinkt dann auf grob ein Drittel (≈ 60 Wh). Das Fenster wird danach geschlossen. In der Bilanz unten ist der ungünstigere Fall (Fenster zu) gerechnet.

### 5.6 Zimmereffekt

**Zimmer:** 20 m² Schlafzimmer, mittleres Geschoss, Westfenster 3 m² mit **Außenrollo (Voraussetzung, nicht Zusatz)**, Fenster tagsüber zu.

**Last (24-h-Mittel):**
- Sonne durch das Fenster (g_ges ≈ 0,12): 37 W
- Innen (Geräte, Schlafender): 33 W
- Summe: **70 W**

**Kopplung an außen (G_a = 22 W/K):** Transmission 12, Lüftung 5, Nachbarräume 5. Die wirksame Außentemperatur ist 24,8 °C (Mittel aus Außenluft ≈ 26 °C und kühleren Nachbarräumen). Ohne Gerät ist T₀ = 24,8 + 70/22 = **28,0 °C** (Schwankung ±0,8 K).

**Massen:** C_Masse ≈ 3,0 MJ/K (60 m² × 5 cm wirksam), C_Luft und Möbel ≈ 0,5 MJ/K, Kopplung Luft-Masse 250 W/K. Die Zeitkonstante beträgt ≈ 33 h.

**Netto-Kälte:** 43,8 W − 7,3 W = **36,5 W** (24-h-Mittel). Der Effekt beträgt −36,5/22 = **−1,66 K** (→ 26,3 °C). Er baut sich auf: Tag 1 −0,9 K, Tag 2 −1,3 K, Tag 3 −1,5 K, Dauerzustand −1,7 K.

**Tagesgang:** Die Nachtleistung (68 / 106 / 124 W, sonst 0) hat als Grundschwingung ≈ 66 W Amplitude. Das gibt ±0,26 K Raumeffekt, maximal kühl gegen 08:00. Damit ergeben sich (Tag 3 oder später):

| Zeitpunkt | ohne Gerät | mit Gerät |
|---|---|---|
| Frühminimum 07:00 | 27,2 °C | ≈ 25,3 °C |
| Abendspitze 20:30 | 28,8 °C | ≈ 27,4 °C |
| 24-h-Mittel | 28,0 °C | **≈ 26,3 °C** |

**Rückkopplung geschlossen:** Kühlere Raumluft senkt den Ertrag. Mit dQ/dT_Raum = 17,4 W/K × 10,5/24 = 7,6 W/K (24 h) gilt T = (G_a·T₀ + 163,4)/(G_a + 7,6). Für den Basisfall folgt (22·28 + 163,4)/29,6 = 26,3 °C.

**Sensitivität auf Zimmer und Last:**

| Fall | G_a | T₀ (ohne) | T (mit) | Effekt |
|---|---|---|---|---|
| **Basis** | 22 W/K | 28,0 °C | **26,3 °C** | −1,7 K |
| gut gelüftet/undicht | 40 W/K | 27,2 °C | 26,3 °C | −0,9 K |
| Last +40 W (Rollo defekt) | 22 W/K | 29,8 °C | 27,7 °C | −2,1 K |
| gut gedämmt, Last 50 W | 15 W/K | 28,1 °C | 25,9 °C | −2,2 K |

Ein hoher Luftwechsel senkt den Effekt (−0,9 K), ohne dass es dann wärmer als 26,3 °C bleibt, denn das Zimmer folgt dann der Nachtluft.

**Sensitivität auf Auslegung (klare Nacht, Basis-Zimmer):**

| Änderung | Q_Nacht | Effekt |
|---|---|---|
| Basis (3 Innenkühler, f_Himmel 0,5) | 1,05 kWh | −1,7 K |
| Nur 2 Innenkühler (G_in = 40 W/K) | 0,92 kWh | −1,4 K |
| Schlechte Himmelssicht 0,35 (T_ref +0,9 K) | 0,90 kWh | −1,35 K |
| Gute Himmelssicht 0,65 | 1,2 kWh | −1,95 K |
| Ausbaustufe: + 2 Brüstungspaneele (0,7 m² wirksam) | 1,24 kWh | −1,9 K (→ 26,1 °C) |

**Wetter (Wochenmittel, heiße Periode):** 60 % klare Nächte (Faktor 1,0), 25 % halb bewölkt (0,6), 15 % bedeckt (0,15) ergeben einen Faktor 0,77. Die Pumpe läuft in bedeckten Nächten kaum, es wird dann auch weniger getreten (≈ 0,85 der Tretlast). Damit ist T = 26,7 °C und der Effekt **−1,3 K** (Spanne −0,7 bis −1,7 K).

**Ziel ≤ 26 °C:** Es wird im Basisfall nicht sicher erreicht, in der Ausbaustufe knapp (26,1 °C) und im gut gedämmten Zimmer erreicht. Nachts das Fenster zu öffnen bringt −1 K und mehr, wo das möglich ist.

### 5.7 Muskeloptionen (durchgerechnet)

| Option | Ergebnis |
|---|---|
| **Wasserdampf-Verdichter** (15 °C/17 mbar → 35 °C/56 mbar) | Für 0,4 kW Kälte sind ≈ 45 m³/h Saugvolumen nötig. Ideal COP ≈ 13, real 4 bis 5. Mit 60 Wh mechanisch wären das 240 bis 300 Wh Kälte gegen 175 Wh Zimmerwärme, netto +70 bis +130 Wh, also 7 bis 12 % der Nachtkälte. **Nicht DIY** (vakuumdichte Welle, Klappen für < 5 mbar). |
| Sorption mit Muskelwärme regenerieren | 60 Wh Reibungswärme ergeben ≈ 30 Wh Kälte, COP < 1. |
| Peltier am Generator | 31 Wh elektrisch × COP 0,5 bis 0,8 ≈ 16 bis 25 Wh Kälte, weit unter COP_min. |
| Zusatz-Lüfter am Raumkühler (Gebläsekonvektor) | G_in 60 → 120 W/K bringt +18 % Q (+190 Wh/Tag). Kosten: ≈ 30 Wh mechanisch mehr (≈ +110 Wh Zimmerwärme). Netto +80 Wh/Tag, also −0,15 K. Nicht empfohlen. |
| Gewicht/Uhrwerk direkt als Pumpenantrieb | Hydraulik 5 mW × 10,5 h = 0,05 Wh. Mechanisch bei η = 15 % ≈ 0,35 Wh. Das entspricht 50 kg × 2,5 m (bei η = 5 % wären es 50 kg × 7,5 m). Theoretisch macht das die Tretzeit von 40 min auf 2 bis 3 min kleiner. Praktisch braucht es eine 10-h-Hemmung und ein Getriebe für 350 Pa Druck, für Laien eine Bastelei mit Ausfallrisiko. Deshalb ist die Batterie die robuste Basis. Wer eine funktionierende Uhrwerks-Pumpe baut, spart den Rollentrainer. |
| Feder/Schwungrad | Speichert nur Sekunden bis Minuten, für 10 h unbrauchbar. |
| Barometrisches Vakuum / Strahlpumpe | Unmöglich (10 m Wassersäule bzw. Dampfdruck des Treibwassers). |
| Schwerkraftumlauf statt Pumpe | Auftrieb bei 1,5 bis 2 K und 2 m Höhe ≈ 5 bis 8 Pa. Selbst bei Rohr 32×3 (≈ 70 Pa Verlust) reicht das nicht. Verworfen. |
| **Batterie + Kleinpumpe** | DIY, netto positiv. Gewählt. |

## 6. Gewicht und Balkonlast

| Position | kg |
|---|---|
| 3 × Typ 10 H900 × L1000 (je ≈ 12 kg) | 36 |
| Wasser Balkonteil (≈ 12 L) | 12 |
| Rahmen/Pergola (Alu/Holz) | 25 |
| Rohre, Dämmung, Pumpe, MAG, Batteriebox | 25 |
| **Balkon betriebsbereit** | **≈ 100** |

Das sind ≈ 1 kN auf 3 m², also ≈ 0,33 kN/m² gegenüber ≈ 4 kN/m² Auslegungslast (DIN EN 1991-1-1, Kategorie Z). Die Last steht auf vier Punkten mit Lastverteilern. Bei Altbau oder Zweifel vorher Vermieter und Statik fragen.

**Windsog:** Bei einer Böe von 25 m/s gilt q ≈ 375 Pa, mit c_p ≈ 1,2 also ≈ 450 Pa auf 2,7 m² und ≈ 1,6 kN Abhebekraft (mit Rahmen). Gefordert sind mindestens 4 Schwerlastanker mit je ≥ 1,5 kN Zug (Sicherheitsfaktor 1,5).

**Zimmer:** 3 × Typ 22 H600 × L1600 (je ≈ 35 kg + 7 L Wasser ≈ 42 kg, zusammen ≈ 126 kg). Aufhängung nur an Massivwand (Voll-/Hochlochziegel, Beton) mit Schwerlastkonsolen (je ≥ 4 pro Körper), auf zwei Wände verteilt. Trockenbau ist ungeeignet.

**Wasserinhalt gesamt:** Strahler 6,6 L, Raumkühler ≈ 20 L, Rohr ≈ 5 L, zusammen ≈ 33 L. Gekauft werden 40 L.

## 7. Stückliste (ungefähre Preise)

| Teil | € |
|---|---|
| 3 × Flachheizkörper Typ 10, H900 × L1000, weiß, PN 6 bar (Strahler) | 210 |
| Rahmen/Pergola, Winkel, 4 Schwerlastanker | 150 |
| Rückseitendämmung PIR alukaschiert 30 mm, ≈ 3 m² | 40 |
| 3 Entlüfter, 4 Kugelhähne, Füll-/Entleerhahn, Luftabscheider | 70 |
| 3 × Flachheizkörper Typ 22, H600 × L1600, weiß (Raumkühler) | 420 |
| Schwerlastkonsolen + Dübel | 60 |
| PEX-Al-PEX 20×2, ≈ 25 m, Pressfittings, T-Stücke | 165 |
| Rohrdämmung 20 mm, ≈ 20 m | 40 |
| MAG 5 L, Sicherheitsventil 3 bar, Manometer | 45 |
| Füllwasser VE, 40 L | 30 |
| Pumpe 12 V, Bürstenlos, PWM-fähig | 40 |
| Regler: ESP32/Arduino, MOSFET, 3 × DS18B20, Gehäuse | 35 |
| AGM 12 V 12 Ah, Sicherung 15 A, Kabel, Voltmeter | 60 |
| 24-V-PM-Gleichstrommotor 250 W, Reibrad + Halter, DC/DC (CC/CV 14,4 V, 10 A), Diode | 130 |
| Zusatzfühler/Logger, 12-V-Strommesser | 35 |
| Kleinteile, Miete Pressfittingzange | 90 |
| **Summe (Fahrrad vorhanden, Außenrollo vorhanden)** | **≈ 1.620** |
| Rollentrainer, falls nötig | + 150 |
| Außenrollo, falls nötig | + 200 bis 400 |
| Ausbaustufe (2 Brüstungspaneele, Konsolen) | + 250 |

## 8. Bauanleitung

1. **Standort:** Himmelssicht prüfen (mindestens ⅔ des Himmels frei, ein Balkon direkt darüber halbiert den Ertrag). Statik und Vermieter klären.
2. **Prototyp zuerst:** 1 Strahlerkörper mit Rahmen, Pumpe, 2 Fühlern und einem Eimer als „Raumkühler-Ersatz“ (Wasserbad, Wassertemperatur ≈ 26 °C) in einer klaren Nacht testen. Erwartung: ≈ 25 bis 35 W je Körper bei 3 bis 5 K Übertemperatur. Wenn der Wert unter 20 W liegt, ist die Himmelssicht das Problem, dann nicht weiterbauen. Zum Messen den Durchfluss mit Eimer und Stoppuhr bestimmen und die Fühler vorher gemeinsam im selben Wasserbad abgleichen (ΔT ≈ 2 K).
3. **Rahmen:** Alu-/Holzprofil, Unterkante ≈ 2,0 m, Neigung 20° (Hochpunkt zur Sammelleitung). Mit ≥ 4 Schwerlastankern sichern.
4. **Strahler:** 3 Körper mit dem Typ-Schild nach oben, die Entlüfter an den Hochpunkten. Rückseiten 30 mm PIR (Alu nach unten). **Hinweis:** Geneigter Betrieb ist herstellerseitig nicht freigegeben. Bei 20° und Entlüftung am Hochpunkt funktioniert es in der Praxis, das Ergebnis ist im Prototyp zu kontrollieren (Fühler). Falls nicht, Alternative: unverglaster Alu-Flachabsorber (Roll-Bond oder Sonnenkollektor-Absorber), weiß lackiert.
5. **Innen:** Raumkühler an Massivwand, Unterkante ≥ 1,2 m, Oberkante ≤ 1,8 m, nicht über dem Bett. Alle Innenkörper liegen mit ihrem Hochpunkt unter dem Strahler-Tiefpunkt.
6. **Rohrleitung:** Mit Pressfittings (Zange leihen), Tichelmann-Verteilung, stetiges Steigen zu den Entlüftern, Vor- und Rücklauf gedämmt.
7. **Durchführung:** Rohre, 12-V-Kabel und Fühlerkabel durch den Fensterspalt (Schaumstoff) oder eine Kernbohrung (Vermieter fragen).
8. **Pumpe und Regler:** Pumpe und Regler wettergeschützt am Balkon. Fühler 1 am Strahler-Auslauf, Fühler 2 am Raumkühler-Rücklauf, Fühler 3 am Vorlauf, alle gedämmt.
9. **Tretlader:** Rollentrainer, Reibrad, Generator, Diode, Sicherung, Wandler, Batterie. Alles Kleinspannung (Leerlauf ≤ 30 V).
10. **Befüllen** mit VE-Wasser (Zusatz nicht nötig, salzarmes Füllwasser nach VDI 2035, optional Molybdat-Inhibitor) und gründlich entlüften. **Druckprobe** mit Wasser bei 2,5 bar für 60 min mit Manometer und trockenem Papier an den Fittings. Betriebsdruck kalt 1,0 bis 1,5 bar.
11. **Test:** Pumpenleistung messen (Ziel ≤ 2,5 W), Durchfluss auf 50 L/h stellen. In der ersten klaren Nacht loggen. Erwartung um 03:00: Vorlauf ≈ 23,6 °C, Rücklauf ≈ 25,4 °C, ΔT ≈ 1,8 K (≈ 105 W). Prüfen, ob der Regler morgens abschaltet, sobald die Sonne den Strahler erwärmt.
12. **Betrieb:** 1× täglich ≈ 40 min bei 90 W treten (bei 4-W-Pumpe 2 × 30 min). Danach duschen. Morgens bei offenem Fenster treten, wenn möglich.
13. **Herbst:** Kreis entleeren (Frostgefahr).

## 9. Sicherheit

- **Absturz und Wind:** Rahmen und Körper (je ≈ 12 kg in 2 m Höhe) mit Schwerlastankern sichern. Bei Sturm kein Aufenthalt darunter.
- **Wandlast innen:** Drei Körper zu je ≈ 42 kg nur an Massivwand mit Schwerlastkonsolen.
- **Stagnation:** Der weiße Strahler erreicht in der Sonne ≈ 45 bis 55 °C. Das ist mit PN 6 bar, MAG und Sicherheitsventil unkritisch. Ablass des Sicherheitsventils zum Boden führen.
- **Elektrik:** Kleinspannung. Sicherung 15 A in der Batterieleitung, passende Leiterquerschnitte. AGM statt Blei-Säure wegen Gasung. Generator und Reibrad abdecken, Verletzungsgefahr durch das laufende Rad.
- **Sport:** 40 min bei 90 W sind mäßig, aber nicht für jeden. Trinken, nach dem Treten duschen. Bei Herz-Kreislauf-Vorerkrankung vorher ärztlich klären. Wer schon nach 20 min erschöpft ist, tritt kürzer und lädt mit einer kleineren Batterie.
- **Korrosion:** Geschlossener Kreis mit sauerstoffdichtem PEX-Al und salzarmem Wasser. Rostschutz an Kanten. Erwartete Lebensdauer der Außenkörper 5 bis 8 Jahre (Außenlackierung mit PU-Lack nachbessern).
- **Schimmel und Feuchte:** Der Regler sperrt den Vorlauf bei < 19 °C. Bei hoher Raumfeuchte (> 65 %) kurz lüften.

## 10. Grenzen und Vergleich

**Grenzen:**
- Der Ertrag hängt an klarem Himmel und guter Himmelssicht. Bei bedecktem Himmel ist er fast null.
- Alle Zahlen sind Handrechnungen mit ≈ ±30 % Unsicherheit, vor allem bei Himmelssichtfaktor, Kollektorwirkungsgrad und Zimmerkopplung G_a. Der Prototyp (Bauschritt 2) klärt das mit einer Nacht Messung.
- Das Ziel ≤ 26 °C wird im Basisfall nicht erreicht (26,3 °C, im Wochenmittel 26,7 °C). Die Ausbaustufe bringt 26,1 °C, nur ein gut gedämmtes Zimmer erreicht es sicher.
- Ohne Muskelkraft steht die Pumpe. Die Batterie überbrückt ≈ 2 Nächte.
- Klimaanlagen-Niveau (−5 K und mehr) ist damit nicht erreichbar. Nachtlüftung ist wirksamer, wo sie möglich ist.
- Ehrlich: Ein 10-W-Solarmodul würde denselben Zweck ohne Zimmerwärme erfüllen. Nach den Vorgaben kommt Solarstrom aber nur in Frage, wenn es mit Muskeln nicht geht.

| | Durchlauf 2 (Zeolith) | Runde 3 (Nachtstrahler) | **Runde 4 (Nachtstrahler, überarbeitet)** |
|---|---|---|---|
| Kälte/Tag | ≈ 1 kWh (nur klare Tage) | ≈ 0,9 kWh (nur klare Nächte) | ≈ 1,05 kWh (nur klare Nächte) |
| Muskel | nein | 20 min/Tag (zu optimistisch) | **≈ 40 min/Tag (Spanne 26 bis 60)** |
| Zimmer | | −1,6 K | **−1,7 K klar, −1,3 K Wochenmittel** |
| Gewicht Balkon | 470 kg | ≈ 100 kg | ≈ 100 kg (+ ≈ 126 kg innen) |
| Kosten | 12 bis 18 k€ | ≈ 1,7 k€ | ≈ 1,6 k€ |
| DIY | nein | ja (heikle Punkte) | **ja, mit Prototyp-Test** |

## 11. Energiebilanz (24-h-Mittel, Auslegungstag, 1 Runde/Tag)

Alle Werte sind 24-h-Mittel. Der Nachtstrahler läuft 10,5 h pro Nacht. Eine Tretrunde von 40 min bei 90 W pro Tag. Luft tags 32 °C, Nachtluft im Betriebsmittel 22,8 °C, Himmel im Mittel 9,9 °C, Umgebung 25,2 °C. Alle „waerme“- und „strahlung“-Ströme zeigen von warm nach kalt.

```json
{
  "knoten": {
    "Nahrung": {"T_C": 25, "rolle": "umgebung"},
    "Mensch": {"T_C": 37, "rolle": "komponente"},
    "Tretgenerator": {"T_C": 40, "rolle": "komponente"},
    "Pumpe_Regler": {"T_C": 30, "rolle": "komponente"},
    "Raumkuehler": {"T_C": 24.4, "rolle": "komponente"},
    "Nachtstrahler": {"T_C": 23.8, "rolle": "komponente"},
    "Wohnung": {"T_C": 26.3, "rolle": "umgebung"},
    "Bad": {"T_C": 15, "rolle": "umgebung"},
    "Himmel": {"T_C": 9.9, "rolle": "umgebung"},
    "Nachtluft": {"T_C": 22.8, "rolle": "umgebung"},
    "Balkonumfeld": {"T_C": 25.2, "rolle": "umgebung"}
  },
  "stroeme": [
    {"von": "Nahrung", "nach": "Mensch", "W": 10.87, "art": "arbeit"},
    {"von": "Mensch", "nach": "Tretgenerator", "W": 2.50, "art": "arbeit"},
    {"von": "Mensch", "nach": "Wohnung", "W": 6.08, "art": "waerme"},
    {"von": "Mensch", "nach": "Bad", "W": 2.29, "art": "waerme"},
    {"von": "Tretgenerator", "nach": "Wohnung", "W": 1.20, "art": "waerme"},
    {"von": "Tretgenerator", "nach": "Pumpe_Regler", "W": 1.30, "art": "arbeit"},
    {"von": "Pumpe_Regler", "nach": "Nachtstrahler", "W": 1.30, "art": "waerme"},
    {"von": "Wohnung", "nach": "Raumkuehler", "W": 43.8, "art": "waerme"},
    {"von": "Raumkuehler", "nach": "Nachtstrahler", "W": 43.8, "art": "waerme"},
    {"von": "Balkonumfeld", "nach": "Nachtstrahler", "W": 3.9, "art": "strahlung"},
    {"von": "Nachtstrahler", "nach": "Himmel", "W": 41.5, "art": "strahlung"},
    {"von": "Nachtstrahler", "nach": "Nachtluft", "W": 7.5, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Wohnung", "T_ein_C": 28.0, "T_aus_C": 26.3, "kuehlleistung_W": 36.5},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```