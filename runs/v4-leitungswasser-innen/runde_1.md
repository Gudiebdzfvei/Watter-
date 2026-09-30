# Zimmerkühlung mit Leitungswasser: Lüfter-Kühlregister, Wasser im Durchlauf

## 1. Kurzfazit

- **Es geht ohne Draußen-Aufbau, komplett in der Wohnung.** Ein Wasser-Luft-Register (Kfz-Heizungswärmetauscher) mit zwei kleinen PC-Lüftern (zusammen ≈ 3 W) holt etwa **280 W** aus dem Zimmer.
- **Wirkung:** Nachmittagsspitze ≈ **27 °C statt 30 °C**. Mit Hitzeschutzfolie auf dem Fenster und Nachtlüftung bleiben ≈ **26 °C** erreichbar.
- **Der Haken ist die Wassermenge:** Wasser trägt wenig Kälte. Für 280 W über 10 h braucht man **≈ 300 l/Tag**, das sind ≈ 1,35 €/Tag. Nach Weiterverwendung (Toilette, Pflanzen) bleiben ≈ 1 €/Tag Nettomehrkosten.
- **Kosten pro kWh Kälte:** ≈ 0,48 €. Ein Klimagerät schafft das mit Strom für ≈ 0,10–0,15 €. Die Wasserlösung lohnt deshalb nur als **Spitzenkappung an einigen Hitzetagen**, nicht als Dauerbetrieb, und am besten dort, wo das Wasser sinnvoll weiterverwendet wird.
- **Stromlose Variante:** Hoch montierte Heizkörper mit natürlicher Konvektion leisten 2 × ≈ 130 W, brauchen aber viel mehr Platz (siehe 4.3).

## 2. Physik: Wie viel Kälte steckt im Liter?

Wasser nimmt **1,163 Wh/(l·K)** auf.

| Erwärmung ΔT | Wh pro Liter | Liter pro kWh Kälte |
|---|---|---|
| 5 K (15→20 °C) | 5,8 | 172 |
| **8 K (15→23 °C)** | **9,3** | **107** |
| 10 K (15→25 °C) | 11,6 | 86 |

Die Austrittstemperatur kann nie über die Raumlufttemperatur steigen. Bei 27 °C Raumluft sind 23–24 °C praktisch das Maximum. Ein Gegenstrom-Register und niedriger Durchfluss nutzen das aus. Mehr Durchfluss kühlt nicht besser, er verschwendet nur Wasser.

## 3. Wärmelast (Auslegungsfall)

Zimmer 20 m² × 2,5 m = 50 m³, mittleres Geschoss, 2 m² Fenster nach Südwest mit Innenvorhang. Außenluft 30 °C. Mittel 9–19 Uhr:

| Quelle | W |
|---|---|
| Sonne durch Fenster (2 m² × 400 W/m² × g_eff 0,45) | 360 |
| Wände/Fenster (Sonnenaufheizung, ΔT_eff ≈ 6–8 K) | 80 |
| Fugenlüftung (0,3/h) | 20 |
| 1 Person + Laptop/Licht (davon ≈ 40 W latent) | 150 |
| **Spitze / Mittel 9–19 Uhr** | **≈ 610 / ≈ 450** |

Das sind ≈ 4,5 kWh in 10 h. Die Speichermasse des Raums schätze ich auf ≈ 1 kWh/K (mittelschwer). Ohne Gerät steigt der Raum nach Nachtlüftung von ≈ 25,5 °C auf **≈ 30 °C**.

## 4. Aufbau

### 4.1 Prinzip

Der Raumluftstrom (≈ 70 m³/h) wird von zwei Lüftern durch zwei Register in Reihe gezogen. Das Wasser läuft im **Gegenstrom** hindurch, erst durch das kalte Register B, dann durch das wärmere Register A. Danach fließt es über einen **freien Auslauf** in einen Sammelbehälter.

