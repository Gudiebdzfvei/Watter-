# Wasserleitung kühlen mit geschlossenem Verdunstungskreislauf

## 1. Kurzantwort

**Das Problem ist real und lässt sich mit einem einzigen Druck im Kreislauf nicht lösen.** In einem geschlossenen Rohr mit reinem Wasser und Dampf hängen Druck und Temperatur fest zusammen (Sattdampfkurve). Verdampfer und Kondensator haben dann praktisch dieselbe Temperatur. Die Kondensationswärme kann dann nur an etwas abgegeben werden, das kälter ist als das Wasser, das man kühlen will. Die Außenluft mit 32 °C ist das nicht. Ein solcher Loop ist ein Wärmerohr: Es transportiert Wärme, erzeugt aber keine Kälte.

**Lösung:** Der Kondensator muss deutlich wärmer sein als der Verdampfer, nämlich wärmer als die Außenluft. Dafür braucht der Kreislauf zwei Druckniveaus und eine Vorrichtung, die den Dampf vom niedrigen auf den hohen Druck bringt. Ohne Strom geht das mit einem **thermischen Verdichter**, einer Sorptionseinheit (Silikagel und Wasser), die mit Sonnenwärme angetrieben wird. Das ist eine solare Adsorptionskältemaschine mit Wasser als Kältemittel. Sie passt gut zu deiner Idee mit den zwei Türmen.

**Wo bleibt die Kondensationswärme?** Sie geht im Kondensator bei etwa 40 °C an die 32 °C warme Luft (737 W). Zusätzlich gibt der Adsorber etwa 1960 W bei etwa 40 °C an die Luft ab. Das ist ein normaler Wärmefluss von warm nach kalt. Bezahlt wird mit Sonnenwärme von etwa 90 °C.

## 2. Warum der naive Loop nichts bringt

