# Zimmer kühlen mit Muskelkraft: Nachtstrahler-Kreis mit muskelbetriebener Umwälzpumpe

## 1. Kurzfazit

- **Ansatzwechsel:** Muskelkraft ist mit reinem Wasser und Selbstbau kein sinnvoller Kälteerzeuger. Die Kälte kommt aus dem **klaren Nachthimmel** und der kühleren Nachtluft. Die Muskeln liefern nur die **Pumpenenergie** (ca. 17 Wh pro Tag). Das ist die einzige Rolle, in der sie netto Sinn ergibt.
- **Gerät:** Ein geschlossener Wasserkreis verbindet zwei weiße Flachheizkörper auf dem Balkon (Nachtstrahler, 3 m²) mit zwei Heizkörpern an der Zimmerwand (Raumkühler). Die Pumpe (1,5 W, 12 V) läuft nur nachts, geregelt und aus einer Batterie gespeist. Die Batterie wird auf dem Fahrrad geladen. Es gibt keinen Dampf, kein Vakuum, keinen Tank, keine Kondensation und keinen Wasserverlust.
- **Ertrag (Auslegungsnacht):** 86 W über 10,5 h, also ≈ **0,9 kWh pro Nacht** (Spanne 0,55 bis 1,25 kWh je nach Himmel). Das sind im 24-h-Mittel 37,5 W.
- **Muskelbilanz:** Eine Runde (20 min, 75 W, 1× täglich) bringt 46,7 Wh Wärme ins Zimmer, das sind im 24-h-Mittel 1,9 W. Dem stehen 37,5 W Kälte gegenüber. **Netto sind es 35,6 W.**
- **Zimmer:** Im 24-h-Mittel wird es um **≈ 1,6 K kühler** (28,0 → 26,4 °C, Unsicherheit ±0,4 K). Abendspitze −1,35 K, Frühminimum −1,9 K. Das Ziel ≤ 26 °C wird nur bei klaren Nächten oder mit Zusatzmaßnahmen erreicht (siehe 7.4).
- **Praxis:** Betriebsbereit wiegt der Balkonteil ≈ 100 kg. Die Kosten liegen bei ≈ 1,7 k€ (1,5 bis 2,0 k€), und das Gerät ist selbst baubar.

## 2. Was gegenüber Runde 1 korrigiert wurde

| Kritikpunkt | Änderung |
|---|---|
| Prüfer: Nutztemperatur nicht unter Außenluft | Die Bilanz nutzt `luft_T_C = 32`. Die Wärmesenken sind Himmel und Nachtluft als eigene Knoten, Tag und Nacht sind sauber getrennt. Die Wohnung liegt bei 26,4 °C, also unter 32 °C. |
| Himmel 4 °C und „trockene Nacht" unrealistisch | Mit dem Taupunkt 17,4 °C (32 °C, 40 % r. F.) liegt der Himmel bei ≈ 9,5 °C (Berdahl-Martin). Nachts steigt die Luftfeuchte auf ≈ 80 % r. F. Der Strahler bleibt mit ≥ 21 °C über dem Taupunkt, es gibt also keinen Tau und keine Folie. |
| Schwerkraftumlauf rechnerisch nicht tragfähig | Der Umlauf ist jetzt **gepumpt** (Rohr 20×2, 1,5 W). Ein Schwerkrafttest ist nur optionaler Bonus (7.6). |
| Konvektor tief hängend | Der Raumkühler hängt hoch an der Wand (Unterkante ≥ 1,5 m), die Kaltluft fällt in den Raum. Bei gepumptem Kreis ist die Höhe frei wählbar. |
| Pool-Absorber nicht druckfest | Es kommen Stahl-Flachheizkörper (PN 6 bis 10 bar) zum Einsatz. Der Betriebsdruck beträgt ≤ 1,5 bar, die Stagnation ≈ 45 °C. |
| Speicherverluste zu niedrig | Es gibt **keinen Tank**. Gespeichert wird in der Bausubstanz des Zimmers. Die Rohrverluste sind bei ΔT ≈ 1 K vernachlässigbar. |
| Hydraulikleistung „10–20 W" falsch | Korrekt sind 5 bis 10 mW hydraulisch. Elektrisch braucht eine Kleinstpumpe 1 bis 2 W wegen ihres Motorwirkungsgrads (7.5). |
| Kernthema und Mensch/Bad fehlten | Die Wärmesenke wird benannt (langwellige Abstrahlung zum Himmel). Nahrung, Mensch, Bad und Tretlader sind in der Bilanz enthalten. |
| Zimmereffekt ungeprüft | Zwei-Knoten-Modell (Luft + Masse), Details in 7.4. |

