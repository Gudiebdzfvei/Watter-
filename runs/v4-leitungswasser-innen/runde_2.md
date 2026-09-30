# Zimmerkühlung mit Leitungswasser: großes Lamellenregister, Lüfter, Durchlauf

## 1. Kurzfazit

- **Es geht komplett drinnen.** Ein Wasser-Luft-Register (Lüftungs-Heizregister, Kupfer/Alu, ca. 500 × 300 mm) wird von vier PC-Lüftern (≈ 4 W) durchströmt. Das Wasser läuft im Gegenstrom durch und danach in einen offenen Sammelbehälter.
- **Leistung, sensibel gerechnet:** ≈ **280 W** bei 27 °C Raumluft und 15 °C Wasser, netto nach Lüfterwärme ≈ 277 W. Plausible Bandbreite 215–340 W. **Latente Kühlung setze ich nicht an**: Bei 27 °C / 50 % r. F. kondensiert es praktisch nicht.
- **Wirkung, stündlich gerechnet** (Start 25,5 °C nach Nachtlüftung, Speichermasse 1 kWh/K):

| Maßnahme | Raumtemperatur 19 Uhr |
|---|---|
| nichts (nur Nachtlüftung) | 30,3 °C |
| nur Gerät | 27,9 °C |
| Sonnenschutzfolie + Gerät | 26,8 °C |
| Außenverschattung + Gerät | ≈ 25,8 °C |

  Das Gerät senkt die Spitze um etwa **2,4 K**. Das Ziel ≤ 26 °C erreicht man nur zusammen mit Sonnenschutz.
- **Preis der Kälte ist das Wasser:** 35 l/h × 10 h = **350 l/Tag** ≈ 1,58 € brutto, nach Weiterverwendung ≈ 1 € netto. Das sind ≈ 0,6 € pro kWh Kälte, etwa das Fünf- bis Sechsfache eines Klimageräts (≈ 0,10–0,20 €/kWh). Das lohnt nur an einigen Hitzetagen, bei sinnvoller Wasserweiterverwendung oder wenn Stromgeräte nicht infrage kommen.
- **Zulauftemperatur ist die Hauptunsicherheit:** Bei 18 °C statt 15 °C sinkt die Leistung auf ≈ 210 W, bei 20 °C auf ≈ 160 W.

## 2. Physik: Wie viel Kälte steckt im Liter?

Wasser nimmt **1,163 Wh/(l·K)** auf. Die Obergrenze der Leistung setzt das Wasser, nicht die Luft:

Q_max = C_W · (T_Raum − T_Wasser) = 40,7 W/K × 12 K = **488 W** bei 35 l/h.

Ein Register mit Wirkungsgrad ε ≈ 0,57 holt davon ≈ 280 W. Mehr Wasser hilft kaum, denn das Register wird luftseitig begrenzt:

| Durchfluss | Leistung bei 27 °C (Rechnung) | Wasseraustritt | Liter pro kWh |
|---|---|---|---|
| 25 l/h (Sparstufe) | ≈ 247 W | ≈ 22,7 °C | ≈ 101 |
| **35 l/h (Auslegung)** | **≈ 280 W** | **≈ 21,9 °C** | **≈ 126** |
| 50 l/h | ≈ 300 W | ≈ 20,0 °C | ≈ 167 |

Der Durchfluss muss nicht genau stimmen: ±10 l/h ändert die Leistung nur um ≈ 10 %, den Wasserverbrauch aber um ≈ 30 %.

## 3. Wärmelast (Auslegungsfall)

Zimmer 20 m² × 2,5 m = 50 m³, mittleres Geschoss, 2 m² Südwest-Fenster mit Innenvorhang, Außenluft 30 °C (nachts 18–20 °C). Betriebszeit 9–19 Uhr, **nur sensible Last**:

| Quelle | Mittel 9–19 Uhr |
|---|---|
| Sonne durch Fenster (2 m² × ≈ 350 W/m² × g_eff 0,45), Spitze 450 W um 15–17 Uhr | 325 W |
| Hülle und Fugen (G = 12,6 + 5 = 17,6 W/K gegen T_Außen + 1,5 K), hängt von T_Raum ab | ≈ 45 W |
| Person sensibel 60 W + Laptop 40 W + Licht 10 W | 110 W |
| **Summe (≈ 4,8 kWh in 10 h)** | **≈ 480 W** |

- **Latent:** Die Person gibt ≈ 40 W latent ab. Das erhöht die Feuchte, nicht die Lufttemperatur, und steht deshalb nicht in der Temperaturbilanz.
- **Speichermasse:** C = 1,0 kWh/K (mittelschwer) ist eine Annahme. Ich rechne mit 0,5–1,5 kWh/K:
  - 0,5 kWh/K: Dachgeschoss oder Leichtbau.
  - 1,5 kWh/K: Massivbau mit freiliegenden Wänden.

## 4. Raumtemperatur stündlich

**Modell:** C · dT/dt = Sonne + innere Last + G·(T_eq − T) − Q_Gerät(T). Dabei ist T_eq = T_Außen + 1,5 K und Q_Gerät = 23,2 W/K × (T − 15 °C) − 4 W Lüfterwärme. Schrittweite 1 h, Start 25,5 °C. Die Sonnenschutzfolie senkt die Sonnenlast um 40 %.

| Uhr | ohne alles | nur Gerät | Gerät + Folie | Q_Gerät netto |
|---|---|---|---|---|
| 9 | 25,5 | 25,5 | 25,5 | 240 W |
| 11 | 26,1 | 25,6 | 25,5 | 243 W |
| 13 | 27,0 | 26,1 | 25,7 | 253 W |
| 15 | 28,1 | 26,7 | 26,1 | 268 W |
| 16 | 28,7 | 27,1 | 26,3 | 277 W |
| 17 | 29,3 | 27,5 | 26,5 | 285 W |
| 19 | 30,3 | 27,9 | 26,8 | ≈ 291 W |

Das Gerät führt an diesem Tag ≈ **2,6 kWh** ab. Das sind ≈ 108 W im 24-h-Mittel. Die Leistung steigt mit der Raumtemperatur von 240 auf 290 W. Ein Ansatz mit konstant 280 W wäre zu optimistisch gewesen.

**Empfindlichkeit, Raumtemperatur um 19 Uhr:**

| Fall | C = 0,5 kWh/K | C = 1,0 kWh/K | C = 1,5 kWh/K |
|---|---|---|---|
| ohne alles | 34,4 | 30,3 | 28,8 |
| nur Gerät | 29,6 | 27,9 | 27,2 |
| nur Folie | 32,2 | 29,1 | 27,9 |
| Gerät + Folie | 27,7 | 26,8 | 26,4 |

- Bei Leichtbau ist die Sonne das eigentliche Problem. Dann gehört Außenverschattung an erste Stelle. Mit ihr (−75 % Sonne) kommt der Raum ohne Gerät auf 28,0 °C, mit Gerät auf ≈ 25,8 °C (C = 1,0).
- Die Werte gelten für Zulauf 15 °C. Der Fall 18 °C steht in Abschnitt 6.

## 5. Aufbau

### 5.1 Prinzip

Die Lüfter saugen Raumluft durch ein großes Register mit **niedrigem Druckverlust**. Die Frontfläche beträgt 0,15 m², die Anströmung ≈ 0,25 m/s und der Druckabfall < 1 Pa. Damit schaffen PC-Lüfter realistisch ≈ 130 m³/h. Der Gedanke "zwei dichte Kfz-Kerne in Reihe" ist verworfen.

