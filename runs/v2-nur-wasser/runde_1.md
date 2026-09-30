# Wasserleitung kühlen mit Verdunstungskälte im geschlossenen Kreislauf

## 1. Kurzfassung

**Das Problem:** Ein reiner Verdunster-Kondensator-Loop (zwei Türme, Rohr dazwischen) kühlt nicht. Der Dampf strömt nur dorthin, wo der Druck niedriger ist, also zur kälteren Stelle. Der Kondensator müsste kälter sein als das zu kühlende Rohr. Nachts kann der Himmel das ein paar Kelvin weit leisten, tagsüber nicht (siehe Variante B).

**Die Lösung:** Der Kreislauf muss eine Wärmepumpe sein, die mit Sonnenwärme und einem Feststoff-Sorbens (Silikagel) arbeitet, mit Wasser als einzigem Arbeitsmittel. Das ist ein Adsorptionskühler ohne Strom.

- **Nachts** verdampft Wasser bei ca. 6 °C im Unterdruck (ca. 1 kPa) am Speicher der Leitung. Das Silikagel bindet den Dampf, er kondensiert also nicht am Verdampfer. Die Adsorptionswärme geht an die Nachtluft.
- **Tagsüber** heizt die Sonne das Silikagel auf ca. 90 °C. Der Dampf wird ausgetrieben und kondensiert in einem separaten, verrippten Kondensator bei ca. 40 °C. Die Kondensationswärme geht an die Umgebungsluft.
- Das Kondensat fließt durch die Schwerkraft über einen Siphon zurück in den Verdampfer.

**Wo bleibt die Kondensationswärme?** In der Außenluft, am Kondensator, bei ca. 40 °C und damit deutlich wärmer als das Kühlgut. Die Wärme wird über das Sorbens und die Sonnenwärme "bergauf" gepumpt (von ca. 6 °C auf ca. 40 °C). Ohne diesen Antrieb wäre die Bilanz netto null.

**Ergebnis (24-h-Mittel, Auslegungsfall):**

| | Balkon | Fassade |
|---|---|---|
| Kollektorfläche | 2,5 m² | 10 m² |
| Kälte ans Leitungswasser | ca. 1,4 kWh/Tag (Mittel 59 W) | ca. 6 kWh/Tag (Mittel ca. 250 W) |
| Menge (24 → 10 °C) | ca. 85 L/Tag | ca. 350 L/Tag |
| Auslauftemperatur | 9–14 °C, Mittel ca. 10 °C | ebenso |
| Strom | 0 W | 0 W |
| Wasserverlust | 0 | 0 |

An bewölkten Tagen sinkt die Menge etwa proportional zur Einstrahlung, also auf 20–40 L/Tag.

---

## 2. Warum offene Verdunstung und der einfache Loop nicht reichen

- **Feuchtkugelgrenze:** Bei 32 °C und 40 % r. F. liegt die Kühlgrenzen­temperatur bei ca. 22 °C, der Taupunkt bei ca. 17 °C. Ein nasser Lappen kühlt Wasser von 24 °C also höchstens auf ca. 22–23 °C. In der Sonne ist es noch weniger. Zudem geht das Wasser in die Atmosphäre verloren (ca. 1,5 L pro kWh Kälte).
- **Geschlossener Loop ohne Antrieb:** Verdampfer und Kondensator hätten dieselbe Temperatur, der Dampf strömt nicht, und die Kühlung ist null. Ein Thermosiphon (Wärmerohr) transportiert nur Wärme zu einem kälteren Kondensator.
- **Konsequenz:** Man braucht entweder eine kältere Senke (Nachthimmel, nur wenige K) oder einen Antrieb mit Hochtemperaturwärme. Die Sorption ist der stärkere Weg, weil die Sonne Wärme mit ca. 90 °C liefert.

---

## 3. Prinzip des Sorptionskreislaufs