## 3. Prinzip

Zwei frühere Erkenntnisse gelten weiter. Ein geschlossener Verdunsten-Kondensieren-Kreis ohne Druckhub kühlt nicht. Offene Verdunstung verliert Wasser. Die Kondensationswärme entfällt hier, weil kein Phasenwechsel stattfindet.

**Die Wärme fließt ohne Druckhub ab**, denn es gibt eine kältere Senke:

1. **Wärmesenke:** Nachts strahlt eine weiße Fläche (Emission ≈ 0,9 im Fenster 8 bis 13 µm) zum Himmel. Der Himmel liegt effektiv bei ≈ 9,5 °C, die Nachtluft bei ≈ 22,5 °C (Mittel 20:30 bis 07:00, von 28 auf 20 °C fallend). Der Strahler kann so auf ≈ 22 bis 23 °C kommen und gibt dabei Wärme ab.
2. **Wärmequelle:** Das Zimmer hat 26 bis 28 °C. Ein Raumkühler mit 23,8 °C Wassertemperatur nimmt Wärme auf.
3. **Wasserkreis:** Er transportiert die Wärme vom Raumkühler zum Nachtstrahler.
4. **Tagsüber:** Die Pumpe steht, der Regler sperrt. Die weiße Fläche heizt sich in der Sonne auf ≈ 45 °C (Absorption ≈ 0,25), liegt aber **über** dem Raumkühler. Diese Wärme wird nicht ins Zimmer gepumpt (Wärmesperre durch Lage und Regelung).
5. **Speicher:** Die Kälte wird in den Zimmerwänden gespeichert (≈ 3 MJ/K wirksame Masse). Der Effekt wirkt nach und baut sich über 2 bis 3 Tage auf.
6. **Muskelkraft:** Sie lädt eine 12-V-Batterie. Die Batterie treibt Pumpe und Regler nachts.

## 4. Ehrliche Bilanz des Tretenden (eine Runde: 20 min, 75 W mechanisch)

| Größe | Wert |
|---|---|
| Stoffwechsel (Wirkungsgrad 23 %) | 326 W, in 20 min 108,7 Wh |
| Körperwärme | 251 W, in 20 min 83,7 Wh |
| Im Körper gespeichert (Ø-Körpertemperatur +0,62 K, 75 kg × 3,47 kJ/kgK = 72 Wh/K) | 45 Wh, geht mit ins Bad |
| **An das Zimmer abgegeben** | **38,7 Wh ≈ 116 W** (fühlbar ≈ 65 W, latent ≈ 51 W entsprechend ≈ 25 g Schweiß) |
| Mechanische Arbeit 25 Wh | Kette Generator, Wandler, Laden (Wirkungsgrad ≈ 0,68): 8 Wh Verlust im Zimmer, 17 Wh elektrisch für die Pumpe (Pumpenabwärme bleibt draußen) |
| **Wärme ins Zimmer je Runde gesamt** | **46,7 Wh** |

Die 25 g Schweiß sind als Luftfeuchte vernachlässigbar (≈ +0,5 g/m³).

**Nötige Leistungszahl** (Wärme ins Zimmer je mechanischer Wh, Generator im Zimmer):

| Runde | mech. | ans Zimmer | COP_min |
|---|---|---|---|
| 20 min, 75 W | 25 Wh | 46,7 Wh | **1,9** |
| 30 min, 100 W | 50 Wh | 96 + 16 = 112 Wh | 2,2 |
| 60 min, 100 W (Körper +1,5 K) | 100 Wh | 227 + 32 = 259 Wh | 2,6 |

Kurze Runden sind günstiger, weil der Körper anfangs viel Wärme speichert. Diese Hürde ist für einen Kältekreis anspruchsvoll. Der Nachtstrahler nimmt sie mühelos: Er liefert 0,9 kWh Kälte für 25 Wh Tretarbeit, also **≈ 36 Wh Kälte je Wh Tretarbeit**.

