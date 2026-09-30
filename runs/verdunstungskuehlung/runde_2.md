# Wasserleitung kühlen: Verdunstungskreislauf mit Verdichter, Solarstrom und Luftkühlung

## 1. Kurzantwort

**Ein geschlossener Verdunstungskreislauf mit nur einem Druck ist ein Wärmerohr.** Es transportiert Wärme, erzeugt aber keine Kälte. Verdampfer und Kondensator haben dieselbe Temperatur, und die Kondensationswärme gibt genau das wieder ab, was die Verdunstung aufgenommen hat. Der Kondensator müsste kälter sein als das zu kühlende Wasser, und so etwas gibt es draußen bei 32 °C nicht.

**Lösung:** Der Kreislauf braucht zwei Druckniveaus. Ein Verdichter hebt den Dampf auf einen Druck, bei dem er schon bei 45 °C kondensiert, also wärmer als die Luft mit 32 °C. Ein Drosselventil ersetzt den "Regen" und senkt den Druck des Kondensats wieder ab. Das ist eine Kältemaschine, und sie ist die bessere Wahl gegenüber Sorption oder Strahlung (Abschnitt 3).

**Wo bleibt die Kondensationswärme?** Im Kondensator bei 45 °C, und von dort fließt sie ganz normal von warm nach kalt an die 32 °C warme Luft: **891 W**. Das sind die 697 W aus dem Wasser plus 194 W Verdichterarbeit. Bezahlt wird mit etwa **224 W Strom**, den ein Standard-PV-Modul (etwa 1,7 m²) mittags direkt liefert. Der Wasserverlust beträgt 0.

**Ergebnis für den Auslegungsfall:** 50 l/h von 24 °C auf **12 °C**, das sind 20 K unter Lufttemperatur. Die Kühlleistung beträgt 697 W bei einer Systemleistungszahl von etwa 3,1.

## 2. Warum der einfache Loop nichts bringt (Zahlen)

| Größe (32 °C, 40 % r.F.) | Wert |
|---|---|
| Kühlgrenztemperatur ("nasser Lappen", offen) | 22,1 °C |
| Taupunkt | 17,2 °C |
| Sättigungsdruck Wasser bei 5 / 45 °C | 0,87 / 9,6 kPa |

- **Offen (nasser Lappen):** Die Verdampfungswärme verlässt das System mit dem Dampf. Die Grenze ist die Kühlgrenze von 22 °C, das Leitungswasser hat schon 24 °C. Es sind also höchstens 1 bis 2 K möglich, und es gehen etwa 1 l/h Wasser verloren (697 W ÷ 2450 kJ/kg). Das ist keine Lösung.
- **Geschlossen mit einem Druck:** Netto null Kühlung, siehe oben.
- **Untere Schranke (2. Hauptsatz):** Um 697 W bei 5 °C aufzunehmen und bei 32 °C abzugeben, braucht man mindestens W = Q·(T_warm − T_kalt)/T_kalt = 697 · 27/278 ≈ **68 W** Arbeit. Ohne Antrieb geht es nicht, und unter 68 W ist es auch mit idealer Technik nicht möglich. Real sind es 3- bis 4-mal so viel, weil der Kondensator wärmer als die Luft sein muss.

## 3. Welche Antriebe kommen infrage?

| Weg | Prinzip | Aufwand für 697 W Kälte | Urteil |
|---|---|---|---|
| **B: Verdichter, Kältemittel R290** | Elektrischer Antrieb, Direktverdampfung an der Wasserleitung | **≈ 224 W Strom**, 1,7 m² PV | **gewählt** |
| Wasserdampf als Kältemittel + Verdichter | Wasser bleibt Kältemittel | Bei 5 °C sind es etwa 150 m³/h Dampf bei Druckverhältnis 11. Das braucht einen mehrstufigen Radialverdichter mit sehr hoher Drehzahl. | Für 0,7 kW nach meiner Kenntnis nicht kaufbar |
| C: Solare Sorption (Silikagel) | Sonnenwärme treibt den Dampf | Bei 32 °C luftgekühlt liegt p/p_s im Adsorber bei 0,145 und im Desorber (85 °C) bei 0,128. Der Hub ist praktisch null. Erst ab etwa 110 °C Antrieb entsteht ein Hub von etwa 0,05 kg/kg. Der COP ist real ≈ 0,2, also ≈ 3,5 kW Wärme, ≈ 11 m² Vakuumröhren, dazu Gel-Betten, Vakuumtechnik und ≈ 150 W Strom für Lüfter und Pumpen. | Größer, teurer und nicht stromfrei, nachts tot. Verworfen. |
| D: Nachthimmelsstrahlung | Kondensator strahlt zum Himmel | Netto etwa 70 W/m² bei Lufttemperatur, bei 5 K darunter nur etwa 25 W/m². 697 W bräuchten 25 bis 35 m² und erreichen nachts nur etwa 16 bis 18 °C. Tagsüber geht praktisch nichts. | Nur als Ergänzung |
| E: Erdreich | Kältere Senke (etwa 10 bis 14 °C) | Kann Wasser nur auf etwa 15 °C bringen, weil das Erdreich wärmer als ein 5-°C-Verdampfer ist. | Nur als Vorkühlung (Abschnitt 7) |