```
NACHT (Adsorption, Kälteproduktion)         TAG (Desorption, Regeneration)

 Verdampfer 6 °C, ca. 1 kPa                  Adsorber 90 °C, ca. 7 kPa
   Wasser verdampft, nimmt Wärme auf           Sorbens gibt Wasserdampf ab
   aus dem Kältespeicher                       (Sonnenwärme)
        | Dampf                                     | Dampf
        v                                           v
 Adsorber ca. 25-30 °C                       Kondensator ca. 40 °C
   Silikagel bindet Dampf,                     Dampf kondensiert, Wärme
   Wärme an Nachtluft (Kamin)                  an Außenluft
                                                    | Kondensat, Schwerkraft
                                                    v (Siphon)
                                             Verdampfer (wartet auf die Nacht)
```

**Passive Steuerung ohne Strom:**
- **Zwei Rückschlagklappen (Dampfleitungen):**
  - R1 (Adsorber → Kondensator) öffnet nur, wenn p_Adsorber > p_Kondensator, also tags.
  - R2 (Verdampfer → Adsorber) öffnet nur, wenn p_Verdampfer > p_Adsorber, also nachts.
- **Siphon in der Kondensatleitung:** Der Druckunterschied Kondensator/Verdampfer beträgt tags bis ca. 6 kPa, das entspricht 0,6 m Wassersäule. Ein U-Siphon mit ≥ 1 m Tiefe hält das Vakuum und lässt das Kondensat trotzdem durch. Die Schwerkraft reicht, wenn der Kondensator höher liegt als der Verdampfer.
- **Kühlung des Adsorbers nachts:** Ein Hinterlüftungskanal mit Kamineffekt führt die Adsorptionswärme ab. Ein Wachs-Dehnstoff-Element mit Feder schließt die Lüftungsklappen tagsüber und öffnet sie nachts, ohne Strom.

---

## 4. Aufbau Balkon (Skizze, Seitenansicht)

```
   Sonne  \  \  \                                    Süd
           \  \  \
 Kondensator K            ______________________
 (verrippt, im Schatten, /  Glas / Selektiv-      /
 Wind erwünscht)        /   absorber + ADSORBER  /   3,0 m x 0,85 m = 2,5 m²
 ca. 1,8 m Höhe        /    (Silikagel, 32 kg,  /    35° geneigt
  ___                 /     Alu-Lamellen)      /
 |   |=== R1 =========/  ^                    /
 | K |   Dampf tags  /___|___________________/
 |___|                    | Hinterlüftung: Kamin, Wachsklappe
   |  Kondensat           |
   |  (Fallrohr)          | Dampfleitung 2 (nachts), R2
   U  Siphon >= 1 m       |
   |___                   |
       \__________________|
   +----------------------------------+
   | VERDAMPFER-MANTEL (Doppelwand,   |   Stahl/Kupfer, evakuiert
   | Kapillardocht, 2-3 L Wasser)     |
   |  +----------------------------+  |
   |  | Speicherbad ca. 150 L      |  |  100 mm Dämmung
   |  | 5 ... 14 °C                |  |
   |  | Trinkwasser-Edelstahlwendel|  |  Gegenstrom: 24 °C oben rein,
   |  | ca. 20 m, DN20             |  |  kalt unten raus
   |  +----------------------------+  |
   +----------------------------------+   Grundfläche ca. 0,7 x 0,7 m
```

**Bauteile und Werkstoffe:**
- Arbeitsmittel: Wasser, ca. 2,5 kg pendeln pro Tag, Gesamtfüllung ca. 5 L. Die Anlage ist geschweißt und vakuumdicht, mit Kupfer oder Edelstahl 316L. Bei normalem Stahl entsteht Wasserstoff (nicht kondensierbares Gas).
- Sorbens: Silikagel (Typ RD, ungiftig, nicht brennbar), alternativ SAPO-/AQSOA-Zeolith, der schon bei 60–80 °C regeneriert.
- **Keine Salzlösungen:** Feste Sorbentien brauchen keine Pumpen und haben keine Kristallisationsprobleme. LiBr ist korrosiv, und CaCl₂-Lösung bräuchte Umwälzung.
- Verdampfer: Doppelwand-Speicher. Ein Kapillardocht (Edelstahlfilz) benetzt die Mantelwand. Das Speicherwasser kühlt durch die Innenwand, und das Trinkwasser fließt in einer Edelstahl-Wellrohrwendel im Speicherbad. Der Trinkwasserweg ist so vom Vakuumsystem getrennt.
- Der kalte Speicher (≤ 14 °C) verhindert Legionellenwachstum (Risikobereich ca. 25–45 °C).