```text
 Kaltwasser-Eckventil (Wand, eigener Abgang)
   │
 [1] Absperrventil
 [2] Geräteventil mit Rückflussverhinderer EA (DVGW)
 [3] Druckminderer 2–3 bar (nur wenn Netzdruck > 4 bar)
 [4] Durchflussregler 0,6 l/min (≈ 35 l/h)
 [5] Gewebeschlauch PN10 mit Aquastop, isoliert
   │ 15 °C
   ▼  Eintritt unten, auf der Luft-AUSTRITTSSEITE des Registers
 ┌──────────── Multiplex-Gehäuse, Regal/Tisch 1,2–1,5 m hoch ─────────────┐
 │ Raumluft 27 °C    Register 3-reihig        Plenum      4 × 120 mm      │
 │ ───────────────►  500×300, PN16  ───────►  25 cm  ──►  Lüfter (2×2)   │
 │                   Wasser im Gegenstrom                   4 W, 12 V  ──►│ Luft ≈ 20,5 °C
 │                   Eintritt 15 °C (Luft-Ausgang) → Austritt ≈ 22 °C     │
 │                   (Luft-Eingang, oben, Entlüfter)                      │
 │ ┌────────── Tropfwanne mit Gefälle, Schlauch zum Behälter ─────────┐   │
 └─┴──────────────────────────────────────────────────────────────────┴───┘
   Ablauf ≈ 22 °C: Kupferrohr/Gewebeschlauch, KEIN Ventil danach
        ▼ freier Auslauf, ≥ 20 mm über Überlauf (Typ AA)
   ┌── Sammelbehälter 60 l, abgedeckt ──┐ Überlauf → Badewanne/WC
   └────────────────────────────────────┘ → Kanne/Eimer: WC, Pflanzen, Putzen
```

Die Anschlussrichtung (Wassereintritt auf der Luftaustrittsseite) muss im Datenblatt des Registers stehen oder nachgefragt werden.

### 5.2 Leistungsrechnung (Annahmen offen)

- **Luft:** V = 130 m³/h (90–170). Mit ρ·cp = 1.177 J/(m³·K) ist C_L = 42,5 W/K.
- **Wasser:** 35 l/h ergeben C_W = 40,7 W/K. Das Verhältnis C_min/C_max liegt bei 0,96.
- **UA:** ≈ 65 W/K (45–90). Eine Kontrollrechnung ergibt luftseitig ≈ 300 W/K (Lamellenteilung 2,5 mm, h ≈ 40 W/(m²K)) und wasserseitig ≈ 150 W/K (laminar). Zusammen mit Kontaktwiderständen sind das ≈ 90 W/K. Ich setze bewusst weniger an.
- **Wirkungsgrad:** NTU = 65/40,7 = 1,6. Der Gegenstrom-Wirkungsgrad liegt bei ≈ 0,62. Wegen der Kreuzstrom-Bauart setze ich × 0,93 an, also **ε ≈ 0,57**.
- **Leistung:** Q = 0,57 × 40,7 × (T − 15) = **23,2 W/K × (T − 15 °C)**. Bei 27 °C sind das 278 W.
- **Bandbreite bei 27 °C / 15 °C:**
  - Pessimistisch (90 m³/h, UA 45): ≈ 215 W.
  - Optimistisch (170 m³/h, UA 90): ≈ 340 W.
- **Messung statt Raten:** Q = 1,163 × Durchfluss [l/h] × (T_aus − T_ein). Die Leistung lässt sich am Wasser messen, ohne Anemometer. Beispiel: 35 × 1,163 × 6,9 K = 281 W.
- **Lüfter:** Vier 120-mm-Lüfter mit ≥ 2 mmH₂O Statikdruck, je ≈ 0,3–0,5 W bei ≈ 1.000 U/min. Ich buche 4 W (Volllast plus Netzteilverlust) und ≈ 25–28 dB(A).
- **Lüfterwärme:** Sie wird nach dem Register in die Luft abgegeben und belastet den Raum wieder. Netto sind es also Q − 4 W.

### 5.3 Kondensation und Entfeuchtung

