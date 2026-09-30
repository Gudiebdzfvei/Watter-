# Wasserleitung kühlen im geschlossenen Wasserkreislauf: solar getriebener Zeolith-Adsorptionskühler ohne Strom (Runde 3)

## 1. Kurzfassung

**Der reine Verdunster-Kondensator-Loop kühlt nicht.** Dampf strömt nur zum niedrigeren Druck, also zur kälteren Stelle. Der Kondensator müsste kälter sein als die Leitung, und Umgebungsluft mit 32 °C und 40 % r. F. hat eine Feuchtkugeltemperatur von nur etwa 22 °C. Ein offener nasser Lappen bringt 24 °C-Wasser also höchstens auf 22–23 °C und verliert dabei Wasser. Der Ansatz bleibt deshalb gewechselt: Sorption statt Verdunstung. Er wird gegenüber Runde 2 in mehreren Punkten neu aufgebaut.

**Das Prinzip ist eine solar getriebene Wärmepumpe mit drei Temperaturen. Arbeitsmittel ist ausschließlich Wasser, Sorbens ist Zeolith (Silikagel als Rückfallebene):**

- **Nachts (Kälte):** Wasser verdampft bei etwa 4–10 °C und 0,8–1,2 kPa an Rohren im kalten Bad. Der Zeolith bindet den Dampf, er kondensiert also nicht am Verdampfer. Die Bindungswärme geht an die Nachtluft.
- **Tags (Regeneration):** Die Sonne heizt das Zeolithbett im Kollektor auf 95 °C oder mehr und treibt den Dampf aus. Der Dampf kondensiert im Rippenrohr-Kondensator bei etwa 41 °C und gibt die Wärme an die Tagluft (32 °C) ab. Das Kondensat läuft per Schwerkraft durch einen zweistufigen Siphon zurück zum Verdampfer.
- **Strom: 0 W. Wasserverlust: 0 L.** Der Antrieb besteht aus Sonnenwärme, Tag/Nacht-Wechsel, Schwerkraft, Kamineffekt und Wachs-Dehnstoffelementen.

**Wo bleibt die Kondensationswärme?**
- **Tagsüber** am Kondensator bei 41 °C: Sie fließt von selbst in die 32 °C warme Luft.
- **Nachts** beim Adsorber, der Bindungswärme, Sonnenwärme und die aufgenommene Kälte an die Nachtluft abgibt.
- **Warum die Leitung trotzdem kalt bleibt:** Verdampfen (etwa 6 °C) und Kondensieren (etwa 41 °C) laufen auf zwei Temperaturniveaus und zu verschiedenen Zeiten ab. Das Zeolithbett puffert den Dampf dazwischen. Die Sonnenwärme hebt die Wärme von 6 °C auf 41 °C, so wie ein Kompressor es täte. Ohne Sonne gäbe es keine Kühlung.

**Ergebnis Auslegungsfall (Klartag 32 °C, Wind 3 m/s, Nacht 29 → 20 °C, konservativ):**

| | Balkon | Fassade (4 Module) |
|---|---|---|
| Kollektorfläche (Apertur) | 2,7 m² | 10,8 m² |
| Zeolith | 40 kg | 160 kg |
| Nutzkälte netto (Tagesmittel) | 0,99 kWh/Tag (41 W) | 3,96 kWh/Tag (165 W) |
| Menge bei 24 → 11 °C | **≈ 65 L/Tag** (Band 38–100) | **≈ 260 L/Tag** (oder ≈ 220 L bei 8,5 °C) |
| Auslauftemperatur | 8–13 °C, Mittel ≈ 11 °C | ≈ Badtemperatur, 8–12 °C |
| Momentane Kühlleistung beim Zapfen (3 L/min) | ca. 2–3 kW aus dem Speicher | ca. 2–3 kW |
| Strom / Wasserverlust | 0 W / 0 L | 0 W / 0 L |
| Dunst | ≈ 18 L/Tag | ≈ 70 L/Tag |
| Bedeckt | 0 (nur Speicher) | 0 |

**Ehrlichkeitsvorbehalt:** Das Ergebnis hängt an der Zeolith-Isotherme. Ich habe sie aus veröffentlichten Kennlinien von AQSOA-Z02- bzw. SAPO-34-Typen abgeschätzt und um etwa 40–50 % gekürzt. Sie muss mit der Herstellerisotherme oder einer eigenen Messung belegt werden. Der Fallback mit Silikagel liefert nur etwa 35 L/Tag (Abschnitt 6).

---

## 2. Energiepfad