```text
 Kaltwasser-Eckventil / Waschmaschinenhahn (Wand)
   │
 [1 Absperrhahn] ─ [2 Geräteventil m. Rückflussverhinderer (EA)]
   │
 [3 Aquastop-Schlauch, isoliert] ─ [4 Regulierventil, ca. 30 l/h]
   │  15 °C
   ▼ (Zulauf unten)
 ┌────────────── Gehäuse (Multiplex), steht erhöht, z. B. Regal 1,5 m ──────────┐
 │                                                                              │
 │  Raumluft   ┌────────────┐   ┌────────────┐   Lüfter ×2      kühle Luft      │
 │  27 °C ────►│ Register A │──►│ Register B │──► 120 mm ──────► ≈ 19 °C ──►    │
 │             │ (wärmer)   │   │ (kälter)   │    (3 W)                         │
 │             └─────▲──────┘   └─────▲──────┘                                  │
 │   Wasser:  Auslauf│ 23 °C ◄────────┘ Zulauf 15 °C → B → A                    │
 │ ┌──────────────── Tropfwanne (Gefälle 2 %) ──────────────┐                   │
 └─┴─────────────────────────┬──────────────────────────────┴───────────────────┘
                             │ Kondensat ≈ 1 l/Tag
   freier Auslauf 23 °C (≥ 20 mm über Wasserspiegel) ▼
                  ┌────── Sammelbehälter 30 l ──────┐ Überlauf → Badewanne/WC
                  └─────────────────────────────────┘ → Eimer für WC-Spülung, Pflanzen
```

### 4.2 Leistungsrechnung (Lüfter-Variante)

- **UA:** Zwei Kfz-Heizungswärmetauscher in Reihe haben bei ≈ 0,5 m/s Anströmung geschätzt UA ≈ 54 W/K (Unsicherheit ±30 %).
- **Stoffströme:** Luft C_L = 70 m³/h ≈ 23,5 W/K, Wasser (30 l/h) C_W ≈ 35 W/K.
- **Wirkungsgrad:** NTU = 2,3 und C_L/C_W = 0,68 ergeben im Gegenstrom ε ≈ 0,77.
- **Sensible Leistung:** 0,77 × 23,5 × (27 − 15) ≈ **218 W**.
- **Latente Leistung (Kondensation):** ≈ 60 W. Die Oberfläche liegt teils unter dem Taupunkt von ≈ 15,5 °C.
- **Summe:** ≈ 280 W aus dem Raum.
- **Wasseraufnahme:** 280 W + 3 W Lüfterabwärme = 283 W, also 15 → 23,1 °C bei 30 l/h.
- **Lüfter-Nutzen:** Der Lüfter verbraucht 3 W und bewirkt etwa das 90-Fache davon an Kühlleistung. Das ist die Kälte des Wassers, keine Kältemaschine.

### 4.3 Reicht natürliche Konvektion?

Nur mit viel Fläche und nur hoch montiert, weil kalte Luft nach unten fällt. Ein tief montierter Kühler bildet nur eine Kaltluftpfütze am Boden.

- **Glatte Kühlfläche (Kühldecke):** ≈ 8–10 W/(m²·K) inklusive Strahlung, also ≈ 70 W/m² bei ΔT = 8 K. Für 280 W wären das 4 m². Das ist nicht machbar, weil die Oberfläche mit 15 °C Wasser unter dem Taupunkt läge und tropfen würde. Kühldecken brauchen Wasser ≥ 18–19 °C oder Mischkreis mit Pumpe. Davon rate ich ab.
- **Panel-Heizkörper Typ 22, 600 × 1000 mm, hoch montiert mit Tropfwanne:** Bei ΔT = 8 K sind es ≈ 110 W trocken, mit Kondensation ≈ 130 W (Nennleistung 1.200 W bei ΔT 50 K, Exponent 1,3).
  - Zwei Stück bringen ≈ 260 W bei ≈ 28 l/h, also ähnlich viel Wasser wie die Lüfter-Variante.
  - Nachteile: je ≈ 30 kg gefüllt, Rost im Frischwasser, Bohren in der Mietwohnung.
  - Das ist eine Notlösung, wenn absolut kein Strom erlaubt ist. Die Lüfter können auch von einem 10-W-Solarmodul am Fenster (≈ 20 €) direkt gespeist werden.

