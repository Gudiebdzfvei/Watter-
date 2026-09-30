# Zimmerkühlung mit Leitungswasser: drei Panelheizkörper als stromloser Kühler

## 1. Kurzfazit

**Ansatzwechsel:** Das frühere Lamellenregister mit PC-Lüftern ist verworfen. Mit ehrlichen Zahlen hält es nicht:
- Luftseitig ist h nur ≈ 10–15 W/(m²K), damit UA ≈ 45–60 W/K.
- Ein realistischer Lüfter braucht 6–10 W.
- Es kommt auf ≈ 210–250 W bei 35 l/h, also ≈ 145 l/kWh.

Drei in Reihe geschaltete **Panelheizkörper** liefern im selben Raum ≈ 256 W bei nur 25 l/h (98 l/kWh). Sie brauchen **0 W Strom** und halten Netzdruck aus. Sie sind gebraucht billig, und das Wasser kommt ≈ 24 °C warm heraus.

| Größe | Zulauf 15 °C (Auslegung) | Zulauf 18 °C (Sommer-Realfall, gleichrangig) |
|---|---|---|
| Leistung bei 27 °C Raumluft | **≈ 256 W** (Band 180–330 W) | **≈ 187 W** |
| Mittel 9–19 Uhr (Raum steigt von 25,5 auf 28 °C) | ≈ 243 W | ≈ 182 W |
| Kälte pro Tag (10 h) | 2,4 kWh | 1,8 kWh |
| Wasser | 250 l/Tag, 103 l/kWh | 250 l/Tag, 138 l/kWh |
| Wasserkosten (4,5 €/m³) | 1,13 €/Tag, ≈ 0,46 €/kWh | 1,13 €/Tag, ≈ 0,62 €/kWh |
| Absenkung der Spitze um 19 Uhr | −2,3 K | −1,7 K |
| Spitze mit Gerät (Raum ohne Gerät 30,4 °C) | 28,1 °C | 28,7 °C |
| Spitze mit Gerät und Außenverschattung (ohne Gerät 28,1 °C) | **26,0 °C** | **26,5 °C** |

**Rangfolge der Maßnahmen** (Kosten-Nutzen):
1. **Nachtlüftung:** gratis, sie liefert die Starttemperatur von 25,5 °C.
2. **Außenverschattung** (Markise, Außenjalousie, Hitzeschutzplane): −2,3 K an der Spitze. Das ist so viel wie das Wassergerät.
3. **Wassergerät:** weitere −2,1 bis −2,3 K. Erst das Zusammenspiel erreicht das Ziel ≤ 26 °C.

Die Kälte kostet ≈ 0,46–0,62 €/kWh. Ein Klimagerät liegt bei ≈ 0,12–0,20 €/kWh. Das Wassergerät lohnt sich also nur an einigen Hitzetagen, wenn Strom, Lärm und Abluftschlauch nicht infrage kommen, oder bei guter Weiterverwendung des Wassers.

**Draußen wird nichts gebaut.** Der Nachthimmel-Strahler (≈ 0,9 kWh pro klarer Nacht, ≈ 1.700 €) lohnt hier nicht. Der Balkon dient nur als Ziel für Gießwasser.

## 2. Physik: Was steckt im Liter?

Wasser nimmt 1,163 Wh/(l·K) auf. Der Wasserbedarf hängt nur davon ab, wie warm das Wasser wieder herauskommt:

**Liter pro kWh = 860 / (T_aus − T_ein)**

Bei 15 → 24 °C sind das ≈ 96 l/kWh. Bei 15 → 21 °C sind es 143 l/kWh. Mehr Tauscherfläche spart also Wasser, denn sie lässt das Wasser wärmer austreten. Mehr Durchfluss bringt dagegen kaum noch etwas:

| Aufbau (Raum 27 °C, Zulauf 15 °C) | Leistung | Austritt | l/kWh |
|---|---|---|---|
| 1 Heizkörper, 12 l/h | 111 W | 23,0 °C | 108 |
| 2 Heizkörper, 25 l/h | 214 W | 22,4 °C | 117 |
| 2 Heizkörper, 35 l/h | 245 W | 21,0 °C | 143 |
| **3 Heizkörper, 25 l/h (Auslegung)** | **256 W** | **23,9 °C** | **98** |
| 3 Heizkörper, 35 l/h (Turbo) | 310 W | 22,6 °C | 113 |

Die Obergrenze setzt das Wasser: 25 l/h × 1,163 × 12 K = 349 W. Die zusätzlichen 10 l/h (+40 % Wasser) bringen nur +54 W (+21 %).

## 3. Wärmeübertragung ohne Strom

**Heizkörper im Kühlbetrieb:** Die Normleistung bei ΔT = 50 K wird mit dem Exponenten 1,3 umgerechnet. Typ 22, 600 × 1000 mm hat 1.200 W bei ΔT 49,8 K, das ergibt Q = 7,46 W/K^1,3 · ΔT^1,3.

| ΔT Raum − mittleres Wasser | 4 K | 6 K | 8 K | 10 K | 12 K |
|---|---|---|---|---|---|
| Leistung je Heizkörper | 45 W | 77 W | 111 W | 149 W | 189 W |

- **Reihenrechnung bei 25 l/h, Raum 27 °C, Zulauf 15 °C:** Heizkörper 1 bringt 140 W (Wasser 15 → 19,9 °C), Nr. 2 bringt 74 W (→ 22,4 °C) und Nr. 3 bringt 42 W (→ 23,9 °C). Zusammen sind das 256 W, mit Wasserbilanz 29,1 W/K × 8,9 K = 257 W.
- **Raumtemperaturabhängigkeit:** Q ≈ 256 W + 25,5 W/K × (T_Raum − 27 °C). Bei 25 °C sind es 208 W, bei 29 °C 308 W.
- **Fläche:** Drei Heizkörper haben zusammen 1,8 m² Frontfläche und etwa 10 m² Gesamtfläche mit Konvektionsblechen.
- **Unsicherheit ±30 %:** Der Exponent 1,3 stammt aus dem Heizbetrieb. Bei kaltem Wasser fällt die Luft am Blech nach unten. Das ist physikalisch gleichwertig, aber ungemessen.
- **Strahlungswirkung:** Die kühlen Flächen senken zusätzlich die gefühlte Temperatur, vermutlich um 0,3–0,5 K. Das ist nicht in die Zahlen eingerechnet.
- **Stromlos ist wirklich stromlos:** 0 W.
- **Optional (Schätzung, nicht gemessen):** Ein 140-mm-PC-Lüfter (≈ 1,5 W), der Luft an die Heizkörper bläst, bringt vermutlich +20–40 %. Das würde das Wasser nur wärmer austreten lassen, ohne mehr Liter zu brauchen.

**Variante mit Gebläse** (gebrauchter Gebläsekonvektor, 80–150 €):
- Er leistet etwa 300 W bei 30 l/h, braucht aber 8–12 W Strom und macht Geräusche.
- Pro Liter bringt er nicht mehr als die Heizkörper (≈ 10 W pro l/h bei beiden), ist aber kompakter.
- Er steht als Alternative bei Platzmangel, ohne Wasservorteil.

## 4. Kondensation und Entfeuchtung

Der Taupunkt bei 28 °C / 50 % liegt bei 16,6 °C, bei 28 °C / 65 % bei 20,4 °C. Die Stahlblechoberfläche liegt wegen der guten Wasserseite nur ≈ 0,2 K über der Wassertemperatur. **Der Wassereintritt mit 15 °C ist also wirklich kalt.** Die Oberflächentemperatur je Heizkörper (Mittel):

| Heizkörper | Wasser rein → raus | mittlere Oberfläche |
|---|---|---|
| 1 | 15 → 19,9 °C | ≈ 17,5 °C |
| 2 | 19,9 → 22,4 °C | ≈ 21 °C |
| 3 | 22,4 → 23,9 °C | ≈ 23 °C |