```
 TAG (Sonne, Kollektor 25 -> 95 C bis ca. 13 Uhr)     NACHT (ca. 21 - 08 Uhr)

 Sonne 800 W/m2                                       Verdampfer 4-10 C, ca. 1 kPa
   | Strahlung                                          Wasser verdampft, Waerme aus Bad
   v                                                    | Dampf nur ueber Klappe R2
 Kollektor (Doppelglas, Absorberrohre)                  v
   | Waerme                                           Adsorber (Zeolith), 23-40 C
   v                                                    bindet Dampf
 Zeolithbett: gibt Dampf ab (ab ca. 78 C)               | Bindungswaerme
   | Klappe R1                                          v
   v                                                  Alu-Rippen im Rueckkanal (Lamellen offen)
 Kondensator ca. 41 C --> Tagluft 32 C                  --> Nachtluft 20-27 C
   | Kondensat, Schwerkraft, 2-stufiger Siphon
   v
 Verdampfer (wartet auf die Nacht)
```

**Zweiter Hauptsatz:** Für das dreistufige System gilt COP_Carnot = T_e/(T_m−T_e) · (T_h−T_m)/T_h. Mit T_e = 279 K (6 °C), T_m = 308 K (35 °C) und T_h = 368 K (95 °C) ergibt das 279/29 · 60/368 ≈ 1,57. Erreicht werden COP_th = 0,34, also etwa 22 % von Carnot. Für eine einbettige Anlage ohne Wärmerückgewinnung ist das plausibel.

**Isolation der Verdampferseite:** Ohne Klappe würde das heiße Bett tags in den kalten Verdampfer desorbieren. Deshalb sitzt dort die passive Dampfdiode R2.

---

## 3. Aufbau Balkon

Maße: Grundfläche 1 × 3 m, Höhe 2,5 m. Der Kollektor sitzt außen an der Brüstung, geneigt 40°, nach Süd ±30°. Der Tank steht darunter.

```
  Sued (links)                                               Wand (rechts)
     Sonne \ \                    Abluft-Kamin (bis 2,5 m)
            \ \        ______________|_______
             \ \     / Doppelglas 40 Grad  ^ \       Kondensator (12 m2 Rippen)
   Bruestung  \ \  /  Absorberblech,        |  \      eigener Schattenkamin
      |        \ /   20 Rohre + Zeolith     |   \        | Kondensat
      |   Zuluft-Lamellen (Regenschutz +    |    |       v
      |   Insektengitter, Rueckkanal)       |    |    2-stufiger Siphon
      |        R2 ---- Dampfweg --- R1 -----+    |
      |    +---------------------------+         |
      |    | Bad 160 L  (Tank 0,45x0,36x1,35 m)   |
      |    | 6 Verdampferrohre + Wendel 32 m     150 mm Daemmung
      |    +---------------------------+
   Trinkwasser: 24 C oben rein, kalt unten raus (Gegenstrom)
```

### 3.1 Bauteile

**Adsorber (Rohrbündel):**
- 20 Rohre Edelstahl 1.4404, 48,3 × 0,8 mm, 2,8 m lang, mit je 2 kg Zeolith (Schüttdichte 0,5–0,6 kg/L).
- Innen liegt ein zentrales Dampfrohr aus Streckmetall (Ø 12 mm), dazu vier radiale Kupfer-Rippen (0,3 mm, 23 mm hoch). Der Wärmeweg im Bett beträgt höchstens 10 mm, das ergibt ΔT ≈ 3 K bei 40 W je Rohr.
- **Dampfdurchgang (Kozeny-Carman):** Eine axiale Durchströmung des Betts würde bei der Spitze von 1 L/s je Rohr rund 1 kPa Druckverlust erzeugen, das wäre der ganze Verdampferdruck. Durch das Zentralrohr bleiben radial 0,25 Pa und axial etwa 26 Pa, das sind 0,4 K.
- **Vakuumfestigkeit:** Für Rundrohre gilt p_krit ≈ 2E/(1−ν²)·(t/D)³ ≈ 2 MPa gegenüber 0,1 MPa Außendruck. Das ergibt Sicherheit über 6, auch mit einem Abminderungsfaktor von 0,3.
- Alu liegt nur außerhalb des Vakuums (Absorberblech, Rippen), es gibt also keine Wasserstoffbildung.