### 4.4 Kondensation und Entfeuchtung

- **Es tropft, und das ist gewollt.** Bei 15–17 °C Oberfläche und Raumtaupunkt 15–17 °C fällt Kondensat an. Die Wanne mit Gefälle und Schlauch führt es in den Sammelbehälter. Ohne Ablauf würde Standwasser schimmeln und Legionellen bilden.
- **Menge:** 60 W ÷ 0,68 Wh/g ≈ 90 g/h ≈ **≈ 1 l pro 10 h**.
- **Vorteil:** Die Entfeuchtung entlastet spürbar. Ich schätze etwa 5 %-Punkte weniger relative Feuchte. Das Kondensat ist kein Trinkwasser, aber gut für Pflanzen.

## 5. Sicherer Trinkwasseranschluss (Gefahr 1: Rückfluss, Gefahr 2: Stagnation)

1. **Eigene Entnahmestelle:** Kaltwasser-Eckventil oder Waschmaschinenhahn, nie die Mischbatterie oder Warmwasser. Ist der Hahn belegt, hilft ein Doppel-Eckventil.
2. **Rückflussverhinderer:** Ein DVGW-geprüftes Geräteventil mit Rückflussverhinderer (Typ EA) sitzt direkt am Hahn. Erwärmtes Wasser zählt nach DIN EN 1717 zu Kategorie 2 und darf nicht zurück in die Leitung.
3. **Freier Auslauf (Typ AA):** Der Schlauchauslauf endet mindestens 20 mm über dem Überlauf des Behälters. Das ist eine zweite, unabhängige Sicherung. Es gibt keine geschlossene Verbindung zu Abwasser oder Behälter.
4. **Stagnation:** Nach dem Betrieb Zulauf schließen und das Register über den Entleerungshahn entleeren. 27 °C warmes Standwasser liegt im Legionellen-Wachstumsbereich (25–45 °C).
5. **Vor jedem Start:** ≈ 5 l in einen Eimer laufen lassen. Die Kaltwasserleitung soll laut DIN 1988-200 ≤ 25 °C haben. Mit Thermometer prüfen.
6. **Dauerdurchfluss** hält die Leitung eher frisch, als dass er sie erwärmt.
7. **Weiterverwendung nur als Brauchwasser** (WC, Pflanzen, Putzen). Nicht trinken, nicht duschen, nicht vernebeln. Register und Behälter beschriften.
8. **Material:** Neue Register in Kupfer/Messing kaufen und gründlich spülen. Keine gebrauchten Kfz-Teile, weil Glykolreste und bleihaltiges Lot möglich sind.
9. **Wasserschaden ist das größte praktische Risiko:** Aquastop-Schlauch, Wassermelder unter Gerät und Behälter, Überlauf zur Badewanne. Bei Abwesenheit Hahn schließen.

## 6. Wasserbedarf, Kosten, Weiterverwendung

**Bilanz der Betriebszeit 9–19 Uhr (10 h):**

| Größe | Wert |
|---|---|
| Durchfluss | 30 l/h → **300 l/Tag** |
| Kälte | 2,8 kWh/Tag, im 24-h-Mittel ≈ 117 W |
| Kosten (4,5 €/m³ Wasser + Abwasser) | **≈ 1,35 €/Tag** |
| Strom (3 W × 10 h) | 0,03 kWh, ≈ 1 ct |

**Weiterverwendung des ≈ 23 °C warmen Wassers:**
- **Toilettenspülung:** 1–2 Personen, ≈ 25–50 l/Tag. Ein Eimer mit 6–10 l in die Schüssel spült ebenfalls.
- **Pflanzen:** ≈ 15 l.
- **Putzen, Handwäsche:** ≈ 15 l.
- **Summe:** ≈ 80 l, in der Wohnung realistisch. Dann bleiben ≈ **220 l/Tag** Nettomehrverbrauch, das sind ≈ **1,0 €/Tag**. Bei 20–30 Hitzetagen sind das ≈ 20–30 € pro Sommer.
- **Mit Garten oder Kleingarten** lässt sich nahezu alles nutzen, dann tendieren die Nettokosten gegen null.
- **Duschen und Waschmaschine** vermeide ich. Ein Vorwärmspeicher für Duschwasser wäre eine eigene, hygienisch aufwendige Installation.