**Fassade (4 Stockwerke, 12–14 m):** Die Höhe wird sinnvoll genutzt:
- Kollektor-Adsorber-Felder oben (ca. 10 m², Sägezahn-Anordnung mit ≥ 30° Neigung, senkrecht müsste die Fläche etwa verdoppelt werden).
- Kondensator oben im Schatten, langes Fallrohr, Siphon unten.
- Verdampfer und Speicher (ca. 500 L) unten nahe der Zapfstelle.
- Die 13 m lange Dampfleitung (DN100) macht keine Probleme: bei ca. 4,6 m/s und ρ_Dampf ≈ 0,008 kg/m³ sind es nur ca. 2 Pa Druckabfall, gegenüber ca. 80 Pa pro K Verdampfertemperatur.
- Der Kamin über 10 m Höhe liefert ca. 4 Pa Auftrieb und damit ca. 1,5–2 m/s Luftgeschwindigkeit. Das reicht für über 1 kW Wärmeabfuhr nachts.

---

## 5. Rechnung Balkon (Auslegungsfall)

**Annahmen:** Tagessumme 7 kWh/m²·d auf geneigter Fläche (Spitze 800 W/m²), 2,5 m² Aperturfläche.

**Solarseite:**
- Einstrahlung: 2,5 × 7 = 17,5 kWh/d, entspricht 729 W im 24-h-Mittel.
- Absorbiert (τα = 0,8): 583 W.
- Nutzbar am Sorbens: 129 W, also 3,1 kWh/d oder 17,7 % der Einstrahlung. Das ist bewusst konservativ. Ein schwerer Adsorber mit ca. 90 °C und Verlusten von ca. 6 W/m²K schneidet eher schwach ab.

**Zyklusbedarf:**
- Silikagel 32 kg mit Δx ≈ 0,08 kg/kg (0,15 → 0,07 zwischen Nacht und Tag) ergibt 2,5 kg Wasser pro Zyklus.
- Desorptionswärme pro Tag: 2,5 kg × 2,85 MJ/kg = 7,1 MJ. Dazu kommt die fühlbare Wärme von Sorbens und Gehäuse (ca. 70 K): 4,1 MJ. Summe ca. 11,2 MJ = 3,1 kWh ✓.

**Kälteseite:**
- Verdampfung bei 6 °C: 2,5 kg × 2,49 MJ/kg = 6,2 MJ = 72 W im Mittel.
- Das Kondensat kommt mit ca. 40 °C zurück: 2,5 × 4,19 × 34 = 0,36 MJ = 4,1 W Wärmeeintrag.
- Netto kommt aus dem Speicher: 72,0 − 4,1 = 67,9 W, also 1,63 kWh/d.
- Speicherverluste bei 100 mm Dämmung, 1,7 m² und ΔT ≈ 22 K: ca. 9 W.
- **Nutzkälte an das Leitungswasser: 59 W, also 1,42 kWh/d.**

**Wassermenge:** Bei 24 → 10 °C (14 K) sind das 1,163 × 14 = 16,3 Wh/kg. Daraus folgen 1420 / 16,3 ≈ **87 L/Tag**.