**Kollektorkasten:**
- Doppelverglasung mit selektivem Absorber (η₀ = 0,72). Für die Rechnung gilt a₁ = 3,6 W/m²K bei 3 m/s Wind (3,0 ohne Wind), a₂ = 0,012 W/m²K².
- Der Glaskasten ist dicht und trocken (Trockenmittelbeutel). Er wird **nie geöffnet**, sodass keine Feuchte oder Insekten an die Beschichtung kommen.

**Rückkanal für die Nachtkühlung:**
- Hinter den Absorberrohren liegt ein getrennter Luftkanal mit etwa 22 m² Alu-Rippen (0,4 mm, 12 kg) auf den Rohren. Er ist regengeschützt: Lamellen mit Insektengitter unten, Kaminaufsatz oben, feuchtebeständige Dämmung an der Außenwand und ein Reinigungszugang.
- Tagsüber ruht die Luft im geschlossenen Kanal. Der Rückverlust liegt bei etwa 3 W/K und ist in a₁ enthalten.

**Klappensteuerung ohne Strom (zwei Wachselemente außerhalb des Vakuums, ODER-verknüpft):**
- Element 1 am Deckglas schließt die Lamellen bei mehr als 40 °C und öffnet sie bei weniger als 35 °C.
- Element 2 am Sammler öffnet die Lamellen bei mehr als 105 °C. Das ist der Überhitzungsschutz.

**Dampfdioden:**
- Funktionsnotwendig ist nur R2 (Verdampfer → Adsorber). R1 (Adsorber → Kondensator) ist Komfort. R2 wird als Doppelklappe in Reihe gebaut.
- Bauart: PTFE-Folie 0,1 mm auf geläpptem waagerechtem Edelstahlsitz DN100, Öffnungsdruck etwa 2 Pa (0,03 K). Das Risiko bleibt Filmhaftung und Verschmutzung, es ist die wichtigste Prototypfrage.

**Verdampfer (neu, mit belegten Werten):**
- 6 waagerechte Rohre 88,9 × 1,5 mm, je 1,0 m lang, im Bad, innen mit 1,5 mm Metallfilz ausgekleidet. Das Wasser sammelt sich als flacher Sumpf unten, der Filz verteilt es kapillar (halber Umfang 157 mm, das ist erreichbar).
- Es gibt keinen dicken Wasserfilm und damit keinen Siedeverzug: 1 cm Wasser würden rund 1,5 K bedeuten, ein 1,5-mm-Filz nur etwa 0,2 K.
- Der Engpass liegt außen: natürliche Konvektion im Bad gibt h ≈ 110 W/m²K auf 1,68 m², also UA ≈ 185 W/K. Bei der Spitze von etwa 190 W sind das ≈ 1 K. **Auslegung: T_Verd = T_Bad − 1,5 K.**
- Frostschutz: ein Bimetall-Schnappteller im Vakuum (keine Durchführung, kein Organik-Ausgasen) schließt den Dampfweg, wenn die Rohrwand unter 2 °C fällt (Bad etwa 4 °C). Er öffnet bei 6 °C.

**Bad und Wendel:**
- Bad 160 L netto. Verdrängung: Verdampferrohre 37 L, Wendel 16 L, Siphon und Rest 5 L. Das Innenvolumen beträgt also etwa 218 L (0,45 × 0,36 × 1,35 m).
- Wendel aus Edelstahl-Wellrohr DN20, 32 m (ca. 3 m², U ≈ 130 W/m²K, UA ≈ 400 W/K). Sie hat keine Verbindung zum Vakuumsystem, und das Bad bleibt unter 14 °C.

**Kondensator (neu bemessen):**
- Die Desorption bringt 4,8 MJ in etwa 2,5 h (10:20–12:50), das sind im Mittel 530 W, nicht 260 W wie in Runde 2. Bei 32 °C Luft und ΔT = 8 K braucht der Kondensator UA ≈ 65 W/K.
- Dafür sind 12 m² Alu-Rippen im Schatten mit eigenem Kamin vorgesehen (h ≈ 6 W/m²K). Ergebnis: T_kond ≈ 39–41 °C. In der Hitzewelle (37 °C Luft) sind es 45 °C.

**Zweistufiger Siphon (Schwerkraft, ohne Strom):**
- Zu überbrücken sind bis 48 °C Kondensator (11,2 kPa) minus 0,8 kPa Verdampfer, also 10,4 kPa ≈ 1,06 m Wassersäule.
- Zwei Stufen mit je 0,75 m Schenkel tragen zusammen 1,4 m (13,7 kPa), das ergibt 30 % Reserve. Sie passen in die Tankhöhe, liegen im Bad und haben keine Wärmebrücke.