Die latente Leistung rechne ich über Stoffübergang (Lewis-Zahl 1). Je Heizkörper ist der konvektive Leitwert ≈ 10,5 W/K, die latente Leistung ist dann Q_lat ≈ 10,5 · 2.400 K · Δx.

| Fall | nasse Fläche | latent | Kondensat | Wirkung |
|---|---|---|---|---|
| 28 °C / 50 %, Zulauf 15 °C | nur Eintrittsende von Nr. 1 | ≈ 3 W | ≈ 5 g/h, ≈ 50 g/Tag | praktisch trocken, perlt an der Unterkante |
| 28 °C / 50 %, Zulauf 12 °C | Nr. 1 ganz | ≈ 25–30 W | ≈ 40 g/h, ≈ 0,4 l/Tag | sensibel 331 W plus latent |
| 28 °C / 65 % (schwül), Zulauf 15 °C | Nr. 1 ganz, Nr. 2 trocken | ≈ 54 W | ≈ 80 g/h, ≈ 0,8 l/Tag | gesamt ≈ 295 W, davon sensibel ≈ 241 W |

**Ehrliche Einordnung:** Die Gesamtleistung ist vom Wasser begrenzt. Bei Schwüle verschiebt die Kondensation Leistung von sensibel auf latent: 281 W sensibel bei trockener Luft gegen 241 W sensibel plus 54 W latent. Die Lufttemperatur sinkt dadurch nicht stärker. Der Gewinn ist nur Komfort, weil die Luft etwas trockener wird. Für die Temperaturbilanz setze ich ihn nicht an.

**Wohin mit dem Kondensat:**
- Eine flache Kunststoffwanne (z. B. 100 × 30 × 3 cm, ≈ 9 l) unter Heizkörper 1 und 2 reicht.
- Die Zuleitung mit 15 °C beschlägt ohne Dämmung sicher. Sie bekommt 13 mm geschlossenzellige Isolierung, denn die Oberfläche bleibt dann über dem Taupunkt.
- Die Verbindungsschläuche zwischen den Heizkörpern haben ≥ 20 °C und sind unkritisch.

## 5. Wärmelast und Raumtemperatur

**Annahmen** (alle offen, Schätzungen):
- Zimmer 20 m² × 2,5 m, mittleres Geschoss, 2 m² Südwest-Fenster mit Innenvorhang.
- Speichermasse C = 1,0 kWh/K (mittelschwer).
- Hülle und Fugen G = 17,6 W/K gegen T_Außen + 1,5 K.
- Person, Laptop und Licht 110 W.
- Betriebszeit 9–19 Uhr, nur sensible Last. Die Feuchte der Person betrifft nicht die Temperatur.
- Außentemperatur 25 / 26,5 / 28 / 29 / 30 °C (Spitze 13–16 Uhr), danach 29,5 und 28,5 °C.
- Sonne durch das Fenster in W, stündlich ab 9 Uhr: 150, 200, 250, 300, 350, 400, 450, 450, 420, 330. Das ist ein Mittel von 330 W.
- Start 25,5 °C nach Nachtlüftung.
- Sonnenschutzfolie −40 % Sonne, Außenverschattung −75 %.

**Modell:** C · dT/dt = Sonne + 110 W + G · (T_Außen + 1,5 K − T) − Q_Gerät(T), mit 1-h-Schritten (Genauigkeit ±0,1 K).

| Uhr | nichts | nur Folie | nur Außenverschattung | nur Gerät | Folie + Gerät | Außen + Gerät |
|---|---|---|---|---|---|---|
| 9 | 25,5 | 25,5 | 25,5 | 25,5 | 25,5 | 25,5 |
| 11 | 26,1 | 26,0 | 25,9 | 25,7 | 25,6 | 25,4 |
| 13 | 27,0 | 26,7 | 26,4 | 26,2 | 25,8 | 25,5 |
| 15 | 28,2 | 27,5 | 27,0 | 26,8 | 26,2 | 25,7 |
| 17 | 29,4 | 28,4 | 27,6 | 27,6 | 26,7 | 25,9 |
| 19 | **30,4** | 29,1 | 28,1 | **28,1** | 27,0 | **26,0** |