**Plausibilitätsprüfung mit Carnot:**
- Temperaturen: T_Verd = 279 K, T_Kond = 313 K, T_Antrieb = 363 K.
- COP_Carnot = (279/34) · (50/363) ≈ 1,13.
- COP_th des Zyklus = 1,63 / 3,1 ≈ 0,52 = 46 % von Carnot. Das ist realistisch (Literatur: 30–60 %).
- Solar-COP = 1,63 / 17,5 ≈ 0,09, was den üblichen Werten solarer Adsorptionsanlagen von 0,05–0,15 entspricht.

**Auslauftemperatur:** Die Wendel (ca. 1,3 m² Fläche, UA ≈ 300 W/K) erreicht bei 3 L/min eine Wärmeübertragungs­effektivität von ca. 0,78. Die Auslauftemperatur liegt dann bei ca. 11,5 °C. Bei 5 L/min sind es ca. 14 °C. Morgens ist das Bad bei ca. 5 °C, abends nach 85 L bei ca. 14 °C. Die Speicherkapazität (150 L × 9 K ≈ 1,6 kWh) passt zur Tagesproduktion.

**Leistungsspitzen:**
- Tagsüber Kondensation bis ca. 280 W (Kondensatorfläche 3–4 m² verrippt, ΔT ≈ 8 K).
- Nachts Verdampfung ca. 200 W.
- Der Adsorber muss nach Sonnenuntergang ca. 400 W Wärme abgeben können. Dafür sind Kamin und Hinterlüftung ausgelegt.

**Fassadenvariante (10 m²):** Skalierung ×4 ergibt netto ca. 250 W im Mittel, also 6,1 kWh/d. Das sind ca. 370 L/Tag bei 24 → 10 °C, bei rund 130 kg Silikagel und 500 L Speicher. Für ein 4-Familien-Haus mit 50–100 L pro Haushalt passt das. Der Bedarf von 200 L pro Haushalt ließe sich mit ca. 6 m² Kollektor pro Haushalt decken.

---

## 6. Energiebilanz (24-h-Mittel, Tag+Nacht)

| Strom | Leistung |
|---|---|
| Sonne → Kollektor (absorbiert) | 583 W |
| Kollektor → Adsorber (Antrieb) | 129 W |
| Kollektor → Luft (Verluste) | 454 W |
| Verdampfer → Adsorber (Dampf, nachts) | 72,0 W |
| Adsorber → Kondensator (Dampf, tags) | 76,4 W |
| Adsorber → Luft (Adsorptionswärme, Abkühlung) | 124,6 W |
| Kondensator → Luft (**Kondensationswärme**) | 72,3 W |
| Kondensator → Verdampfer (Kondensat) | 4,1 W |
| Speicher → Verdampfer | 67,9 W |
| Leitungswasser → Speicher | 59,0 W |
| Luft → Speicher (Verlust) | 8,9 W |

Gesamtbilanz: Zufuhr von 651 W (Sonne 583 + Leitungswasser 59 + Speicherverlust 9) entspricht der Abgabe an die Luft von 651 W. Die Sonne treibt also die Wärmepumpe an, und die Kondensationswärme landet vollständig in der Außenluft.

---

## 7. Variante B: rein passiv, schwächer, ohne Sorbens

Ein Thermosiphon aus Wasser bei ca. 15 °C (evakuiertes Kupferrohr) verbindet die Speicherwendel mit einer Strahlungsfläche, die nachts zum klaren Himmel abstrahlt.

- Bei 20 °C Luft, Taupunkt ca. 17 °C und Paneltemperatur ca. 15 °C sind netto nur ca. 20–30 W/m² möglich (Strahlung ca. 43 W/m² minus Konvektionsgewinn). Unter dem Taupunkt kommt außerdem Tau auf das Panel.
- 3 m² ergeben ca. 0,6–0,9 kWh pro Nacht, also ca. 40 L/Tag auf ca. 15–17 °C.
- Tagsüber wirkt das Panel nicht (Sonne), es muss abgedeckt werden.

Variante B ist einfach und robust. Für Auslauftemperaturen deutlich unter 15 °C reicht sie nicht. Sie lässt sich mit dem Sorptionskreislauf kombinieren: Das Panel kühlt nachts den Adsorber.