Das ist keine thermodynamische Leistungszahl. Die Kälte kommt aus dem Himmel, und das Treten hält nur den Umlauf am Laufen. Bei einem Kreis, der auch ohne Pumpe liefe (7.6), wäre der Beitrag des Tretens null.

## 5. Prüfung der Muskel-Optionen

| Option | Ergebnis |
|---|---|
| **Wasserdampf-Verdichter** (Verdampfer 15 °C/17 mbar, Kondensator 35 °C/56 mbar) | Für 0,4 kW Kälte sind ≈ 45 m³/h Saugvolumen nötig. Ideal wäre COP ≈ 13, real 4 bis 5. **Nicht DIY** (vakuumdichte Welle, Klappen für < 5 mbar). Selbst gelungen brächte er je 20-min-Runde nur ≈ +80 Wh netto, ein Zehntel der Nachtkälte. |
| Sorption mit Muskelwärme regenerieren | 33 Wh Reibungswärme ergeben ≈ 29 Wh Kälte, COP < 1. |
| Gewicht heben / Feder spannen | Für Kälte unbrauchbar (1,4 t bzw. 800 kg je Runde). Für die **Pumpe** wären rechnerisch ≈ 0,5 Wh nötig (50 kg × 2 m bei 5 % Wirkungsgrad). Das ist eine Uhrwerks-Bastelei, die Batterie ist einfacher. |
| Generator + Peltier | 17 Wh elektrisch × COP 0,5 bis 0,8 ergeben ≈ 10 Wh Kälte, weit unter COP_min. |
| Lüfter am Raumkühler (1,5 W) | Bringt ≈ +7 W im Mittel, kostet aber eine zweite Runde (≈ 3 W Zimmerwärme). Netto ≈ 0, **nicht empfohlen**. |
| Barometrisches Vakuum / Strahlpumpe | Unmöglich (10 m Wassersäule bzw. Dampfdruck des Treibwassers). |
| **Pumpe per Batterie** | Ausreichend, DIY und netto deutlich positiv. Das ist die gewählte Lösung. |

## 6. Aufbau

```
 BALKON (außen)
   Himmel (klar, Ø ≈ 9,5 °C)      ↑ ↑ ↑  Abstrahlung nachts
 ┌────────────────────────────────────────────────┐  ≈ 2,2 m Höhe
 │ Nachtstrahler: 2 × Flachheizkörper Typ 10,       │  5–10° geneigt, Entlüfter an
 │ H500 × L3000, weiß, Rückseite 30 mm PIR gedämmt  │  der höchsten Stelle (Pergola)
 └───────┬──────────────────────────────┬───────────┘
   Vorlauf (kalt)                  Rücklauf (warm)
         │                              ▲
   ┌─────┴─────┐  Pumpe 1,5 W (12 V)     │  PEX-Al 20×2, 20 mm gedämmt
   │   Pumpe   │◄─ Regler + 2 Fühler     │  MAG 8 L, SV 3 bar, Manometer
   └─────┬─────┘                         │
═════════╪═══════ Fenster-/Balkontür-Durchführung ═════╪═════════
 ZIMMER  ▼                               │
 ┌───────────────────────────────────────┴───────────┐
 │ Raumkühler: 2 × Typ 22, 600 × 1800, hoch an der    │  Unterkante ≥ 1,5 m,
 │ Massivwand, weiß; Kaltluft fällt in den Raum       │  Kühlbetrieb ohne Kondensat
 └───────────────────────────────────────────────────┘
 Muskelseite: Fahrrad/Rollentrainer → Reibrad → 24-V-Gleichstrommotor als Generator
              → Diode/Sicherung → DC/DC-Wandler → 12-V-AGM-Batterie 7 Ah → Pumpe/Regler
```

**Regelung** (Differenzregler mit zwei Fühlern):
- Die Pumpe läuft nur, wenn T_Strahler-Auslauf < T_Raumkühler-Rücklauf − 1,0 K und T_Strahler < 26 °C gilt (Hysterese 0,5 K).
- Sperre bei Kühler-Vorlauf < 18 °C als Kondensschutz.
- Tagsüber steht die Pumpe, und die heiße Strahlerfläche bleibt vom Zimmer getrennt.