- **Gerät allein:** Es führt 2,43 kWh ab. Die Leistung steigt von 218 W um 9 Uhr über 252 W um 15 Uhr auf 280 W um 18 Uhr, im Mittel 243 W. Im 24-h-Mittel sind das 101 W.
- **Mittlere Raumtemperatur in der Betriebszeit:** 27,7 °C ohne Gerät, 26,6 °C mit Gerät, also im Mittel −1,1 K.
- **Schwere oder leichte Bauweise** (Raumtemperatur um 19 Uhr):

| Speichermasse | nichts | nur Gerät | Absenkung |
|---|---|---|---|
| 0,5 kWh/K (Dachgeschoss, Leichtbau) | 34,6 | 30,0 | −4,6 K |
| 1,0 kWh/K | 30,4 | 28,1 | −2,3 K |
| 1,5 kWh/K (Massivbau) | 28,8 | 27,3 | −1,5 K |

  Im Leichtbau ist die Sonne das eigentliche Problem. Dort kommt Außenverschattung zuerst, und ≤ 26 °C ist mit Gerät allein nicht erreichbar.
- **Laufzeit:** Wer das Gerät erst um 12 Uhr startet, spart 75 l, hat aber um 19 Uhr +0,8 K (28,9 statt 28,1 °C). Der frühe Start bringt also viel und bleibt Normalbetrieb.

**Empfindlichkeit Zulauftemperatur** (3 Heizkörper, 25 l/h, Raum 27 °C):

| Zulauf | Leistung | Austritt | l/kWh | Spitze 19 Uhr, nur Gerät | mit Außenverschattung |
|---|---|---|---|---|---|
| 12 °C | 331 W (+ 25–30 W latent) | 23,4 °C | 76 | ≈ 27,6 °C | ≈ 25,5 °C |
| **15 °C** | **256 W** | **23,9 °C** | **98** | **28,1 °C** | **26,0 °C** |
| **18 °C** | **187 W** | **24,5 °C** | **134** | **28,7 °C** | **26,5 °C** |
| 20 °C | 140 W | 24,9 °C | 178 | ≈ 29,1 °C | ≈ 26,8 °C |

Die Werte für 15 und 18 °C sind simuliert, die für 12 und 20 °C interpoliert.

**Zulauftemperatur als Hauptunsicherheit:**
- Im Sommer erwärmen Steigleitungen das Wasser. Auch in der Wohnung nimmt es in 10 m ungedämmter Leitung bei 25 l/h etwa +1–2 K auf. Deshalb kommt das Gerät direkt an den nächsten Kaltwasserhahn und bekommt gedämmte Zuleitungen.
- Der Dauerfluss von 0,4 l/min hält das Leitungsstück eher frisch (Verweilzeit ≈ 3 min).
- **Messen:** Zulauftemperatur nach 30 min und nach 3 h Betrieb. Ab 18 °C rechne ich mit dem Sommer-Realfall. Ab 20 °C lohnt der Betrieb nicht mehr.
- **Leistung nachmessen:** Q = 1,163 × Durchfluss [l/h] × (T_aus − T_ein). Beispiel: 25 × 1,163 × 8,9 K = 259 W.

## 6. Aufbau

### 6.1 Prinzip

Wasser fließt durch drei in Reihe stehende Panelheizkörper und gibt nach einem freien Auslauf in die Badewanne ab. Die Wanne dient als Puffer. Nichts ist geschlossen, nichts kann zurückfließen.