Der Verdichter trifft den Kern der Aufgabe am besten. Er verbindet die Idee "Verdunsten unten, Kondensieren oben" mit dem, was physikalisch fehlt, nämlich einer Druckerhöhung.

## 4. Aufbau

```
      Luft 32 °C ──►  Lüfter 130 l/s (im Schatten!)  ──► Luft 38 °C
   ┌──────────────────────────────────────────────┐
   │  KONDENSATOR-TURM  (Lamellen ~2,3 m²)  45 °C │
   └───────┬──────────────────────────▲───────────┘
   flüssig ~42 °C, 15 bar             │ Heißgas ~63 °C, 15 bar
           │                    ┌─────┴──────┐
     Filtertrockner             │ VERDICHTER │◄── 194 W Strom
           │                    │ (hermetisch│   aus PV 1,7 m²
   Expansionsventil/Kapillare   │  ~1 m³/h)  │   (+ Regelung)
   (ersetzt den "Regen")        └─────▲──────┘
           │ 5,5 bar                  │ Sauggas 5 °C, 5,5 bar
   ┌───────▼──────────────────────────┴───────────┐
   │  VERDAMPFER-TURM  5 °C                       │
   │  Kältemittel verdunstet an der Wand der      │◄── Wasser 24 °C
   │  Wasserleitung (Plattentauscher, Gegenstrom, │    50 l/h
   │  doppelwandig, ≥0,15 m²)                     │──► Wasser 12 °C
   └──────────────────────────────────────────────┘
   Kältemittel: ~100 g R290, im Kreis, kein Verlust
```

Zur Zuordnung zu deiner Turm-Idee: Der linke Turm ist der Verdampfer an der Leitung, der rechte der Kondensator. Zwischen den Türmen gibt es zwei neue Bauteile. Der Verdichter macht aus "Dampf steigt auf" einen Druckhub, und das Drosselventil ersetzt den frei fallenden Regen. Die Schwerkraft spielt keine Rolle mehr, denn der Druckunterschied von etwa 10 bar treibt das Kältemittel.

## 5. Rechnung (Auslegungsfall Tag)

**Kühllast:** 50 l/h = 0,01389 kg/s. Q = 0,01389 · 4186 · (24 − 12) = **697 W**.

**Kreisprozess R290** (Näherungswerte aus Stoffdaten, etwa ±5 %):
- Verdampfen bei 5 °C (5,5 bar), Kondensieren bei 45 °C (15,3 bar), Druckverhältnis 2,8.
- Nettokälteeffekt (Sattdampf 5 °C minus Flüssigkeit bei 42 °C): 269 kJ/kg.
- Massenstrom: 697 / 269 = **2,6 g/s ≈ 9,3 kg/h**.
- Saugvolumenstrom ≈ 0,22 l/s ≈ 0,8 m³/h, das entspricht einem Hubvolumen von etwa 1 m³/h (rund 5,5 cm³ bei 3000 U/min). Das gibt es als Serienverdichter.
- Isentrope Verdichtung: 48 kJ/kg, entsprechend 124 W. Mit Gesamtwirkungsgrad 0,64 sind es **194 W** elektrisch. Das ergibt COP_Verdichter = 3,6, also etwa 52 % des Carnot-Werts (6,95). Für einen kleinen Kolben- oder Rollkolbenverdichter ist das üblich.

**Verdampfer** (Plattenwärmetauscher, Wasser/R290, Gegenstrom):
- ΔT_log = (19 − 7)/ln(19/7) = 12,0 K, damit UA = 697/12,0 = 58 W/K.
- Bei 50 l/h liegt die Strömung in den Plattenkanälen im laminaren Bereich. Das Wellenprofil erzwingt trotzdem Nu ≈ 6 bis 10, also h ≈ 1000 W/m²K. Ich rechne konservativ mit U = 500 W/m²K, das ergibt 0,12 m². Ich plane **0,15 bis 0,2 m²** ein.
- Für Trinkwasser braucht es einen **doppelwandigen** Tauscher mit Leckageanzeige oder einen kleinen Zwischenkreis. Der Zwischenkreis kostet etwa 2 K Verdampfungstemperatur und etwa 8 % COP.