## 7. Rechnung

### 7.1 Kühlleistung des Nachtstrahlers je m²

**Annahmen (Nachtmittel 20:30 bis 07:00):**
- Himmelssicht-Faktor 0,5 (Brüstung, Balkon darüber, Fassade)
- Restumgebung 25 °C (Fassade speichert noch Wärme)
- ε = 0,9
- Luft 22,5 °C
- Himmel 9,5 °C
- Konvektion h = 6 W/m²K (Wind 0 bis 3 m/s)

Positive Werte bedeuten Wärmeabfuhr. Konvektion an die Luft zählt als Abfuhr, wenn die Fläche wärmer als die Luft ist.

| T_Fläche | Himmel | Umgebung | Luft | **netto W/m²** |
|---|---|---|---|---|
| 25 °C | +38,8 | 0 | +15 | 54 |
| 24 °C | +36,1 | −2,7 | +9 | 42 |
| 23 °C | +33,4 | −5,4 | +3 | 31 |
| **22,8 °C** | +32,9 | −5,9 | +1,8 | **28,8** |
| 22 °C | +30,8 | −8,0 | −3 | 20 |
| 21 °C | +28,2 | −10,6 | −9 | 9 |
| 20 °C | +25,6 | −13,2 | −15 | −3 |

Der Strahler kann also nicht wirklich unter ≈ 20 bis 21 °C kühlen. Er wirkt als Trockenkühler gegen die Nachtluft, unterstützt durch die Abstrahlung. Das ist der ehrliche Nutzen bei 17 °C Taupunkt.

### 7.2 Gleichgewicht Raumkühler ↔ Strahler

Nachts hat das Zimmer im Mittel ≈ 25,7 °C. Der Raumkühler hat eine Leitfähigkeit von 45 W/K (2 × Typ 22, Bandbreite 35 bis 55). Der Strahler liegt 1 K unter der Wassertemperatur.

Das Gleichgewicht folgt aus 45·(25,7 − T_w) = 3 m² · [31 + 11·(T_w − 1 − 23)]:

- T_w = 23,8 °C
- T_Strahler = 22,8 °C
- **Q = 86 W**, das entspricht 0,9 kWh in 10,5 h

**Empfindlichkeit:** Ein Raumkühler mit 35 W/K liefert 77 W, mit 55 W/K liefert er 94 W. Der Ertrag hängt also kaum am Kühler, sondern an Himmelssicht und Wetter.

### 7.3 Wetterabhängigkeit

| Nacht | Ertrag | 24-h-Mittel | Zimmer nach 3 Tagen (vs. ohne) |
|---|---|---|---|
| klar, trocken (Taupunkt 12 °C) | ≈ 1,2 kWh | 50 W | ≈ −2,3 K |
| **klar, Auslegungsfall** | **0,9 kWh** | **37,5 W** | **−1,6 K** |
| halb bewölkt | ≈ 0,55 kWh | 23 W | ≈ −1,0 K |
| bedeckt | ≈ 0,15 kWh | 6 W | ≈ −0,3 K |

Schlechte Himmelssicht (Faktor 0,35 statt 0,5) senkt den Ertrag auf ≈ 55 W bzw. 0,6 kWh. Die Himmelssicht ist der wichtigste Standortfaktor.

### 7.4 Zimmereffekt (Zwei-Knoten-Modell)

**Zimmer:** 20 m² Schlafzimmer, mittleres Geschoss, Westfenster 3 m² mit Außenrollo, Fenster tagsüber zu.

**Wärmelast:**
- Sonne durch das Fenster (g_ges ≈ 0,12, Spitze ≈ 220 W gegen 17 Uhr): Mittel 37 W
- Innen (Geräte, Schlafender): 33 W
- Summe ≈ 70 W

**Modellparameter:**
- C_Luft + leichte Möbel: 0,5 MJ/K
- C_Masse (60 m² × 5 cm): 3,0 MJ/K
- Kopplung Luft ↔ Masse: G_LM = 250 W/K
- Kopplung an die Umgebung: G_a = 22 W/K (Transmission 12, Lüftung 5, Nachbarräume 5)
- Wirksame Außentemperatur: 24,8 °C (Mittel aus Außenluft ≈ 26 °C und kühleren Nachbarräumen)