```text
 Kaltwasser-Eckventil (Wand, eigener Abgang, nie Warmwasser)
   │
 [1] Absperrventil / Doppel-Eckventil
 [2] Geräteventil mit Rückflussverhinderer EA (DVGW)
 [3] Nadelventil (Feindosierung), eingestellt auf 0,4 l/min ≈ 25 l/h
 [4] Aquastop-Gewebeschlauch DN15, Dämmung 13 mm (beschlägt sonst)
   │ 15 °C
   ▼ Anschluss unten
 ┌── HK 1, Typ 22, 600×1000 ──┐      Stand auf Bodenkonsolen,
 │  15 → 19,9 °C   ≈ 140 W    │      10 cm Wandabstand,
 └─────────── oben ───────────┘      Wanne darunter (Kondensat)
   │ Wellschlauch (oben → unten)
   ▼ unten
 ┌── HK 2 ────────────────────┐
 │  19,9 → 22,4 °C ≈ 74 W     │
 └─────────── oben ───────────┘
   │
   ▼ unten
 ┌── HK 3 ────────────────────┐   Entlüfter an jedem Heizkörper oben,
 │  22,4 → 23,9 °C ≈ 42 W     │   Ablasshahn an HK 3 unten
 └─────────── oben ───────────┘
   │ 23,9 °C, Gewebeschlauch PN10, KEIN Ventil danach, fixiert
   ▼ freier Auslauf ≥ 20 mm über Überlaufkante (Typ AA)
 ┌──────── Badewanne (Stopfen zu, ≈ 150 l) ────────┐
 └── Überlauf → Abfluss ──→ Kanne/Eimer: WC, Pflanzen, Putzen ─┘
```

Anschlusslogik:
- **Zulauf:** Der Zulauf geht unten in jeden Heizkörper, der Ablauf oben heraus. Dann sammelt sich keine Luft.
- **Stopfen:** Die zwei nicht genutzten Anschlüsse bekommen Blindstopfen.
- **Stand:** Jeder Heizkörper wiegt gefüllt ≈ 30–35 kg. Zusammen sind das ≈ 100 kg auf Bodenkonsolen, keine Wandmontage. Das ist mietwohnungsfreundlich.
- **Kippsicherung:** Gurt an einem festen Punkt, Heizkörper nicht an Kinder.

### 6.2 Ausbaustufen

| Stufe | Inhalt | Leistung (15 °C, 27 °C) | Wasser | Kosten | Spitze |
|---|---|---|---|---|---|
| **Einstieg** | 1 gebrauchter Heizkörper, 12 l/h | ≈ 110 W | 120 l/Tag | ≈ 200 € | ≈ −1,0 K |
| **Basis** | 2 gebrauchte Heizkörper, 25 l/h | ≈ 214 W | 250 l/Tag | ≈ 310 € | ≈ −1,9 K |
| **Voll (Auslegung)** | 3 gebrauchte Heizkörper, 25 l/h | ≈ 256 W | 250 l/Tag | ≈ 420 € | −2,3 K |
| Turbo an heißen Tagen | 3 Heizkörper, 35 l/h | ≈ 310 W | 350 l/Tag | wie Voll | ≈ −2,8 K |

Die Stufen Einstieg und Basis sind aus der Reihenrechnung und der Faustregel von ≈ 0,95 K pro abgeführter kWh abgeleitet.

## 7. Sicherer Trinkwasseranschluss

1. **Eigener Abgang** am Kaltwasser-Eckventil oder Waschmaschinenhahn. Nie Warmwasser oder Mischbatterie.
2. **Rückflussverhinderer EA** (Geräteventil, DVGW) direkt am Hahn. Er sichert nach DIN EN 1717 gegen Rückfließen aus Flüssigkeitskategorie 2 (erwärmtes, stehendes Wasser).
3. **Freier Auslauf Typ AA:** Der Schlauch endet ≥ 20 mm über der Überlaufkante der Wanne. Es gibt keine geschlossene Verbindung zum Abwasser.
4. **Druck:**
   - Panelheizkörper sind für mehrere bar ausgelegt (Betriebsdruck meist 10 bar), Wellschläuche für PN 10.
   - Das Nadelventil sitzt vor den Heizkörpern. Im Normalbetrieb liegt hinter ihm nur etwa Umgebungsdruck.
   - **Kein Ventil hinter dem letzten Heizkörper.** Ein geknickter Ablaufschlauch würde den vollen Netzdruck anlegen. Deshalb Schlauch PN10 und fixieren.
   - Ein Druckminderer ist nur nötig bei Netzdruck > 6 bar.