**Recht (keine Rechtsberatung):**
- Mit dem Vermieter abstimmen. Es darf keine Installation verändert werden, Anschluss nur an vorhandenen Hähnen.
- Der Verbrauch läuft über den Wasserzähler.
- Bei Trockenheit verhängen Kommunen teils Einschränkungen oder Nutzungsverbote (Allgemeinverfügungen). Kühlung mit Trinkwasser ist dann nicht vertretbar.
- Die AVBWasserV verlangt einen Anschluss nach den anerkannten Regeln der Technik, also Rückflusssicherung.

## 7. Speicher oder Dauerdurchfluss?

**Dauerdurchfluss mit Gegenstrom ist besser.**
- Das Register sieht immer 15 °C. Ein geschlossener Speicher erwärmt sich dagegen, die Leistung sinkt und die Stagnationsgefahr steigt.
- 100 l Speicher liefern nur ≈ 0,9 kWh.
- Der Speicher gehört an den **Ausgang**, als 30-l-Sammelbehälter zur Weiterverwendung.
- Optional verhindert eine batteriebetriebene Bewässerungsuhr (≈ 30 €) das Vergessen des Abstellens (Betrieb z. B. 9–19 Uhr, Steuerung stromlos).

## 8. Empfindlichkeit (Zulauftemperatur, 30 l/h)

| Leitungswasser | Kühlleistung | Austritt | Liter pro kWh |
|---|---|---|---|
| 12 °C | ≈ 370 W (mehr Kondensat) | ≈ 22,6 °C | ≈ 81 |
| **15 °C** | **≈ 280 W** | **≈ 23,1 °C** | **≈ 107** |
| 20 °C | ≈ 130 W (kaum Kondensat) | ≈ 23,6 °C | ≈ 236 |

**Bei ≥ 20 °C lohnt das Gerät praktisch nicht mehr.** Wenn warmes Kaltwasser aus Steigleitung oder Schacht kommt (Zirkulationsleitung nebenan), liefert das Gerät kaum noch Kälte.

## 9. Ergebnis

| Maßnahme | Raumspitze |
|---|---|
| Nur Nachtlüftung (Basis) | ≈ 30 °C |
| **+ Kühlregister (2,8 kWh in 10 h)** | **≈ 27 °C** |
| + Hitzeschutzfolie (Sonnenlast −150 W, Mittellast ≈ 300 W) | **≈ 26 °C** |

Rechnung ohne Folie: Wärmeeintrag 4,5 − 2,8 = 1,7 kWh, das sind +1,7 K auf 25,5 °C, also ≈ 27 °C.

## 10. Stückliste (ca.-Preise)

| Teil | € |
|---|---|
| 2 × Kfz-Heizungswärmetauscher Kupfer/Messing, neu | 70 |
| 2 × PC-Lüfter 120 mm, 12 V, ≈ 1,5 W | 16 |
| 12-V-Netzteil 1 A | 8 |
| Multiplex 9 mm (≈ 0,5 m²), Dichtband, Schrauben, Winkel | 25 |
| Tropfwanne + 2 m Schlauch | 14 |
| Anschlussgruppe: Doppel-Eckventil + Geräteventil mit Rückflussverhinderer | 22 |
| Aquastop-Zulaufschlauch 3/4″, 2 m | 18 |
| Regulierventil, Tüllen, Schellen | 25 |
| 3 m Wasserschlauch 1/2″ (Register-Verbindungen, Auslauf) | 12 |
| Entleerungshahn + Handentlüfter | 10 |
| Sammelbehälter 30 l + Überlaufschlauch | 15 |
| 2 × Wassermelder | 20 |
| Isolierschlauch 2 m | 6 |
| **Summe** | **≈ 260** |