Ohne Gerät ergibt das T₀ = 24,8 + 70/22 ≈ **28,0 °C** im 24-h-Mittel. Die Tagesschwankung beträgt ±0,8 K (27,2 bis 28,8 °C).

**Effekt des Geräts (Linearisierung):**
- Netto-Kälte: P = 37,5 − 1,9 = 35,6 W
- ΔT_Mittel = −35,6 / 22 ≈ **−1,6 K**, also 28,0 → **26,4 °C**
- Zeitkonstante τ ≈ (C_L + C_M)/(G_a + G_Gerät) ≈ 33 h. Der Effekt baut sich über mehrere Tage auf: Tag 1: −0,9 K, Tag 2: −1,3 K, Tag 3: −1,45 K, danach −1,6 K.
- Tagesgang des Geräteeffekts: ±0,26 K (Nachtleistung 86 W gegen Tagesnull, verteilt auf 3,5 MJ/K). Das ergibt ein Minimum um 07:00 von −1,9 K und eine Abendspitze um 20:30 von −1,35 K.
- Luft gegen Masse: die Lufttemperatur liegt tagsüber ≈ 0,3 K über der Masse (70 W / 250 W/K).

| Zeitpunkt | ohne Gerät | mit Gerät (Tag 3) |
|---|---|---|
| Frühminimum ≈ 07:00 | 27,2 °C | ≈ 25,3 °C |
| Abendspitze ≈ 20:30 | 28,8 °C | ≈ 27,4 °C |
| 24-h-Mittel | 28,0 °C | **26,4 °C** |

Der Zielwert ≤ 26 °C wird im Mittel **nicht sicher** erreicht (26,0 bis 26,8 °C). Diese Hebel bringen weitere Kelvin:
- Außenrollo konsequent nutzen: ≈ −0,5 K
- Nachts das Fenster öffnen, wo das möglich ist (Nachtlüftung ist stärker als jedes Wassergerät): −1 K und mehr
- 3. Innenkühler + zusätzliche Strahlerfläche (Brüstung, Ertrag je m² ≈ 60 %): Q ≈ 128 W (+50 %), zusätzlich ≈ −0,8 K

### 7.5 Muskelkraft und Hydraulik

- **Hydraulikleistung:** ṁ = 13,7 g/s bei ≈ 300 Pa ergibt ≈ 4 mW. Bei 500 Pa und 20 g/s sind es ≈ 10 mW.
- **Elektrisch** braucht eine Mini-Bürstenlospumpe 1 bis 2 W (Motorwirkungsgrad ≈ 0,3 %). Ich setze 1,5 W an. Mit PWM auf ≈ 40 % Drehzahl sind ≈ 0,6 W möglich.
- **Energie pro Nacht:**
  - Pumpe 1,5 W × 10 h = 15 Wh
  - Regler 0,1 W × 24 h = 2,4 Wh
  - Summe ≈ 17 Wh elektrisch
  - benötigt ≈ 25 Wh mechanisch (Kette η ≈ 0,68), das sind 20 min bei 75 W
- **Batterie:** 12 V 7 Ah (84 Wh) deckt ≈ 2 Tage Reserve. Alternativ: alle 2 Tage 30 bis 40 min.
- **Gegenüber Solar:** Ein 10-W-Modul würde es billiger und ohne Zimmerwärme leisten. Nach den Vorgaben kommt Solarstrom aber nur in Frage, wenn es mit Muskeln nicht geht. Es geht, also gibt es keins.

### 7.6 Schwerkraftumlauf (Bonus-Test)

- **Rohr 20×2 (Innendurchmesser 16 mm):** Bei ≈ 13,7 g/s (86 W, 1,5 K Spreizung) ist die Strömung laminar mit v ≈ 0,068 m/s. Das ergibt ≈ 8,5 Pa/m, über ≈ 12 m Rohr ≈ 100 Pa. Der Auftrieb beträgt 2,03 Pa/K · 2 m · 1,5 K ≈ 6 Pa. **Schwerkraft ist damit unmöglich.**
- **Rohr 40×4 (Innendurchmesser 32 mm):** Es sind ≈ 5 Pa Reibung gegen 6 Pa Auftrieb, also nur knapp. Es erfordert zudem eine Kernbohrung. Deshalb ist es nicht die Basis.
- **Test:** Wer das ausprobiert (Pumpe eine klare Nacht aus, Q per Fühler messen) und ≥ 50 W erreicht, braucht das Fahrrad nicht mehr.