5. **Material:** Heizkörper sind nicht trinkwasserzugelassen. Verwendung **nur als Brauchwasser**, nicht trinken, kein Duschen, kein Vernebeln. Neue Heizkörper haben Herstellungsöl und Schmutz. Vor der Erstnutzung ≈ 15 min bei hohem Durchfluss in den Abfluss spülen. Gebrauchte Heizkörper sind von innen oft verschlammt, darum kräftig durchspülen.
6. **Rost:** Stahl im Frischwasser rostet. Anfangs kann das Wasser bräunlich sein und die Wanne anfärben. Vorsicht bei hellem Email.
7. **Stagnation und Legionellen:**
   - Das Wasser bleibt unter 25 °C und wird nicht versprüht.
   - Abends Hahn zu und Heizkörper über den Ablasshahn entleeren.
   - Morgens erste ≈ 10 l in die Wanne laufen lassen, dann erst den Durchfluss einstellen.
   - Wannenwasser täglich verbrauchen oder ablassen.
8. **Leckageschutz:** Viele Häuser haben ein Wasserstopp-/Leckagesystem, das bei Dauerverbrauch die ganze Wohnung absperren kann. Vorher prüfen, ob 0,4 l/min über 10 h dort zulässig sind.
9. **Wasserschaden ist das größte Alltagsrisiko:**
   - Aquastop-Schlauch,
   - Wassermelder unter Heizkörper und am Wannenrand,
   - Hahn zu bei Abwesenheit.

## 8. Wasser, Kosten, Weiterverwendung

**Bilanz (Betriebszeit 9–19 Uhr, Auslegung):**

| Größe | Wert |
|---|---|
| Durchfluss | 25 l/h → **250 l/Tag** |
| Kälte | 2,43 kWh/Tag, 24-h-Mittel ≈ 101 W, Betriebsmittel 243 W |
| Wasser + Abwasser (4,5 €/m³) | 1,13 €/Tag |
| Strom | 0 W |
| Kälte brutto | ≈ 0,46 €/kWh (bei 18 °C Zulauf ≈ 0,62 €/kWh) |
| 20–30 Hitzetage | ≈ 23–34 € brutto |

**Wassermanagement ehrlich gerechnet:** Die Wanne (≈ 150 l) fasst nicht alles. Der Rest läuft über den Überlauf ab. Von Hand abholbar und sinnvoll ersetzbar sind nur etwa 100 l pro Tag:

| Verwendung | Liter/Tag |
|---|---|
| WC-Spülung mit Eimer (2 Personen, 8–10 Spülungen à 5 l) | 40–60 |
| Pflanzen (Balkon, Zimmer) | 20–30 |
| Putzen, Handwäsche, Geschirr | 15–20 |
| **Summe** | **≈ 90–110** |

- Netto bleiben ≈ 150 l als Verlust, also etwa 0,7 €/Tag.
- Wer das Wasser nicht holt, zahlt die vollen 1,13 €/Tag.
- Ein Kübel oder eine Regentonne (120–200 l, ≈ 30–50 €) mit Überlaufschlauch zur Wanne ersetzt die Wanne, wenn diese gebraucht wird.
- Der Wannenstopfen bleibt tagsüber zu, die Wanne ist dann nicht nutzbar.
- Das Wasser geht **nicht** zurück in Dusche oder Waschmaschine: Kreuzverbindungsverbot, und es fehlt der Netzdruck.

**Recht (keine Rechtsberatung):**
- **Vermieter:** Zustimmung einholen. Es werden nur vorhandene Hähne genutzt und nichts an der Installation verändert. Gewicht und Wasserschaden vorher klären (Haftpflicht, Hausrat).
- **Abrechnung:** Der Verbrauch läuft über den Wohnungswasserzähler, das Abwasser meist nach Frischwassermenge. Gießwasser wird also mitbezahlt.
- **Trockenheit:** Kommunen können per Allgemeinverfügung Trinkwasser für Kühlzwecke untersagen. Dann nicht betreiben.
- **Anschluss:** AVBWasserV verlangt Anschluss nach den anerkannten Regeln der Technik (Rückflusssicherung, siehe Abschnitt 7).