**Kondensator:**
- Q = 697 + 194 = **891 W**. Bei 6 K Luftaufwärmung (32 → 38 °C) sind das 0,128 m³/s, also etwa 460 m³/h.
- ΔT_log = (13 − 7)/ln(13/7) = 9,7 K, UA = 92 W/K. Mit U ≈ 40 W/m²K bezogen auf die Lamellenfläche ergeben sich **≈ 2,3 m²**.
- Der Kondensator muss im **Schatten** stehen. Nur 6 K Kondensatorreserve gegenüber der Luft sind knapp, und ein von der Sonne aufgeheizter Kondensator verliert schnell 15 % COP.

**Strom (ehrlich):**

| Verbraucher | W |
|---|---|
| Verdichter | 194 |
| Lüfter (0,128 m³/s, Δp ≈ 80 Pa ≈ 10 W Luftleistung, Wirkungsgrad 40 %) | 25 |
| Regelung, Magnetventil, Frostwächter | 5 |
| **Summe** | **224** |

Die Leistungszahl beträgt 697/224 = 3,1. Eine Pumpe ist nicht nötig, weil der Leitungsdruck das Wasser treibt.

**PV:** Ein Standardmodul mit etwa 320 Wp (1,7 m²) liefert bei 800 W/m² und 60 °C Zelltemperatur etwa 320 · 0,8 · 0,88 ≈ **224 W**. Der Verdichter läuft mit Drehzahlregelung (Inverter) direkt am MPPT.

## 6. Wo die Energie bleibt (Tagesbetrieb)

| Zufuhr | W |
|---|---|
| Sonne, netto auf PV | 1280 |
| Wärme aus dem Leitungswasser | 697 |
| **Summe** | **1977** |

| Abfuhr an die Luft | W |
|---|---|
| Kondensator (697 W Wasserwärme + 194 W Arbeit) | 891 |
| PV-Abwärme (1280 − 224) | 1056 |
| Lüfter, Regelung | 30 |
| **Summe** | **1977** |

Die Kondensationswärme landet also in der Luft. Möglich ist das nur, weil der Verdichter das Kältemittel auf 45 °C bringt, also über die Lufttemperatur. Das Wasser selbst gibt seine Wärme bei 5 °C ab, und der Verdichter pumpt sie 40 K bergauf.

## 7. Varianten und Ausbaustufen

**Auslauftemperatur** (gleiche Geometrie, Elektrik grob):

| Auslauf | Kälte | Verdampfung | Strom gesamt |
|---|---|---|---|
| 16 °C | 465 W | ≈ 11 °C | ≈ 135 W |
| **12 °C** | **697 W** | **5 °C** | **≈ 224 W** |
| 8 °C | 930 W | ≈ 1,5 °C | ≈ 310 W |

Unter 8 °C Auslauf würde ich nicht gehen, weil die Wand nahe 0 °C kommt. **Frostwächter und Durchflusswächter sind Pflicht**, denn bei Stillstand des Wassers friert der Tauscher und platzt.

**Erd-Vorkühlung (optional, Größenordnung ±50 %):**
- Eine erdverlegte PE-Leitung kühlt 24 → 15 °C und liefert etwa 520 W passiv. Dafür braucht man etwa 60 bis 80 m Rohr in 1,5 bis 2 m Tiefe oder eine Erdsonde von 15 bis 20 m.
- Der Kältekreis muss dann nur noch 15 → 8 °C leisten (≈ 410 W) und braucht dafür ≈ 135 W. Das ist ein Auslauf von 8 °C statt 12 °C bei weniger als zwei Dritteln des Stroms.
- Das Erdreich (10 bis 14 °C) ist wärmer als der 5-°C-Verdampfer, kann also nicht als Kondensatorsenke oder als Ersatz für den Verdampfer dienen.

**24-h-Betrieb:**
- Nachts (Luft 20 °C) kondensiert die Anlage bei etwa 32 °C. Dann sind es etwa 150 W.
- Der Tagesbedarf liegt bei etwa 4,5 kWh (12 h × 224 W + 12 h × 150 W).
- Ein Modul liefert an einem klaren Sommertag nur etwa 1,4 kWh. Für Dauerbetrieb braucht man also etwa 3 Module und etwa 3 kWh Batterie oder Netzstrom (etwa 1,35 €/Tag bei 0,30 €/kWh).
- Alternativ läuft die Anlage nur mittags direkt aus der PV und füllt einen isolierten Kaltwasserspeicher (z. B. 200 l bei 10 °C).