**Nichtkondensierbare Gase (neu):**
- Es gibt **zwei Gassammler**, je 10 L, in beiden Sackgassen: am fernen Ende der Adsorberrohre (dort sammelt sich nachts das Gas) und am oberen Kondensatorende (tags).
- Anforderung: Gesamt-Leckrate ≤ 5·10⁻⁸ mbar·L/s, realistisch für vollgeschweißten Aufbau mit orbitalgeschweißten Nähten und Helium-Prüfung je Baugruppe.
- Das ergibt in 10 Jahren etwa 1575 Pa·L, also rund 80 Pa je Sammler. Bei Nachevakuieren alle 3 Jahre sind es unter 30 Pa, das sind unter 3 % des Nachtdrucks.
- Wasser wird entgast eingefüllt (Sieden unter Vakuum), der Zeolith bei 250 °C unter Vakuum ausgeheizt.
- Nur wenige Teile sitzen im Vakuum: R2 und R1 (passiv), der Bimetallteller und eine Berstscheibe statt eines Sicherheitsventils (leckfrei).
- Kontrolle: Zwei Thermometer an den Sammlern, ein kalter Bereich zeigt Gas an.

**Sicherheit:**
- Berstscheibe bei 200 kPa abs, Abblaseleitung nach unten. Sie löst praktisch nie aus, weil das System nur etwa 5 kg Wasser enthält und der Zeolith es bindet.
- Stagnation bis etwa 130 °C ist beherrscht. Berührungsschutz und Verbundglas sind vorgesehen.

### 3.2 Massenliste des Adsorbers (Wärmekapazität)

| Bauteil | Masse | c (kJ/kgK) | C (kJ/K) |
|---|---|---|---|
| Zeolith | 40 kg | 0,85 | 34,0 |
| Adsorbat (Mittel) | 4,4 kg | 4,19 | 18,4 |
| 20 Rohre 48,3 × 0,8 | 52,6 kg | 0,50 | 26,3 |
| Cu-Rippen | 14 kg | 0,385 | 5,4 |
| Streckmetall-Dampfrohre | 4 kg | 0,50 | 2,0 |
| Sammler + Dampfleitung | 12 kg | 0,50 | 6,0 |
| Alu-Außenrippen | 12 kg | 0,90 | 10,8 |
| Alu-Absorberblech | 3,6 kg | 0,90 | 3,3 |
| Anteil Glas/Dämmung | – | – | 19 |
| **Summe** | | | **≈ 125 kJ/K (34,7 Wh/K)** |

Das Gesamtgewicht betriebsbereit beträgt etwa 470 kg (Adsorbereinheit 143, Glas und Kasten 83, Verdampfer 19, Bad mit Wasser, Tank und Dämmung 220). Das sind rund 1,5 kN/m² auf 3 m² Grundfläche, die Balkonlast muss geprüft werden.

---

## 4. Rechnung Balkon (Klartag)

### 4.1 Kollektor stundenweise (Wind 3 m/s eingerechnet)

Ansatz: A = 2,7 m², Q = 0,72·G·A − A·[3,6·ΔT + 0,012·ΔT²], C = 34,7 Wh/K, Startwert 25 °C um 07:00. Ab 78 °C (Desorptionsbeginn bei 7,8 kPa) kommt das latente Fenster hinzu, es wirkt wie zusätzliche 91 Wh/K bis 95 °C.

| Zeit | G (W/m²) | Luft | T_Ende | Nutzwärme ans Bett |
|---|---|---|---|---|
| 07–08 | 220 | 22 | 35 | 0,39 kWh |
| 08–09 | 400 | 24 | 52 | 0,58 |
| 09–10 | 570 | 26 | 72 | 0,72 |
| 10–11 | 700 | 28 | 83 (Desorption ab 78 °C) | 0,80 |
| 11–12 | 770 | 30 | 89,5 | 0,85 |
| 12–13 | 790 | 31 | 95 (Ende gegen 12:50) | 0,72 (Rest) |
| **Summe** | | | | **4,06 kWh** |

- Einstrahlung insgesamt: 6,15 kWh/m²d, das sind 16,6 kWh auf 2,7 m². Absorbiert werden 0,72 · 16,6 = 11,96 kWh (498 W im 24-h-Mittel).
- **Überschuss:** Bis etwa 15:30 stehen weitere rund 1 kWh zur Verfügung (T bis 110 °C). Das reicht für höheres Δx bis etwa 0,07. Die Auslegung nutzt das nicht. Es ist Reserve, keine Grundlage der Menge. Ohne Wind (a₁ = 3,0) wird das Ergebnis etwa 8 % besser.