## 9. Speicher oder Dauerdurchfluss?

**Dauerdurchfluss mit Pufferwanne am Ausgang.** Ein Speicher am Eingang wäre unhygienisch (Stagnation) und bräuchte eine Pumpe. Ein 200-l-Tank (15 → 25 °C) liefert nur ≈ 2,3 kWh, im Mittel bei ≈ 19,5 °C also nur ≈ 175 W. Die Wassereffizienz wäre dieselbe (≈ 100 l/kWh) und der Aufwand größer.

## 10. Stückliste (ca.-Preise, Voll-Ausbau)

| Teil | € |
|---|---|
| 3 × Panelheizkörper Typ 22, 600 × 1000, gebraucht (neu 100–140 je) | 150 |
| 3 × Bodenkonsolen/Standfüße | 75 |
| 4 × Edelstahl-Wellschlauch DN15 mit EPDM-Kern | 40 |
| Geräteventil mit Rückflussverhinderer EA | 15 |
| Doppel-Eckventil/T-Stück | 15 |
| Nadelventil (Feindosierung) | 20 |
| Aquastop-Gewebeschlauch | 12 |
| Rohrisolierung 13 mm | 8 |
| Blindstopfen, 3 Entlüfter, Ablasshahn, Dichtungen | 15 |
| 2 Auffangwannen (Kondensat) | 20 |
| 2 Wassermelder | 20 |
| 2 Thermometer (Zu-/Ablauf), Hygrometer | 20 |
| Ablaufschlauch PN10 mit Halter | 10 |
| **Summe** | **≈ 420** |

- Mit neuen Heizkörpern ≈ +200–300 €.
- Basis (2 Heizkörper) ≈ 310 €, Einstieg (1 Heizkörper) ≈ 200 €.
- Druckminderer (30 €) nur bei Netzdruck > 6 bar.
- Optional Bewässerungsuhr mit Batterie (≈ 25 €) als Zeitschaltung. Sie kommt nach dem EA und ist nicht trinkwasserzugelassen.

## 11. Bauanleitung

1. **Standort:** Innenwand, nicht im direkten Sonnenschein, 10 cm Wandabstand, nicht neben dem Sitzplatz wegen Kaltluftabfall. Nah am Kaltwasserhahn (kurze Zuleitung).
2. **Heizkörper vorbereiten:** 15 min mit Netzdruck durchspülen (in die Wanne oder den Abfluss), Schlamm ausspülen. Blindstopfen und Entlüfter einsetzen, Anschlüsse unten (Zulauf) und oben (Ablauf) wählen.
3. **Aufstellen:** Auf Bodenkonsolen, Kippsicherung, Wanne unter HK 1 und HK 2.
4. **Verschlauchen:** Wellschläuche von oben HK 1 nach unten HK 2, von oben HK 2 nach unten HK 3. Zulaufseite und Ablaufseite klar unterscheiden.
5. **Wasserseite am Hahn:** In dieser Reihenfolge: Eckventil → Geräteventil mit EA → Nadelventil → Aquastop-Schlauch. Alles isolieren.
6. **Ablauf:** Schlauch an HK 3 oben, **ohne Ventil**, fixiert über der Wanne, ≥ 20 mm über der Überlaufkante. Wassermelder aufstellen.
7. **Dichtheit:** 30 min Dauerbetrieb, Verschraubungen prüfen.
8. **Dosieren:** Mit Eimer und Uhr auf ≈ 25 l/h (0,4 l/min) stellen. Regelgröße: **Ablauftemperatur 23–24 °C**. Liegt sie über 25 °C, mehr Wasser, liegt sie unter 22 °C, weniger. Der Durchfluss schwankt mit dem Netzdruck (etwa ±30 %), deshalb morgens kurz nachmessen.
9. **Betrieb:**
   - Morgens ≈ 10 l ablaufen lassen und für WC/Pflanzen auffangen.
   - Zulauf nach 30 min und 3 h prüfen.
   - Abends Hahn zu, Heizkörper entleeren, Wanne leeren und trocknen.
   - Wöchentlich Wanne und Wannen mit Essigreiniger säubern.