---

## 8. Grenzen und Risiken

- **Vakuumdichtheit** ist die größte Praxisfrage. Undichtigkeiten bringen Luft ins System und stoppen die Kühlung. Nötig sind Schweißnähte statt Verschraubungen und eine einmalige Evakuierung mit Vakuumpumpe beim Bau. Das ist Wartung, kein Betriebsstrom. Alle paar Jahre kann Nachevakuieren nötig sein.
- **Rückschlagklappen:** Die Öffnungsdrücke müssen unter ca. 30 Pa liegen (≈ 0,4 K Verdampfertemperatur). Es braucht große Klappen (DN50–100) und dichte Dichtungen. Sie sind das empfindlichste Bauteil.
- **Verdampfertemperatur:** Sie fällt mit der Beladung von ca. 6 auf ca. 2 °C. Unter 0,6 kPa Dampfdruck (0 °C) würde der Verdampfer vereisen. Die Beladung wird deshalb begrenzt, und das Bad bleibt ≥ 5 °C.
- **Wetter:** Die Leistung ist proportional zur Einstrahlung und fällt bei Bewölkung stark ab. Nachts bringt die Anlage nur, was tagsüber regeneriert wurde. Bei Hitzeperioden mit Kondensator > 45 °C sinkt der Ertrag.
- **Sicherheit:** Der Adsorber erreicht ca. 100 °C und braucht Berührungsschutz. Das Vakuum verlangt druckfeste Behälter (außen 100 kPa).
- **Annahmen** (Einstrahlung 7 kWh/m²d, Δx = 0,08, τα = 0,8, Kollektorverluste) müssen an einem Prototyp gemessen werden. Die Unsicherheit liegt bei ca. ±30 %.
- **Strom:** 0 W. Es gibt keine Pumpen, Ventilatoren oder Regelung. Antrieb sind Sonne, Schwerkraft, Kamineffekt und der Tag/Nacht-Wechsel.

---

```json
{
  "knoten": {
    "Sonne": {"T_C": 5500, "rolle": "umgebung"},
    "Luft": {"T_C": 32, "rolle": "umgebung"},
    "Leitungswasser": {"T_C": 24, "rolle": "umgebung"},
    "Kollektor": {"T_C": 80, "rolle": "komponente"},
    "Adsorber": {"T_C": 60, "rolle": "komponente"},
    "Kondensator": {"T_C": 40, "rolle": "komponente"},
    "Verdampfer": {"T_C": 6, "rolle": "komponente"},
    "Kaeltespeicher": {"T_C": 8, "rolle": "komponente"}
  },
  "stroeme": [
    {"von": "Sonne", "nach": "Kollektor", "W": 583, "art": "strahlung"},
    {"von": "Kollektor", "nach": "Adsorber", "W": 129, "art": "waerme"},
    {"von": "Kollektor", "nach": "Luft", "W": 454, "art": "waerme"},
    {"von": "Verdampfer", "nach": "Adsorber", "W": 72.0, "art": "stoff"},
    {"von": "Adsorber", "nach": "Kondensator", "W": 76.4, "art": "stoff"},
    {"von": "Adsorber", "nach": "Luft", "W": 124.6, "art": "waerme"},
    {"von": "Kondensator", "nach": "Luft", "W": 72.3, "art": "waerme"},
    {"von": "Kondensator", "nach": "Verdampfer", "W": 4.1, "art": "stoff"},
    {"von": "Kaeltespeicher", "nach": "Verdampfer", "W": 67.9, "art": "waerme"},
    {"von": "Leitungswasser", "nach": "Kaeltespeicher", "W": 59.0, "art": "waerme"},
    {"von": "Luft", "nach": "Kaeltespeicher", "W": 8.9, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Leitungswasser", "T_ein_C": 24, "T_aus_C": 10, "kuehlleistung_W": 59.0},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```