### 4.2 Isotherme und Δx (Bandbreite)

| Zustand | T_Bett | p | p/p_s | x (Auslegung) |
|---|---|---|---|---|
| Ende kühle Nacht | 24–30 °C | 0,8–1,2 kPa | 0,2–0,3 | 0,17–0,19 |
| Ende warme Nacht | 36–40 °C | 0,9–1,2 kPa | 0,12–0,16 | 0,13–0,14 |
| Ende Regeneration Klartag | 95 °C | 7,8 kPa | 0,09 | 0,07–0,08 |

- **Auslegung: x_ads = 0,13, x_des = 0,08, also Δx = 0,05.** Das sind 2,0 kg Wasser pro Tag bei 40 kg Zeolith.
- Als Schutz gegen die Nachtluft-Kritik wird der Ansatz mit dem warmen Nachtwert 0,13 gerechnet. Das ist zugleich das Ergebnis für Bett 36–40 °C.

### 4.3 Wärmebedarf, Kälte und COP

- **Regeneration:** Fühlbar 125 kJ/K · 68 K (27 → 95 °C) = 8,5 MJ. Latent 2,0 kg · 2,8 MJ/kg = 5,6 MJ. Dampfweg und Sammler 0,5 MJ. **Summe 14,6 MJ = 4,06 kWh**, passend zur Stundenrechnung.
- **Verdampfung:** 2,0 · 2,487 = 4,97 MJ = 1,38 kWh.
- **Abzug Kondensat** (flasht von 41 auf 6 °C): 2,0 · 4,19 · 35 = 0,29 MJ = 0,08 kWh.
- **Abzug Speicherverluste:** 150 mm PIR, 2,43 m², ΔT ≈ 19 K ergeben 9 W = 0,22 kWh. Dazu kommt ein Wärmeeintrag über Rohre, Klappe und Strahlung von 4 W = 0,10 kWh, zusammen 13 W.
- **Nutzkälte netto: 1,38 − 0,08 − 0,32 = 0,99 kWh/Tag (41 W).**
- **COP_th** = 4,97/14,6 = **0,34**. Solar-COP = 0,99/16,6 = 6,0 %.
- **Menge:** 0,99 kWh / (1,163 Wh/kgK · 13 K) = **65 L/Tag**.

### 4.4 Nachtprofil stundenaufgelöst

Die Lamellen öffnen um etwa 19:45. Der Bettwärmeverlust läuft über UA_Luft ≈ 39 W/K (Rippen 95 W/K, ε = 0,88 bei 44 W/K Luftwärmestrom) plus Glas etwa 8 W/K, zusammen ≈ 47 W/K. Die Adsorption setzt ein, sobald das Bett unter etwa 45 °C fällt.

| Zeit | Luft | T_Bett | Vorgang |
|---|---|---|---|
| 19:45 | 29,5 | ≈ 66 | Lamellen öffnen, sensible Abkühlung, ca. 550 W |
| 21:00 | 27 | ≈ 40 | Adsorption beginnt, Spitze ca. 500 W Abfuhr |
| 22:00 | 25,5 | ≈ 35 | Adsorption aktiv |
| 00:00 | 24,5 | ≈ 29,5 | |
| 02:00 | 22,5 | ≈ 26 | |
| 04:00 | 21 | ≈ 24 | |
| 06:30 | 20 | ≈ 23 | ca. 120 W |

- Das Fenster-Mittel der Luft beträgt etwa 23 °C, das Bett liegt im Mittel bei etwa 28 °C. Die Nachtluft ist also **nicht** mit 21 °C angesetzt.
- Der Spitzenwert zu Beginn liegt bei T_Bett = 40 °C. Selbst dort bleibt x_eq über 0,13.
- Die gesamte Abfuhr beträgt 1,37 kWh sensibel plus 1,56 kWh Adsorption, das sind etwa 2,9 kWh in rund 11 h (im Mittel 270 W).

### 4.5 Kamin (gekoppelt gerechnet)

Auftrieb, Druckverlust und Wärmeaufnahme wurden iteriert:
- **Balkon:** Kanal 0,17 m², ζ ≈ 5, Höhe ab Rippenblock ≈ 0,75 m, Auftrieb mit ΔT_Luft (im Mittel 75 % von ΔT_aus). Ergebnis: v ≈ 0,22 m/s, V̇ ≈ 0,038 m³/s, Wärmestrom der Luft ≈ 44 W/K. Bei 300 W erwärmt sich die Luft um 6,8 K. Das Bett liegt ≈ 5–6 K über der Zuluft.
- **Fassade:** Kamin 10 m, 0,5 m², ζ ≈ 8, 1,2 kW. Ergebnis: v ≈ 0,44 m/s, Wärmestrom ≈ 254 W/K, ΔT_Luft ≈ 4,7 K.