## 12. Was gegenüber der Vorversion geändert wurde

| Kritik | Antwort |
|---|---|
| Luftseitiges h geschönt, UA zu hoch | Register mit PC-Lüftern verworfen. Nachgerechnet liegt UA bei ≈ 45–60 W/K, damit ≈ 210–250 W bei 35 l/h plus 6–10 W Strom. |
| Luftstrom und Lüfterleistung optimistisch | Stromlose Hauptlösung, 0 W. Die optionalen 1,5 W und der Gebläsekonvektor mit 8–12 W sind offen benannt. |
| Stromlose Variante abgetan | Sie ist jetzt die Hauptlösung mit Reihenrechnung, Stückliste und Bauanleitung. |
| Kondensation zu knapp | Oberfläche je Heizkörper gerechnet, drei Fälle mit Kondensat und latenter Leistung, Zero-Sum-Erklärung. |
| Wassermanagement passt nicht | Wanne als Puffer, Überlauf ehrlich als Verlust, nur ≈ 100 l/Tag abholbar. |
| Kosten-Nutzen schwach | Rangfolge Nachtlüftung, Außenverschattung, dann Gerät. Einstieg ab ≈ 200 €. |
| 15 °C optimistisch | 15 und 18 °C gleichrangig in Tabellen. Messung nach 30 min und 3 h. |
| JSON Momentaufnahme | Bilanz jetzt als Mittel der Betriebszeit. |

## 13. Grenzen, ehrlich

- **Wasser ist ein dünner Kälteträger.** 98 l/kWh bei 15 °C, 134 l/kWh bei 18 °C. Das kostet ≈ 0,46–0,62 €/kWh, drei- bis fünfmal so viel wie ein Klimagerät.
- **Die Leistung ist unsicher.** Die Bandbreite ist 180–330 W (Heizkörperexponent, Aufstellung). Speichermasse und Sonnenlast sind Annahmen. Die Raumspitze mit Gerät und Außenverschattung liegt bei 26,0 °C (C = 1,0) und ändert sich mit C und Sonne.
- **Allein reicht es nicht für ≤ 26 °C.** Im Leichtbau (C = 0,5) bleibt es bei ≈ 30 °C ohne Verschattung.
- **Mehr Leistung kostet überproportional Wasser:** +21 % Leistung kosten +40 % Wasser.
- **Das Wasser geht zu ≈ 60 % verloren,** wenn man es nicht holt. Mit Garten oder Kleingarten lässt sich mehr nutzen.
- **Bei Trockenheitsverbot, Zulauf ≥ 20 °C oder Wasserstopp-Anlage im Haus** bleibt das Gerät aus.

## 14. Energiebilanz

Die Bilanz ist das **Mittel der Betriebszeit 9–19 Uhr** im Auslegungsfall ohne Folie mit Zulauf 15 °C und 25 l/h. Die Raumluft liegt ohne Gerät im Mittel bei 27,7 °C und mit Gerät bei 26,6 °C. Die Kühlleistung beträgt 243 W (24-h-Mittel ≈ 101 W). Das Wasser tritt im Mittel mit ≈ 23,4 °C aus, die mittlere Wassertemperatur in den Heizkörpern ist 19,2 °C. Der Leitungswasserverbrauch beträgt 250 l/Tag, in die Luft verdunstet nichts.

```json
{
  "knoten": {
    "Wohnung": {"T_C": 26.6, "rolle": "umgebung"},
    "Heizkoerper": {"T_C": 19.2, "rolle": "komponente"},
    "Leitungswasser": {"T_C": 15, "rolle": "umgebung"}
  },
  "stroeme": [
    {"von": "Wohnung", "nach": "Heizkoerper", "W": 243, "art": "waerme"},
    {"von": "Heizkoerper", "nach": "Leitungswasser", "W": 243, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Wohnung", "T_ein_C": 27.7, "T_aus_C": 26.6, "kuehlleistung_W": 243},
  "luft_T_C": 30,
  "wasserverlust_l_pro_tag": 0
}
```