- **Bei 27 °C / 50 % r. F. tropft nichts.** Der Taupunkt liegt bei 15,7 °C. Die kälteste Stelle des Registers (Luftaustritt, Wassereintritt) hat nicht 15 °C: Die Luft verlässt das Register mit ≈ 20,5 °C, und die Oberfläche liegt wegen des Wasserseiten-Widerstands bei ≈ 17–19 °C. Latent rechne ich mit **0 W**.
- **Wann es doch tropft:**
  - Schwüle Tage (z. B. 28 °C / 60 %, Taupunkt 19,5 °C).
  - Zulauf 12 °C, dann 0–20 W latent.
  - Die Wanne mit Gefälle und Schlauch nimmt das auf (≈ 0–0,3 l/Tag).
- **Entfeuchtung ist kein Vorteil**, sondern nur Zufall bei Schwüle. Die Temperaturbilanz wird dadurch nicht gestützt.

### 5.4 Natürliche Konvektion ohne Strom?

Ja, aber schwächer und unsicher. Das sind Rechnungen, keine Messungen, mit ±40 %:

- **Kühldecke oder Kühlwand** mit 15 °C Wasser tropft und braucht ≥ 18–19 °C. Ich rate ab.
- **Zwei Panel-Heizkörper Typ 22, 600 × 1000 mm**, hoch montiert, in Reihe bei 35 l/h, liefern ≈ 240 W. Die Rechnung nutzt die Nennleistung 1.200 W bei ΔT 50 K und Exponent 1,3: ≈ 140 W für den ersten, ≈ 100 W für den zweiten. Die Oberflächen liegen über dem Taupunkt. Nachteile:
  - je ≈ 30 kg gefüllt, Standgestell nötig (Mietwohnung),
  - Stahl rostet im Frischwasser, das Wasser taugt nur für Pflanzen und WC.
- **Fallschacht:** Register oben in einem 1,2 m hohen Holzschacht (50 × 30 cm). Die Kaltluft sinkt und zieht nach. Die Gleichgewichtsrechnung (Auftrieb ≈ 0,3–0,5 Pa gegen Verluste K ≈ 5) ergibt ≈ 100–160 m³/h. Wegen Einlauf-, Strömungs- und Zugluftverlusten setze ich nur **120–200 W** an. Mit den Lüftern am Schachtfuß läuft er auch mit ausgefallenem Lüfter weiter.
- **Solarmodul statt Netzteil (optional):** Ein 10-W-Modul am Fenster plus 5-€-Abwärtswandler auf 12 V speist die Lüfter. Bei Sonne laufen sie schnell, bei Wolken langsam. Das passt zur Last, aber an Wolkentagen und abends fehlt Luftstrom, während das Wasser weiterläuft. Ich empfehle das Netzteil: 4 W × 10 h = 0,04 kWh ≈ 1,4 ct.

## 6. Empfindlichkeit Zulauftemperatur (35 l/h, ε = 0,57, Raum 27 °C)

| Leitungswasser | Leistung | Austritt | Liter pro kWh | Raumspitze (Gerät + Folie, C = 1) |
|---|---|---|---|---|
| 12 °C | ≈ 348 W (+ 0–20 W latent) | 20,6 °C | 100 | ≈ 26,2 °C |
| **15 °C (Auslegung)** | **278 W** | **21,9 °C** | **126** | **26,8 °C** |
| **18 °C (Realfall im Sommer)** | **209 W** | **23,1 °C** | **167** | **27,4 °C** |
| 20 °C | 162 W | 24,0 °C | 216 | 27,8 °C |

- **Die Zulauftemperatur ist die Hauptunsicherheit.** Steigleitungen und Schächte erwärmen das Wasser im Sommer. Bei 0,6 l/min bleibt es in der Wohnung lange in der Leitung: Bei 10 m Leitung im 26-°C-Raum rechne ich ≈ +1 K.
- **Messen statt annehmen:** Thermometer (Einsteck- oder Anlegethermometer) am Zulauf, Messung **nach 30 min und nach 3 h** Dauerbetrieb.
- **Schwellen:**
  - Zulauf > 18 °C: Das Gerät bringt wenig, ich rechne den Fall 18 °C als Normalfall.
  - Zulauf ≥ 20 °C: Ich betreibe es nicht mehr.