### 4.6 Auslauftemperatur

Wendel mit UA = 400 W/K, Bad als Reservoir, ε = 1 − exp(−UA/(ṁ·c_p)). Bei 3 L/min ist ε = 0,85:

| Bad | Auslauf bei 3 L/min | bei 5 L/min |
|---|---|---|
| 5 °C (morgens) | 7,9 °C | 11,1 °C |
| 8 °C | 10,4 °C | 13,1 °C |
| 11,5 °C (abends) | 13,4 °C | 15,5 °C |

Das Bad schwingt täglich um etwa 7 K (1,30 kWh/0,192 kWh/K). Bei sparsamer Zapfung (3 L/min) liegt der Tagesmittelwert bei etwa 11 °C, bei 5 L/min bei 13–14 °C.

---

## 5. Fassade

**Aufbau:** 4 Balkonmodule übereinander, je eines pro Geschoss (Geschosshöhe ≈ 3,3 m). Jedes Modul ist ein **eigenes geschlossenes System** mit Verdampfer, Adsorber und Kondensator. Es gibt keine gemeinsame Dampfleitung, deshalb entfallen Gleichverteilung und R2-Probleme. Bei Ausfall eines Moduls laufen die anderen weiter.

**Was die Höhe bringt (ehrlich):**
- **Gemeinsamer hinterlüfteter Kamin** über 10–13 m mit ≈ 254 W/K statt 4 · 44 = 176 W/K, also ≈ +45 % Luftwärmestrom. Das gibt etwa 1,5 K kühleres Bett. Dieser Gewinn ist als Reserve geführt und **nicht** in der Menge angesetzt.
- **Kondensat:** Jedes Modul entwässert per Fallrohr in den eigenen Siphon.
- **Trinkwasser in Reihe:** Bei Reihenschaltung der vier Wendeln (je NTU = 1,15 bei 5 L/min) ist ε = 1 − exp(−4,6) = 0,99. Der Auslauf entspricht dann der Badtemperatur (+0,2 K), selbst bei hohen Zapfraten. Das Bad kann bei etwa 10–11 °C betrieben werden. Ein höherer Verdampferdruck gibt Reserve im Δx und weniger Frostrisiko.
- **Ohne Fassadenhöhe** wäre der Aufbau eine reine Vervierfachung. Das ist die ehrliche Bilanz: Die Höhe verbessert Robustheit und Auslauftemperatur, sie erhöht den Ertrag nur wenig.

**Rechnung:**

| Größe | Wert |
|---|---|
| Zeolith, Δx | 160 kg, 0,05 → 8,0 kg Wasser/Tag |
| Verdampfung | 19,9 MJ = 5,53 kWh |
| Kondensat-Abzug | 0,32 kWh |
| Verluste (4 × 13 W) | 1,25 kWh |
| **Netto ans Leitungswasser** | **3,96 kWh/Tag (165 W)** |
| Menge bei 24 → 11 °C | **≈ 260 L/Tag** (≈ 220 L bei 8,5 °C) |
| Wärmebedarf | 4 × 4,06 = 16,2 kWh = 26 % der 66 kWh Einstrahlung |

Zwei Betriebsarten sind möglich: (a) ein Modul je Wohnung mit 65 L/Tag oder (b) die Reihenschaltung für zentrale Versorgung von 3–4 Wohnungen.

**Verschattung, Statik, Recht:**
- **Verschattung:** Bei 3,3 m Geschosshöhe und 1,3 m Ausladung (0,74 m Auskragung) beträgt der Schattenwurf bei höchstem Sonnenstand (63°) etwa 1,45 m, die nächste Kollektorkante liegt 2,6 m tiefer. Es gibt also keine gegenseitige Verschattung, sonst nur morgens und abends und unter 3 %. Die Module wirken zugleich als Sonnenschutz der Fenster darunter. Das ist eine geometrische Vorprüfung, keine Simulation.
- **Statik:** 4 × 470 kg = 1,9 t auf vier Konsolen (je ≈ 5 kN vertikal). Der Windsog auf 10,8 m² Kollektorfläche liegt bei etwa 12–16 kN. Ein statischer Nachweis in Stahlbeton ist nötig.
- **Brandschutz:** Glas, Edelstahl und Mineralwolle sind nichtbrennbar. Am Tank ist im Balkonfall 150 mm PIR (B1) vorgesehen. An der Fassade ist stattdessen 200 mm Mineralwolle (A1) anzusetzen, das entspricht den 150 mm PIR bei den Verlusten (U ≈ 0,17 W/m²K).
- **Balkon-Fall:** Der Balkon darüber verschattet bei hohem Sonnenstand. Der Kollektor gehört außen vor die Plattenkante mit mindestens 2,5 m freier Höhe, sonst sinkt der Ertrag um 10–25 %. Es fallen Windlast, Genehmigung/WEG und Baurecht an.