## 8. Gewicht und Balkonlast

| Position | kg |
|---|---|
| 2 × Typ 10, H500 × L3000 (je ≈ 23 kg) | 46 |
| Wasser (≈ 9 L) | 9 |
| Rahmen/Pergola (Alu/Holz) | 25 |
| Rohre, Dämmung, Pumpe, MAG, Kleinteile | 20 |
| **Summe Balkon betriebsbereit** | **≈ 100** |

Das sind ≈ 1 kN auf 3 m², also ≈ 0,33 kN/m² gegenüber ≈ 4 kN/m² Auslegungslast (Wohnungsbalkon, DIN EN 1991-1-1, Kategorie Z). Der Rahmen steht auf vier Punkten mit je ≈ 0,25 kN und Lastverteilern. Bei Altbau oder Zweifel vorher Vermieter und Statik klären.

**Windsog** (Böe 25 m/s, c_p ≈ 1,2): ≈ 1,6 kN Abhebekraft auf 3 m². Der Rahmen braucht mindestens 4 Schwerlastanker, jeder ≥ 1 kN Zug, mit Sicherheit 1,5.

**Zimmer:** Die zwei Raumkühler wiegen ≈ 100 kg (je ≈ 50 kg inkl. Wasser) und hängen an Massivwand (Voll-/Hochlochziegel, Beton) mit Schwerlastkonsolen (≥ 4 pro Heizkörper). Trockenbauwände sind ungeeignet.

## 9. Stückliste (ungefähre Preise)

| Teil | € |
|---|---|
| 2 × Flachheizkörper Typ 10, H500 × L3000, weiß, PN 6 bis 10 bar (Nachtstrahler) | 380 |
| Rahmen/Pergola, Winkel, Schwerlastanker | 150 |
| Rückseitendämmung PIR alukaschiert 30 mm, ≈ 4 m² | 50 |
| Entlüfter (2 Hochpunkte), 4 Kugelhähne, Füll-/Entleerhahn | 60 |
| 2 × Flachheizkörper Typ 22, H600 × L1800, weiß (Raumkühler) | 340 |
| Schwerlastkonsolen + Dübel | 50 |
| PEX-Al-PEX 20×2, ≈ 25 m | 75 |
| Pressfittings, T-Stücke, Übergänge | 90 |
| Rohrdämmung 20 mm, ≈ 20 m | 40 |
| MAG 8 L, Sicherheitsventil 3 bar, Manometer | 43 |
| VE-Wasser ≈ 30 L | 15 |
| Mini-Bürstenlospumpe 12 V (1 bis 4 W) | 35 |
| Differenzregler 12 V (≤ 0,15 W) + 2 Fühler | 40 |
| 12-V-AGM-Batterie 7 Ah, Sicherung, Kabel, Voltmeter | 60 |
| 24-V-Gleichstrommotor 250 W (Generator), Reibrad + Halter, DC/DC-Wandler 24 → 14 V/10 A, Diode/Sicherung | 130 |
| Thermometer/Logger (4 Fühler) | 40 |
| Kleinteile, Werkzeugmiete (Pressfittingzange) | 80 |
| **Summe (Fahrrad vorhanden)** | **≈ 1.680** |
| Falls Rollentrainer nötig | + 150 |

Ohne Tretlader (Schwerkrafttest oder Fremdlader) sind es ≈ 1.500 €.

## 10. Bauanleitung