| Größe | Wert (32 °C, 40 % r.F.) |
|---|---|
| Kühlgrenztemperatur (offene Verdunstung, „nasser Lappen") | ca. 22 °C |
| Taupunkt der Luft | ca. 17 °C |
| Sättigungsdruck bei 8 °C / 40 °C | 1,07 kPa / 7,4 kPa |

- **Nasser Lappen (offen):** Der Wasserdampf diffundiert in die Luft, die Verdampfungswärme verlässt das System mit dem Dampf. Das funktioniert nur, solange Wasser verloren geht. Die Grenze ist die Kühlgrenztemperatur von etwa 22 °C. Das Leitungswasser hat schon 24 °C, es wären also höchstens 1 bis 2 K Kühlung.
- **Geschlossen mit einem Druck:** Verdampfer und Kondensator liegen bei derselben Temperatur. Steht der Kondensator in der Sonne, wird der „Verdampfer" sogar warm. Die Nettokühlung ist null.
- **Geschlossen mit zwei Drücken:** Der Verdampfer läuft bei 8 °C (1,07 kPa), der Kondensator bei 40 °C (7,4 kPa). Nur so kann der Kondensator seine Wärme an die 32 °C warme Luft abgeben. Der Druckhub von etwa 6,9 kostet Energie.

## 3. Drei Wege, den Druckhub zu erzeugen

| Weg | Prinzip | Aufwand für 700 W Kälte | Bewertung |
|---|---|---|---|
| A: Kälteres Reservoir | Wärmerohr zu einer Senke unter 12 °C: Erdreich (10 bis 12 °C in 2 bis 3 m Tiefe) oder Strahlung zum Nachthimmel | Erdreich: Rohrregister, kein Verdunsten nötig. Strahlung: nur ca. 50 bis 100 W/m² (tagsüber mit Spezialfolie weniger), also über 10 m² | Erdreich ist die einfachste Lösung, wenn Platz da ist. Strahlung taugt eher als Nachtergänzung. |
| B: Elektrischer Verdichter | Kompressionskältemaschine. Mit Wasserdampf selbst nicht baubar (ca. 130 m³/h Dampf bei 1 kPa). Mit R290 oder R134a: COP ≈ 4 | ca. 175 W elektrisch | Kompakt und robust, aber Strom nötig |
| **C: Sorption (gewählt)** | Sorbens saugt den Dampf bei niedrigem Druck auf, Sonnenwärme treibt ihn bei hohem Druck wieder aus | ca. 2 kW Wärme (Sonne) plus ca. 65 W Strom | Wasser bleibt im Kreislauf, fast strom- und verbrauchsfrei |

## 4. Aufbau (Lösung C)

```
             Sonne 800 W/m²
              ↓ ↓ ↓ ↓ ↓
      ┌─────────────────────────┐
      │ Vakuumröhren-Kollektor  │  4 m², ca. 90 °C
      └───────┬───────────▲─────┘
        Heißwasser        │ (Pumpe ~15 W)
              ▼           │
   ┌───────────────┐  Umschaltventile  ┌───────────────┐
   │   BETT A      │◄────────────────►│   BETT B      │
   │  (Desorber)   │  alle ~10 min     │  (Adsorber)   │
   │  85 °C        │  Bett-Rollen      │  40 °C, Luft- │
   │               │  tauschen         │  gekühlt      │
   └───────┬───────┘                   └───────▲───────┘
           │ Klappenventil                     │ Klappenventil
           │ Dampf 7,4 kPa                     │ Dampf 1,07 kPa
           ▼                                   │ (DN 100, kurz)
   ┌───────────────┐                   ┌───────┴───────┐
   │  KONDENSATOR  │                   │  VERDAMPFER   │
   │  40 °C        │                   │  8 °C         │
   │ (Lamellen,    │                   │  Rieselfilm   │◄── Leitung 24 °C
   │  Ventilator)  │                   │  über Rohr-   │──► Leitung 12 °C
   │  →→ Luft 32°C │                   │  wendel       │
   └───────┬───────┘                   └───────▲───────┘
           │ Kondensat („Regen")               │
           └──────► U-Siphon, ≥ 1 m tief ──────┘
                    (hält 6,3 kPa Druckdifferenz)
```

**Was der Aufbau leistet:**
1. Im Verdampfer rieselt Wasser (etwa 10 l/h im Umlauf) über die Wendel mit dem Leitungswasser und verdampft bei 8 °C. Das ist die Kälte.
2. Der Dampf strömt durch ein Klappenventil ins Adsorberbett. Das Silikagel nimmt ihn auf und hält den Druck bei etwa 1 kPa. Das Bett wird mit Luft gekühlt und bleibt bei etwa 40 °C.
3. Das andere Bett wird mit Sonnenwärme auf 85 °C geheizt und gibt den Dampf bei etwa 7,4 kPa wieder ab.
4. Der Dampf kondensiert im Kondensator bei 40 °C. Die Wärme geht an die Luft, denn 40 °C sind wärmer als 32 °C.
5. Das Kondensat fließt durch einen U-Siphon zurück. Die Druckdifferenz von 6,3 kPa entspricht 0,64 m Wassersäule, also braucht der Siphon mindestens 1 m Tiefe. Das ist der Turm-Effekt deiner Idee, nur mit einer Flüssigkeitssäule als Druckschleuse.
6. Alle etwa 10 min tauschen die Betten ihre Rollen. Das geschieht mit wenigen Umschaltventilen und selbsttätigen Klappenventilen. So läuft der Betrieb kontinuierlich, solange die Sonne scheint.

## 5. Rechnung (Auslegungsfall Tag)

**Kühllast:** 50 l/h = 0,0139 kg/s, Auslauf 12 °C.
Q = 0,0139 · 4186 · (24 − 12) ≈ **697 W**

**Verdampfer:**
- Mit gegenströmendem Wasser (24 → 12 °C) und 8 °C Verdampfungstemperatur ergibt sich ΔT_log = 12 / ln(16/4) ≈ 8,7 K.
- Mit U ≈ 600 W/m²K folgt eine Fläche von etwa 0,13 m². Ich plane 0,2 m² ein, also mehrere parallele dünne Rohre mit 5 bis 6 m Länge.
- Ein Rieselfilm ist nötig. Ein Tauchverdampfer geht bei 1 kPa nicht: 10 cm Wassersäule würden den Siedepunkt fast verdoppeln.

**Kältemittelmenge:**
- Das Kondensat kommt mit 40 °C zurück, das kostet 4,19 · 32 = 134 kJ/kg Kälteleistung.
- Netto pro kg Dampf: 2482 − 134 = 2348 kJ/kg.
- Massenstrom: 697 / 2348 000 ≈ 2,97·10⁻⁴ kg/s ≈ **1,07 l/h**. Diese Menge kreist intern und geht nicht verloren.

**Dampfleitung:**
- Volumenstrom: 2,97·10⁻⁴ · 121 m³/kg ≈ 0,036 m³/s ≈ 130 m³/h.
- Mit DN 100 ergeben sich etwa 4,6 m/s, der Druckverlust ist vernachlässigbar. Die Leitung muss kurz sein, und das Gerät muss vakuumdicht geschweißt sein.

**Sorption (Silikagel/Wasser):**
- Bei 40 °C Adsorbertemperatur und 1,07 kPa beträgt die Beladung etwa 0,09 kg/kg. Bei 85 °C und 7,4 kPa sind es etwa 0,035 kg/kg. Der Hub liegt bei etwa 0,055 kg/kg.
- Pro 10-min-Halbzyklus werden 0,18 kg Wasser umgesetzt. Das ergibt etwa 3,2 kg Silikagel pro Bett. Ich plane 5 kg pro Bett ein, jeweils auf einem Lamellenwärmetauscher.

**Wärmebedarf:**
- Ich nehme einen thermischen COP von 0,35 an. Für kleine Silikagel-Maschinen bei luftgekühltem Betrieb mit 32 °C Umgebung sind 0,3 bis 0,5 üblich.
- Antriebswärme: 697 / 0,35 ≈ **2000 W**.
- Plausibilitätsprüfung mit Carnot für Antrieb 85 °C, Abfuhr 38 °C und Verdampfer 8 °C: COP_max ≈ 1,2. Mein Wert liegt bei etwa 28 % davon, das ist realistisch.

**Kollektor:**
- 4 m² Aperturfläche (Vakuumröhren) empfangen 3200 W.
- Bei 90 °C Betriebstemperatur ist der Wirkungsgrad etwa 0,625, das ergibt 2000 W nutzbar.
- Verluste an die Luft: etwa 400 W (mit Rohrverlusten). Wind stört Vakuumröhren kaum.

**Luftkühler (Kondensator + Adsorber):**
- Abzuführen sind etwa 2700 W bei einer Lufterwärmung von 32 auf 37 °C.
- Luftstrom: etwa 0,5 m³/s. Bei ΔT_log ≈ 5 K sind etwa 15 m² Lamellenfläche nötig, das ist ein kleines Register.

**Strom (ehrlich):**

| Verbraucher | Leistung |
|---|---|
| Kollektorpumpe | ca. 15 W |
| Sprühpumpe Rieselfilm | ca. 5 W |
| Ventilator (Niederdruck, EC) | ca. 40 W |
| Ventile, Steuerung | ca. 5 W |
| **Summe** | **ca. 65 W** |

Das entspricht einer Leistungszahl von etwa 10 (697 W Kälte für 65 W Strom). Ein kleines PV-Modul mit etwa 0,4 m² deckt das direkt. Nachts fehlt der Solarbetrieb.

**Wasserverlust:** 0 l/Tag. Der Kreislauf ist zu, und das Kältemittel geht nicht verloren.

## 6. Wo die Energie bleibt (Tagesbetrieb, Bilanz)

| Zufuhr | W |
|---|---|
| Sonne (absorbiert) | 2400 |
| Wärme aus dem Leitungswasser | 697 |
| Strom | 65 |
| **Summe** | **3162** |

| Abfuhr an die Luft | W |
|---|---|
| Adsorber | 1960 |
| Kondensator | 737 |
| Kollektorverluste | 400 |
| Ventilator, Pumpen | 65 |
| **Summe** | **3162** |

Nichts geht verloren und nichts entsteht neu. Die Kondensationswärme (737 W) landet im Kondensator bei 40 °C, alle weiteren Wärmen bei etwa 40 °C an der Luft. Die 697 W aus dem Wasser wandern über Verdampfen, Adsorbieren und Wärmeabfuhr an die Außenluft.

## 7. Grenzen und ehrliche Einschränkungen

- **Nur bei Sonne:** Ohne Wärmespeicher gibt es nachts keine Kühlung. Ein 500-l-Heißwasserspeicher (ΔT 30 K) fasst etwa 17 kWh, das reicht bei 2 kW Antrieb für etwa 8 h. Dafür wäre der Kollektor auf etwa 8 m² zu verdoppeln. Nachts ist es kühler (20 °C), der Kondensator läuft dann bei etwa 28 °C, und der COP steigt auf etwa 0,5.
- **Wolken:** Bei 400 W/m² sinkt die Leistung etwa auf die Hälfte.
- **Aufwand:** Die Anlage ist größer als ein Kompressor-Kühlgerät (Kollektor, Sorptionsbetten, Vakuumtechnik). Für 0,7 kW gibt es keine Serienmaschine, kommerzielle Adsorptionskältemaschinen beginnen bei etwa 8 kW. Es wäre ein Eigenbau oder eine Sonderanfertigung.
- **Vakuum:** Verdampfer und Bett müssen dauerhaft dicht sein. Nicht kondensierbare Gase (Luft) müssen gelegentlich abgesaugt werden.
- **Temperaturgrenzen:** Der Verdampfer darf nicht unter etwa 5 °C gehen (Einfriergefahr). Bei 10 °C Auslauf sinkt die Verdampfungstemperatur auf etwa 6 °C, der COP fällt, und die Leistung steigt auf etwa 810 W. Bei 15 °C Auslauf sind es nur etwa 520 W.
- **Alternativen:** Mit Erdreich (Weg A) geht es einfacher, wenn Platz für ein Erdregister da ist. Wenn 175 W Strom akzeptabel sind, ist eine kleine Kompressionskältemaschine (Weg B) die pragmatischste Lösung.

```json
{
  "knoten": {
    "Sonne": {"T_C": 5500, "rolle": "umgebung"},
    "Luft": {"T_C": 32, "rolle": "umgebung"},
    "Leitungswasser": {"T_C": 18, "rolle": "umgebung"},
    "Strom": {"T_C": 32, "rolle": "umgebung"},
    "Kollektor": {"T_C": 90, "rolle": "komponente"},
    "Desorber": {"T_C": 85, "rolle": "komponente"},
    "Adsorber": {"T_C": 40, "rolle": "komponente"},
    "Kondensator": {"T_C": 40, "rolle": "komponente"},
    "Verdampfer": {"T_C": 8, "rolle": "komponente"},
    "Hilfsantriebe": {"T_C": 40, "rolle": "komponente"}
  },
  "stroeme": [
    {"von": "Sonne", "nach": "Kollektor", "W": 2400, "art": "strahlung"},
    {"von": "Kollektor", "nach": "Desorber", "W": 2000, "art": "waerme"},
    {"von": "Kollektor", "nach": "Luft", "W": 400, "art": "waerme"},
    {"von": "Leitungswasser", "nach": "Verdampfer", "W": 697, "art": "waerme"},
    {"von": "Verdampfer", "nach": "Adsorber", "W": 737, "art": "stoff"},
    {"von": "Desorber", "nach": "Kondensator", "W": 777, "art": "stoff"},
    {"von": "Kondensator", "nach": "Verdampfer", "W": 40, "art": "stoff"},
    {"von": "Desorber", "nach": "Adsorber", "W": 1223, "art": "waerme"},
    {"von": "Adsorber", "nach": "Luft", "W": 1960, "art": "waerme"},
    {"von": "Kondensator", "nach": "Luft", "W": 737, "art": "waerme"},
    {"von": "Strom", "nach": "Hilfsantriebe", "W": 65, "art": "arbeit"},
    {"von": "Hilfsantriebe", "nach": "Luft", "W": 65, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Leitungswasser", "T_ein_C": 24, "T_aus_C": 12, "kuehlleistung_W": 697},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```