---

## 6. Wetter, Bandbreiten, Fallback

| Fall | Δx | Balkon L/Tag |
|---|---|---|
| Hitzewelle (Luft 37 °C, warme Nächte, T_kond 45 °C) | 0,035 | ≈ 38 |
| **Auslegung Klartag** | **0,05** | **65** |
| Kühle Nacht/Literaturisotherme | 0,07 | ≈ 100 (obere Grenze) |
| Heller Dunst (G ≈ 60 %, Endtemperatur ≈ 85 °C, Δx ≈ 0,0225) | 0,0225 | ≈ 18 |
| Bedeckt (G < 250 W/m²) | ≈ 0 | 0 (nur Speicherinhalt) |
| **Silikagel-Fallback** (60 kg, Δx 0,022) | 0,022 | ≈ 34, COP_th ≈ 0,23 |

- Die Stagnationstemperatur des Doppelglaskollektors bei 250 W/m² beträgt etwa 63 °C, das liegt unter der Schwelle von 78 °C. Bei 300 W/m² sind es etwa 81 °C, bei 350 W/m² etwa 88 °C. Ohne mehrere Stunden über 300 W/m² gibt es also keine nutzbare Desorption.
- **Trübwetter-Strategien:**
  - Zeolith (schon in der Auslegung) bringt an Dunsttagen etwa 18 L statt 0.
  - **Option V:** Vakuumröhren- oder Vakuumflachkollektor (rechnerisch mit a₁ ≈ 1,3 W/m²K, a₂ ≈ 0,004 W/m²K² über 100 °C schon ab etwa 250 W/m²). Das rettet dünne Tage teilweise und kostet etwa 5–8 k€ mehr.
  - **Speicher vergrößern:** Ein Bad von 400 L puffert etwa 1,5 Tage länger.
  - **Nachthimmel-Panel (Variante B):** 2 m² bringen nur etwa 0,2 kWh (≈ 13 L) und nur bei klarem Nachthimmel. Es hilft bei Bewölkung nicht und ist kein Trübwetter-Ersatz.
- **Drei Regentage** bleiben ohne Strom ein echtes Ausfallrisiko.

---

## 7. Betrieb, Kosten, offene Punkte

- **Winter:** Anlage außer Betrieb (Kollektor abdecken, Wendel und Bad entleeren). Das Arbeitsmittel bleibt im System.
- **Wartung:** Nachevakuieren alle 2–3 Jahre am Servicestutzen. Das ist Wartung, kein Betriebsstrom.
- **Kosten (grobe Schätzung, ohne Herstellerangebote, ±40 %):**
  - Balkon als Einzelstück etwa 12.000–18.000 €. Der Zeolith allein kostet etwa 1.500–3.000 €. Dazu kommen Helium-dichter Edelstahlaufbau, Sonderklappen und Prüfung.
  - Serie etwa 5.000–8.000 €. Fassade etwa 45.000–70.000 €.
  - Wirtschaftlich ist das **nicht**: 0,99 kWh Kälte kosten mit einer Kompressoranlage etwa 0,3 kWh Strom, das sind über die Saison rund 20 €. Der Nutzen liegt in Stromfreiheit, Geräuschlosigkeit und Betrieb ohne Kältemittel.
- **Offene Prototypfragen:** Herstellerisotherme des Zeoliths, Klappendichtheit R2, Leckrate am Gesamtsystem, Verdampferwirkung des Filzes, gemessene Nachtabfuhr, Kondensator-UA.

### Änderungen gegenüber Runde 2