1. **Standort und Freigabe:** Himmelssicht prüfen (mindestens ⅔ des Himmels frei von der Strahlerposition, ein Balkon direkt darüber halbiert den Ertrag). Tragfähigkeit und Vermieter klären.
2. **Rahmen/Pergola** aus Alu- oder Holzprofil bauen, in ≈ 2,2 m Höhe. Mit ≥ 4 Schwerlastankern (je ≥ 1 kN Zug) an Wand und Boden sichern. Die Heizkörper mit 5 bis 10° Neigung montieren, die Entlüfter an der höchsten Stelle.
3. **Heizkörper** liegend montieren. **Hinweis:** Liegender Betrieb ist herstellerseitig nicht freigegeben, die Entlüftung ist der kritische Punkt. Als Alternative dient ein unverglaster Alu-Flachkollektor, weiß lackiert. Die Rückseiten mit 30 mm PIR (Alu-Seite nach unten) dämmen.
4. **Innen:** Raumkühler an der Massivwand mit Unterkante ≥ 1,5 m montieren. Nicht über dem Bett hängen.
5. **Rohrleitung** mit Pressfittings (Zange leihen). Die Rohre steigen stetig zu den Entlüftern. Vor- und Rücklauf getrennt und gedämmt führen.
6. **Durchführung:** Beide Rohre, das 12-V-Kabel und die Fühlerkabel gehen durch den Fensterspalt (Schaumstoff-Kompression) oder eine Kernbohrung (Vermieter fragen).
7. **Pumpe, Regler, Fühler:** Pumpe auf dem Balkon wettergeschützt. Fühler 1 am Strahler-Auslauf, Fühler 2 am Raumkühler-Rücklauf, beide gedämmt.
8. **Tretlader:** Rollentrainer, Reibrad, Generator, Diode, Sicherung, Wandler, Batterie. Alles bleibt Kleinspannung.
9. **Befüllen** mit VE-Wasser ohne Zusätze und entlüften. **Druckprobe** mit Wasser bei 2,5 bar für 60 min, Manometer beobachten und Fittings mit trockenem Papier kontrollieren. Betriebsdruck kalt 1,0 bis 1,5 bar.
10. **Test:** Pumpe von Hand einschalten und den Durchfluss per Eimer/Stoppuhr messen (≈ 50 l/h). In der ersten klaren Nacht die Fühlerwerte loggen. Erwartung um 03:00: Strahler-Auslauf ≈ 22,3 °C, Kühler-Rücklauf ≈ 23,8 °C, ΔT ≈ 1,5 K entspricht Q ≈ 86 W. Ebenfalls prüfen: Schaltet der Regler morgens ab, sobald die Sonne den Strahler erwärmt?
11. **Betrieb:** 1× täglich 20 min mit 75 W treten. Bei vollem Akku (≥ 12,4 V) reicht alle 2 Tage 30 bis 40 min.

## 11. Sicherheit

- **Absturz und Wind:** Rahmen und Heizkörper (je ≈ 23 kg, in 2,2 m Höhe) fest verankern. Kein Aufenthalt bei Sturm unter der Pergola.
- **Wandlast innen:** Zwei Heizkörper mit je ≈ 50 kg nur an Massivwand mit Schwerlastkonsolen hängen.
- **Stagnation:** Der weiße Strahler erreicht in der Sonne ≈ 45 °C. Das ist mit PN 6 bar, MAG und Sicherheitsventil unkritisch. Ablass des Sicherheitsventils zum Boden führen.
- **Elektrik:** Alles ist Kleinspannung (Generator ≤ 30 V im Leerlauf). Sicherung 15 A in der Batterieleitung, Kabelquerschnitt passend, AGM statt Blei-Säure wegen Gasung im Zimmer.
- **Sport:** 20 min bei 75 W sind mäßig. Trinken, nach dem Treten duschen. Bei Herz-Kreislauf-Vorerkrankung vorher ärztlich klären.
- **Korrosion und Wasserqualität:** Geschlossener Kreis mit sauerstoffdichtem PEX-Al und VE-Wasser. Rostschutzlack an Heizkörperkanten außen. Erwartete Lebensdauer der Außenheizkörper 5 bis 8 Jahre.
- **Frost:** Im Herbst entleeren.
- **Schimmel:** Kein Kondenswasser bei 21 °C oder mehr Wasser (Raumtaupunkt ≈ 15 °C). Der Regler sperrt bei Vorlauf < 18 °C.

## 12. Grenzen und Vergleich