## 7. Sicherer Trinkwasseranschluss

1. **Eigener Abgang:** Kaltwasser-Eckventil oder Waschmaschinenhahn, nie Warmwasser oder Mischbatterie.
2. **Rückflussverhinderer EA** (Geräteventil, DVGW) direkt am Hahn. Das Wasser im Register ist wärmer (DIN EN 1717, Kategorie 2) und darf nicht zurück in die Leitung.
3. **Freier Auslauf (Typ AA):** Der Schlauch endet ≥ 20 mm über dem Überlauf. Es gibt keine geschlossene Verbindung zum Behälter oder zu Abwasser. Dadurch kann nichts zurücksaugen.
4. **Druck:**
   - Register mit **PN 16** (Herstellerangabe), keine Autokühler oder Kfz-Heizungskerne (meist Aluminium mit Kunststoffkästen, nur 1,5–2 bar).
   - Durchflussregler am Eingang.
   - Druckminderer auf 2–3 bar, falls der Netzdruck > 4 bar ist.
   - **Kein Ventil hinter dem Register.** Ein geknickter Ablaufschlauch würde den Netzdruck anlegen. Deshalb Kupferrohr oder druckfester Gewebeschlauch PN10 verwenden, der Schlauch wird fixiert.
5. **Material:** Kupfer/Messing/Al-Lamellen. Die Trinkwasserzulassung (KTW/DVGW) haben Lüftungsregister meist nicht. Deshalb:
   - Bleifreiheit beim Hersteller erfragen.
   - Vor Erstnutzung ≈ 15 min bei hohem Durchfluss in den Abfluss spülen.
   - Das Wasser **nur als Brauchwasser** verwenden, nicht trinken.
6. **Stagnation und Legionellen:**
   - Vor jedem Start ≈ 10 l aufdrehen und für WC oder Pflanzen auffangen.
   - Zulauf messen (Kaltwasser ≤ 25 °C nach DIN 1988-200, ich nehme ≤ 18–20 °C).
   - Abends Hahn zu und Register über den Entleerungshahn leeren.
   - Sammelbehälter abdecken, **täglich leeren und trocknen**, wöchentlich reinigen.
   - Nicht vernebeln und nicht duschen.
7. **Wasserschaden ist das größte Alltagsrisiko:** Aquastop-Schlauch, Wassermelder unter Gerät und Behälter, Überlauf in die Badewanne, Hahn zu bei Abwesenheit, Wanne unter dem Register.

## 8. Wasser, Kosten, Weiterverwendung

**Bilanz Betriebszeit 9–19 Uhr, Normalfall (15 °C):**

| Größe | Wert |
|---|---|
| Durchfluss | 35 l/h → **350 l/Tag** |
| Kälte | ≈ 2,6 kWh/Tag, 24-h-Mittel ≈ 108 W |
| Wasser + Abwasser (4,5 €/m³) | ≈ 1,58 €/Tag |
| Strom | 0,04 kWh ≈ 1,4 ct/Tag |
| Kälte brutto | ≈ 0,6 €/kWh |

- **Sparstufen:**
  - 25 l/h (Regler 0,4 l/min): 250 l/Tag, Raumspitze ≈ +0,3 K.
  - Nur 12–19 Uhr laufen lassen: ≈ 245 l/Tag, Raumspitze ≈ +0,3 K. Die Leistung ist bei höherer Raumtemperatur größer, die späten Stunden sind also die effizientesten.

**Sinnvolle Weiterverwendung (Wasser ≈ 22 °C, Brauchwasser):**