| Kritik | Korrektur |
|---|---|
| Nachtluft 21 °C zu optimistisch | Stundenprofil 29 → 20 °C, Fenstermittel 23 °C, T_Bett ≈ 28 °C, Δx-Band |
| Kamin widersprüchlich | Gekoppelte Iteration, ΔT_Luft 6,8 K bzw. 4,7 K, größere Rippenfläche (22 m²) |
| C = 100 kJ/K zu niedrig | Massenliste je Bauteil, 125 kJ/K, Zeolith 40 kg, zentrales Dampfrohr |
| Verdampfer unbelegt | Filz statt Wasserfilm, UA aus Konvektion (185 W/K), 1,5 K Auslegung, Tankvolumen 218 L |
| Siphon-Reserve klein | Zweistufig, 1,4 m Tragfähigkeit gegen 1,06 m Bedarf bei 48 °C |
| Nichtkondensierbare Gase | Zwei Sammler in den Sackgassen, realistische Leckrate, Entgasen, Bimetall im Vakuum |
| Klappen lassen Regen ein | Glaskasten dicht, separater Rückkanal mit Lamellen und Insektengitter |
| Solar-Bilanz uneinheitlich | Stundenrechnung offen, Wind 3 m/s, Reserve klar benannt |
| Fassade bloße Skalierung | Ehrlich benannt, eigenständige Module, Verschattung, Statik, Brandschutz |
| Kosten zu niedrig | 12–18 k€ Einzelstück, Trübwetter-Optionen quantifiziert |

---

## 8. Energiebilanz (Zyklusmittel über 24 h, Balkon, Auslegungsfall)

Ein echter stationärer Zustand existiert nicht, weil Tag- und Nachtprozess nacheinander laufen. Die Bilanz gilt daher als 24-h-Mittel. Die Knotentemperaturen sind Zyklusmittel.

| Strom | W |
|---|---|
| Sonne → Kollektor (0,72 · 16,6 kWh) | 498,0 |
| Kollektor → Adsorber | 169,0 |
| Kollektor → Tagluft (Verluste) | 329,0 |
| Verdampfer → Adsorber (Dampf) | 57,6 |
| Adsorber → Kondensator (Dampf) | 55,6 |
| Adsorber → Nachtluft | 171,0 |
| Kondensator → Tagluft (**Kondensationswärme**) | 52,2 |
| Kondensator → Verdampfer (Kondensat) | 3,4 |
| Speicher → Verdampfer | 54,2 |
| Leitungswasser → Speicher (**Nutzkälte**) | 41,2 |
| Tagluft → Speicher (Verlust und Eintrag) | 13,0 |

Zufuhr 498 + 41,2 + 13 = 552,2 W, Abfuhr an die Luft 329 + 52,2 + 171 = 552,2 W. Die Entropieerzeugung beträgt etwa 1,56 W/K.

```json
{
  "knoten": {
    "Sonne": {"T_C": 5500, "rolle": "umgebung"},
    "Luft_Tag": {"T_C": 32, "rolle": "umgebung"},
    "Luft_Nacht": {"T_C": 21, "rolle": "umgebung"},
    "Leitungswasser": {"T_C": 24, "rolle": "umgebung"},
    "Kollektor": {"T_C": 85, "rolle": "komponente"},
    "Adsorber": {"T_C": 60, "rolle": "komponente"},
    "Kondensator": {"T_C": 41, "rolle": "komponente"},
    "Verdampfer": {"T_C": 6, "rolle": "komponente"},
    "Kaeltespeicher": {"T_C": 8, "rolle": "komponente"}
  },
  "stroeme": [
    {"von": "Sonne", "nach": "Kollektor", "W": 498.0, "art": "strahlung"},
    {"von": "Kollektor", "nach": "Adsorber", "W": 169.0, "art": "waerme"},
    {"von": "Kollektor", "nach": "Luft_Tag", "W": 329.0, "art": "waerme"},
    {"von": "Verdampfer", "nach": "Adsorber", "W": 57.6, "art": "stoff"},
    {"von": "Adsorber", "nach": "Kondensator", "W": 55.6, "art": "stoff"},
    {"von": "Adsorber", "nach": "Luft_Nacht", "W": 171.0, "art": "waerme"},
    {"von": "Kondensator", "nach": "Luft_Tag", "W": 52.2, "art": "waerme"},
    {"von": "Kondensator", "nach": "Verdampfer", "W": 3.4, "art": "stoff"},
    {"von": "Kaeltespeicher", "nach": "Verdampfer", "W": 54.2, "art": "waerme"},
    {"von": "Leitungswasser", "nach": "Kaeltespeicher", "W": 41.2, "art": "waerme"},
    {"von": "Luft_Tag", "nach": "Kaeltespeicher", "W": 13.0, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Leitungswasser", "T_ein_C": 24, "T_aus_C": 11, "kuehlleistung_W": 41.2},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```