**Grenzen:**
- Der Ertrag hängt an klarem Himmel, freier Himmelssicht und der Nachtluft. Bei bedecktem Himmel ist er fast null (7.3).
- Die Zahlen sind Handrechnungen mit ±30 % Unsicherheit, vor allem beim Himmelssicht-Faktor.
- Das Ziel ≤ 26 °C wird nur teilweise erreicht (26,4 °C, Bandbreite 26,0 bis 26,8 °C).
- Ohne Muskelkraft steht die Pumpe. Ein Schwerkrafttest (7.6) oder eine kleine Notreserve (Batterie) sichert den Betrieb.
- Klimaanlagen-Niveau (−5 K und mehr) ist damit nicht erreichbar. Wo nachts gelüftet werden darf, ist das Fenster deutlich wirksamer.

| | Durchlauf 2 (Zeolith) | **Nachtstrahler mit Muskelpumpe** |
|---|---|---|
| Kälte/Tag | ≈ 1 kWh (nur klare Tage) | ≈ 0,9 kWh (nur klare Nächte) |
| Gewicht Balkon | 470 kg | ≈ 100 kg (+ ≈ 100 kg an der Wand innen) |
| Kosten | 12 bis 18 k€ | ≈ 1,7 k€ |
| Vakuum / Sonderteile | ja, Helium-Lecktest | nein |
| DIY | nein | ja |
| Antrieb | Sonne | Nachthimmel + 25 Wh/Tag Muskelkraft |
| Muskel nötig | nein | 20 min/Tag (nur für die Pumpe) |

## 13. Energiebilanz (24-h-Mittel, Auslegungstag, 1 Runde/Tag)

Alle Werte sind 24-h-Mittel. Der Nachtstrahler läuft 10,5 h pro Nacht (Faktor 0,4375). Eine Tretrunde à 20 min bei 75 W pro Tag. Tagluft 32 °C, Nachtluft im Betriebsmittel 22,5 °C.

```json
{
  "knoten": {
    "Nahrung": {"T_C": 25, "rolle": "umgebung"},
    "Mensch": {"T_C": 37, "rolle": "komponente"},
    "Tretgenerator": {"T_C": 40, "rolle": "komponente"},
    "Pumpe_Regler": {"T_C": 30, "rolle": "komponente"},
    "Raumkuehler": {"T_C": 23.8, "rolle": "komponente"},
    "Nachtstrahler": {"T_C": 22.8, "rolle": "komponente"},
    "Wohnung": {"T_C": 26.4, "rolle": "umgebung"},
    "Bad": {"T_C": 15, "rolle": "umgebung"},
    "Himmel": {"T_C": 9.5, "rolle": "umgebung"},
    "Nachtluft": {"T_C": 22.5, "rolle": "umgebung"},
    "Balkonumfeld": {"T_C": 25, "rolle": "umgebung"}
  },
  "stroeme": [
    {"von": "Nahrung", "nach": "Mensch", "W": 4.53, "art": "arbeit"},
    {"von": "Mensch", "nach": "Tretgenerator", "W": 1.03, "art": "arbeit"},
    {"von": "Mensch", "nach": "Wohnung", "W": 1.61, "art": "waerme"},
    {"von": "Mensch", "nach": "Bad", "W": 1.89, "art": "waerme"},
    {"von": "Tretgenerator", "nach": "Wohnung", "W": 0.33, "art": "waerme"},
    {"von": "Tretgenerator", "nach": "Pumpe_Regler", "W": 0.70, "art": "arbeit"},
    {"von": "Pumpe_Regler", "nach": "Nachtstrahler", "W": 0.70, "art": "waerme"},
    {"von": "Wohnung", "nach": "Raumkuehler", "W": 37.5, "art": "waerme"},
    {"von": "Raumkuehler", "nach": "Nachtstrahler", "W": 37.5, "art": "waerme"},
    {"von": "Balkonumfeld", "nach": "Nachtstrahler", "W": 7.7, "art": "strahlung"},
    {"von": "Nachtstrahler", "nach": "Himmel", "W": 43.5, "art": "strahlung"},
    {"von": "Nachtstrahler", "nach": "Nachtluft", "W": 2.4, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Wohnung", "T_ein_C": 28.0, "T_aus_C": 26.4, "kuehlleistung_W": 35.6},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```