## 8. Grenzen und Praxis

- **Strom ist nötig, es geht nicht ohne.** Der Mindestwert liegt bei 68 W, realistisch sind 224 W. Ohne Strom oder Wärme mit hoher Temperatur gibt es keine Kühlung unter Umgebung. Das folgt aus dem 2. Hauptsatz.
- **Nur mittags voll solar.** Bei Wolken (400 W/m²) liefert das Modul nur etwa die Hälfte, und der Verdichter fährt langsamer. Die Kälteleistung sinkt entsprechend.
- **Wind** stört den Kondensator nicht, er hilft sogar. Die Sonne stört, wenn sie den Kondensator aufheizt. Deshalb Schatten, Luft von der Nordseite ansaugen, Luftführung so, dass keine warme Abluft zurückströmt.
- **R290 ist brennbar.** Bei weniger als 150 g im hermetischen Kreis und Aufstellung im Freien ist das üblich beherrschbar (kleine Füllmenge). Montage und Befüllung gehören in die Hand eines Kälte-Fachbetriebs.
- **Trinkwasser:** doppelwandiger Tauscher (EN 1717), kein Stagnationsbetrieb. Kaltes Wasser, das im Rohr wieder auf 25 °C aufwärmt, ist ein Legionellenrisiko.
- **Kosten (grob):** Verdichter, Plattentauscher, Kondensator mit Lüfter, Regelung ≈ 1.000 bis 1.800 €, dazu PV-Modul und Wechselrichter/MPPT ≈ 200 bis 400 €. Eine fertige Kompaktkältemaschine dieser Größe kostet ähnlich oder mehr. Die Sorptionsanlage aus Runde 1 wäre ein Sonderbau im mittleren bis hohen vierstelligen Bereich.
- **Wartung:** Lamellen jährlich reinigen, Filter im Wassereintritt prüfen. Der hermetische Verdichter hält bei sauberer Kondensatorluft etwa 10 bis 15 Jahre.

## 9. Was sich gegenüber Runde 1 geändert hat

- **Antrieb gewechselt:** Statt Sorption jetzt ein Verdichter. Das Silikagel-Gleichgewicht trug bei luftgekühlten 40 °C nicht, der COP war zu optimistisch, und die Nacht war nicht lösbar.
- **Strom vollständig:** Lüfter mit realem Wirkungsgrad, Regelung und Frostschutz sind eingerechnet (224 W statt 65 W).
- **Erdreich korrigiert:** Es taugt nur als Vorkühlung auf etwa 15 °C, nicht als Senke für den 8-°C-Verdampfer.
- **Bilanz sauber:** Leitungswasser mit realem Eintritt 24 °C, PV-Abwärme mitgerechnet, keine stationären Ersatzknoten für wechselnde Bauteile.
- **Verdampfer** mit Plattentauscher und konservativem U nachgerechnet, mit Frostschutz und Trinkwasserschutz.

```json
{
  "knoten": {
    "Sonne": {"T_C": 5500, "rolle": "umgebung"},
    "Luft": {"T_C": 32, "rolle": "umgebung"},
    "Leitungswasser": {"T_C": 24, "rolle": "umgebung"},
    "PV": {"T_C": 60, "rolle": "komponente"},
    "Verdichter": {"T_C": 55, "rolle": "komponente"},
    "Kondensator": {"T_C": 45, "rolle": "komponente"},
    "Verdampfer": {"T_C": 5, "rolle": "komponente"},
    "Hilfsantriebe": {"T_C": 40, "rolle": "komponente"}
  },
  "stroeme": [
    {"von": "Sonne", "nach": "PV", "W": 1280, "art": "strahlung"},
    {"von": "PV", "nach": "Luft", "W": 1056, "art": "waerme"},
    {"von": "PV", "nach": "Verdichter", "W": 194, "art": "arbeit"},
    {"von": "PV", "nach": "Hilfsantriebe", "W": 30, "art": "arbeit"},
    {"von": "Hilfsantriebe", "nach": "Luft", "W": 30, "art": "waerme"},
    {"von": "Leitungswasser", "nach": "Verdampfer", "W": 697, "art": "waerme"},
    {"von": "Verdampfer", "nach": "Verdichter", "W": 948, "art": "stoff"},
    {"von": "Verdichter", "nach": "Kondensator", "W": 1142, "art": "stoff"},
    {"von": "Kondensator", "nach": "Verdampfer", "W": 251, "art": "stoff"},
    {"von": "Kondensator", "nach": "Luft", "W": 891, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Leitungswasser", "T_ein_C": 24, "T_aus_C": 12, "kuehlleistung_W": 697},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```