| Verwendung | Liter/Tag |
|---|---|
| WC-Spülung (2 Personen, ≈ 8–10 Spülungen) | 40–60 |
| Pflanzen (Balkon) | 20–30 |
| Putzen, Handwäsche, Geschirr | 20 |
| Körperpflege mit Kanne oder Schöpfkelle (kein Aerosol, Wasser < 12 h, nur kaltes Abwaschen, optional) | bis ≈ 40 |
| **Summe** | **≈ 100–150 l** |

- Netto bleiben **≈ 200–250 l/Tag ≈ 0,9–1,1 €**. Auf 20–30 Hitzetage sind das ≈ 30–45 € brutto pro Sommer, nach Weiterverwendung ≈ 20–30 €.
- Mit Garten oder Kleingarten lässt sich nahezu alles nutzen. Dann tendiert der Nettoverbrauch gegen null.
- **Duschvorwärmung und Waschmaschine** habe ich geprüft und verworfen. Das Register liegt im Trinkwasserteil. Brauchwasser darf nicht in die Trinkwasserinstallation zurück (DIN EN 1717, Kreuzverbindung). Die Waschmaschine braucht zudem Netzdruck, den ein offener Tank nicht liefert. Die Ersparnis (2 × 50 l/Woche) lohnt den Aufwand nicht.
- **Recht (keine Rechtsberatung):**
  - **Vermieter:** Zustimmung einholen, keine Eingriffe in die Installation, nur vorhandene Hähne nutzen.
  - **Abrechnung:** Der Verbrauch läuft über den Wasserzähler. Abwasser wird meist nach Frischwasser berechnet, das Gießwasser wird also mitbezahlt. Einen Gartenzähler gibt es in der Mietwohnung selten.
  - **Trockenheit:** Kommunen können per Allgemeinverfügung die Nutzung von Trinkwasser für Kühlzwecke einschränken. Dann nicht betreiben.
  - **Anschluss:** AVBWasserV verlangt Anschluss nach den anerkannten Regeln der Technik (Rückflusssicherung).
  - **Versicherung:** Leitungswasserschäden klären (Haftpflicht, Hausrat).

## 9. Speicher oder Dauerdurchfluss?

**Dauerdurchfluss.** Ein Speicher wäre zusätzlich unhygienisch (Stagnation) und braucht eine Pumpe. Ein 200-l-Tank (15 → 25 °C) liefert nur ≈ 2,3 kWh, bei einem Mittel von ≈ 19,5 °C nur ≈ 175 W. Die Effizienz (≈ 100 l/kWh) ist dieselbe wie im Durchlauf. Der Speicher gehört an den **Ausgang** (Sammelbehälter), nicht an den Eingang.

## 10. Stückliste (ca.-Preise)

| Teil | € |
|---|---|
| Wasser-Heizregister für Lüftungskanal, Cu/Al, 3-reihig, ca. 500 × 300 mm, PN 16 | 150 (110–220) |
| 4 × PC-Lüfter 120 mm, 12 V, hoher Statikdruck | 32 |
| Netzteil 12 V/2 A + Spannungsregler-Modul | 12 |
| Multiplex 9 mm (≈ 0,6 m²), Dichtband, Winkel, Schrauben | 35 |
| Tropfwanne + Schlauch | 20 |
| Doppel-Eckventil + Geräteventil mit Rückflussverhinderer | 22 |
| Druckminderer mit Manometer (nur bei Netzdruck > 4 bar) | 30 |
| Durchflussregler 0,5–0,6 l/min (Fallback: Nadelventil + Eimermessung) | 25 |
| Gewebeschlauch PN10, Kupferrohr, Entleerungshahn, Handentlüfter | 45 |
| Rohrisolierung | 8 |
| Sammelbehälter 60 l mit Deckel, Überlaufschlauch | 25 |
| 2 Wassermelder | 20 |
| 2 Thermometer (Zulauf/Ablauf), Hygrometer | 20 |
| Kleinmaterial | 15 |
| **Summe** | **≈ 430–460 (ohne Druckminderer ≈ 430)** |