Optional: Bewässerungsuhr ≈ 30 €, Thermometer/Hygrometer ≈ 10 €, 10-W-Solarmodul ≈ 20 €.

## 11. Bauanleitung

1. **Gehäuse:** Multiplex zu einem Kasten ≈ 30 × 30 × 40 cm zuschneiden und verschrauben. Zwei Register hintereinander dicht einsetzen. Mit Schaumstoffband abdichten, damit keine Luft am Register vorbeiströmt.
2. **Lüfter:** Die Lüfter auf der Austrittsseite einbauen, sodass sie durch die Register saugen. Netzteil anschließen.
3. **Wasserführung:** Register B unten anschließen (Zulauf) und oben verlassen. Dann zu Register A unten hinein und oben hinaus zum Auslauf. Am tiefsten Punkt den Entleerungshahn setzen, am höchsten den Handentlüfter.
4. **Wanne:** Die Tropfwanne mit 2 % Gefälle unter die Register legen. Den Schlauch in den Sammelbehälter führen.
5. **Aufstellung:** Das Gerät erhöht aufstellen (Regal), damit die kalte Luft in den Raum fällt.
6. **Anschluss:** Am Wandhahn nacheinander Geräteventil mit Rückflussverhinderer, Aquastop-Schlauch und Regulierventil montieren. Schlauch isolieren.
7. **Auslauf:** Das Ende des Auslaufschlauchs im Sammelbehälter fixieren, ≥ 20 mm über dem Überlauf. Überlaufschlauch zur Badewanne oder zum WC führen. Wassermelder aufstellen.
8. **Dichtheitsprobe:** 30 min bei offenem Hahn beobachten. Dann auf ≈ 30 l/h einstellen. Mit Eimer und Uhr messen, Ziel: Austritt ≈ 22–24 °C.
9. **Betrieb:** Vor dem Start ≈ 5 l ablaufen lassen. Abends Hahn schließen, Register entleeren. Wanne und Behälter wöchentlich mit Essigreiniger säubern.

## 12. Grenzen, ehrlich

- **Wasser als Kälteträger ist dünn:** ≈ 107 l pro kWh. Für dauerhafte Volllast wäre ein Klimagerät um den Faktor ≈ 4 günstiger.
- **Die 280 W sind eine Schätzung (±30 %).** Das UA des Registers kenne ich nicht genau. Nach dem Bau Durchfluss und Austrittstemperatur messen und nachregeln.
- **Zulauf ≥ 20 °C:** Das Gerät bringt kaum noch etwas, siehe Tabelle 8.
- **Stromlos:** Nur mit sperrigem Heizkörper-Aufbau (Notlösung) oder mit Solarmodul am Lüfter.
- **Draußen bringt nichts Besseres:** Der Balkon hilft höchstens dem Nachthimmel-Strahler (≈ 0,9 kWh pro klarer Nacht). Gegenüber dem Innenaufbau lohnt das hier nicht.

```json
{
  "knoten": {
    "Wohnung": {"T_C": 27, "rolle": "umgebung"},
    "Kuehlregister": {"T_C": 19, "rolle": "komponente"},
    "Leitungswasser": {"T_C": 15, "rolle": "umgebung"},
    "Strom": {"T_C": 20, "rolle": "umgebung"}
  },
  "stroeme": [
    {"von": "Wohnung", "nach": "Kuehlregister", "W": 280, "art": "waerme"},
    {"von": "Strom", "nach": "Kuehlregister", "W": 3, "art": "arbeit"},
    {"von": "Kuehlregister", "nach": "Leitungswasser", "W": 283, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Wohnung", "T_ein_C": 30, "T_aus_C": 27, "kuehlleistung_W": 280},
  "luft_T_C": 30,
  "wasserverlust_l_pro_tag": 0
}
```

Die Bilanz gilt für die Betriebszeit von 10 h, der Tagesverbrauch an Leitungswasser beträgt dabei ≈ 300 l. Die 280 W enthalten ≈ 60 W latente Kondensationswärme. Es wird nichts in die Luft verdunstet, im Gegenteil fällt ≈ 1 l Kondensat an.