Optional:
- Mechanischer Wasser-Timer (Federwerk) oder Batterieuhr ≈ 25 €.
- 10-W-Solarmodul ≈ 20 €.
- Ein gebrauchter **Gebläsekonvektor (Fan-Coil)** für 80–150 € ersetzt Register, Lüfter und Gehäuse, braucht aber 10–40 W Lüfterleistung. Das liegt über dem "wenige Watt"-Rahmen.

## 11. Bauanleitung

1. **Gehäuse:** Multiplex zu einem Kasten mit Plenum bauen (innen 500 × 300 × 250 mm). Register vorn einsetzen und mit Schaumstoffband rundum abdichten. Rückwand mit 4 Löchern (Ø ≈ 115 mm, 2 × 2) für die Lüfter.
2. **Lüfter:** Auf der Austrittsseite einbauen, sodass sie durch das Register saugen. Kabel über Spannungsregler (ca. 7–12 V) an das Netzteil. Netzteil spritzwassergeschützt, nicht unter dem Register.
3. **Wasserführung:** Eintritt unten auf der Luftaustrittsseite, Austritt oben auf der Lufteintrittsseite (Datenblatt prüfen). Entleerungshahn am tiefsten Punkt, Entlüfter am höchsten. Nach dem Register **kein** Ventil.
4. **Wanne:** Tropfwanne mit Gefälle unter das Register legen, Schlauch in den Sammelbehälter.
5. **Aufstellen:** 1,2–1,5 m hoch (Regal oder Tisch), Ausblasrichtung in den Raum, frei von Vorhängen.
6. **Anschluss:** Am Wandhahn in dieser Reihenfolge montieren: Geräteventil mit EA, ggf. Druckminderer, Durchflussregler, Aquastop-Gewebeschlauch. Isolieren.
7. **Auslauf:** Ende im Sammelbehälter fixieren, ≥ 20 mm über dem Überlauf. Überlaufschlauch in die Badewanne oder zum WC. Wassermelder aufstellen.
8. **Erstinbetriebnahme:**
   - 15 min spülen (nicht für Pflanzen).
   - Dichtheit bei 30 min Dauerbetrieb prüfen.
   - Mit Eimer und Uhr auf ≈ 35 l/h stellen.
   - Zulauf- und Ablauftemperatur messen. Erwartung: Ablauf ≈ 22 °C bei 27 °C Raumluft.
9. **Betrieb:**
   - Vor dem Start ≈ 10 l ablaufen lassen und auffangen.
   - Zulauf nach 30 min und 3 h prüfen.
   - Abends Hahn zu, Register entleeren, Behälter leeren und trocknen.
   - Wöchentlich Wanne und Behälter mit Essigreiniger säubern.

## 12. Was sich gegenüber dem ersten Entwurf geändert hat

| Schwäche | Korrektur |
|---|---|
| Latent 60 W, Entfeuchtung ≈ 5 %-Punkte | Oberflächentemperatur pro Registerabschnitt bilanziert: trocken bei 27 °C / 50 %. Latent 0 W, kein Entfeuchtungsvorteil angesetzt. |
| Luftstrom 70 m³/h mit zwei dichten Kernen unplausibel | Ein Register mit großer Fläche und < 1 Pa Druckverlust, Volumenstrom 130 m³/h (90–170) als offene Annahme. Leistung am Wasser messbar. |
| 280 W als Zehn-Stunden-Mittel bei 27 °C | Stündliche Rechnung mit T_Raum(t), Q(T) und Bandbreite der Speichermasse. Mittel ≈ 260 W, Spitze 291 W. |
| Latent und sensibel vermischt | Nur sensible Last bilanziert, Person latent nur als Feuchtelast. |
| Lüfterwärme falsch gebucht | Nach dem Register in den Raum zurückgebucht: netto 277 W bei 281 W Wasseraufnahme. |
| Kfz-Kerne: Druck, Material, Zulassung | PN16-Register, Durchflussregler, Druckminderer, kein Ventil nach dem Register, Material- und Spülhinweise. |
| Zulauf 15 °C optimistisch | 18 °C als Realfall mitgerechnet, Messung nach 30 min und 3 h, Hauptunsicherheit benannt. |
| Dosierung, Stagnation, Batterieuhr | Durchflussregler, tägliches Leeren des Behälters, Timer nur optional. |
| Weiterverwendung, Waschmaschine/Dusche | Geprüft und aus Gründen der Kreuzverbindung und des Netzdrucks verworfen. Kannenwäsche als Option. |
| Konvektion und Solarlüfter ungeprüft | Heizkörper und Fallschacht als Rechnung mit ±40 %, Solarmodul-Verhalten bei Wolken benannt. |

## 13. Grenzen, ehrlich

- **Wasser ist ein dünner Kälteträger:** ≈ 126 l/kWh bei 15 °C, ≈ 167 l/kWh bei 18 °C. Die Kälte kostet ≈ 0,6 €/kWh gegenüber ≈ 0,10–0,20 €/kWh beim Klimagerät.
- **Die Rechenwerte UA, Luftstrom und Speichermasse sind Schätzungen.** Die Bandbreite der Leistung ist 215–340 W, die der Raumspitze 26,4–27,7 °C (Gerät + Folie).
- **Allein reicht es nicht für ≤ 26 °C.** Es braucht Nachtlüftung und Sonnenschutz. Der Modellraum (C = 1 kWh/K) erreicht ≈ 26,8 °C mit Folie und ≈ 25,8 °C mit Außenverschattung. Für leichte Dachzimmer bleibt das Ziel unerreichbar.
- **Mehr Leistung kostet überproportional Wasser:** Ein zweites Register gäbe ≈ +60 %, bräuchte aber ≈ 700 l/Tag (≈ 3 €/Tag). Dann ist Wasser nicht mehr sinnvoll.
- **Draußen bringt nichts Besseres:** Der Balkon hilft höchstens dem Nachthimmel-Strahler (≈ 0,9 kWh pro klarer Nacht). Gegenüber dem Innenaufbau lohnt das hier nicht.
- **Bei Trockenheitsverboten oder Zulauf ≥ 20 °C** bleibt das Gerät aus.

## 14. Energiebilanz

Die Bilanz ist eine **Momentaufnahme im Betrieb um 16 Uhr** (Betriebszeit 9–19 Uhr, Auslegungsfall ohne Folie, 15 °C Zulauf, 35 l/h). Die Raumluft liegt bei 27,1 °C (ohne Gerät wären es 28,7 °C), die Kühlleistung beträgt 281 W brutto und 277 W netto. Das 24-h-Mittel ist ≈ 108 W. Der Leitungswasserverbrauch beträgt 350 l/Tag. Es wird nichts in die Luft verdunstet.

```json
{
  "knoten": {
    "Wohnung": {"T_C": 27.1, "rolle": "umgebung"},
    "Kuehlregister": {"T_C": 18.5, "rolle": "komponente"},
    "Luefter": {"T_C": 30, "rolle": "komponente"},
    "Leitungswasser": {"T_C": 15, "rolle": "umgebung"},
    "Strom": {"T_C": 20, "rolle": "umgebung"}
  },
  "stroeme": [
    {"von": "Wohnung", "nach": "Kuehlregister", "W": 281, "art": "waerme"},
    {"von": "Kuehlregister", "nach": "Leitungswasser", "W": 281, "art": "waerme"},
    {"von": "Strom", "nach": "Luefter", "W": 4, "art": "arbeit"},
    {"von": "Luefter", "nach": "Wohnung", "W": 4, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Wohnung", "T_ein_C": 28.7, "T_aus_C": 27.1, "kuehlleistung_W": 277},
  "luft_T_C": 30,
  "wasserverlust_l_pro_tag": 0
}
```