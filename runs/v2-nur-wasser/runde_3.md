# Wasserleitung kühlen im geschlossenen Wasserkreislauf: solar getriebener Silikagel-Kühler ohne Strom (Runde 3)

## 1. Kurzfassung

**Der reine Verdunster-Kondensator-Loop kühlt nicht.** Dampf strömt nur zum niedrigeren Druck, also zur kälteren Stelle. Der Kondensator müsste kälter sein als die Leitung. Bei 32 °C und 40 % r. F. liegt die Feuchtkugeltemperatur bei etwa 22 °C. Ein offener nasser Lappen bringt 24 °C-Wasser also nur auf 22–23 °C, und das Wasser geht verloren. Die Kondensationswärme muss deshalb auf ein höheres Temperaturniveau gehoben und dort an die Luft abgegeben werden. Das leistet hier die Sonne, so wie ein Kompressor es täte.

**Prinzip:** eine solar getriebene Adsorptionskältemaschine. Arbeitsmittel ist nur Wasser, Sorbens ist Silikagel. Sie läuft im Tag/Nacht-Zyklus.

- **Nachts (Kälte):**
  - Wasser verdampft bei 4–9 °C und etwa 1 kPa in einem Docht-Verdampfer, der im Kältebad liegt.
  - Das Silikagel bindet den Dampf. Die Bindungswärme geht über einen Rückkanal mit Kamineffekt an die Nachtluft.
- **Tags (Regeneration):**
  - Die Sonne heizt das Gel im verglasten Kollektor auf 100–110 °C.
  - Der Dampf kondensiert im Rippenkondensator bei etwa 40–42 °C und gibt die Wärme an die Tagluft (32 °C) ab.
  - Das Kondensat läuft per Schwerkraft durch einen Siphon zurück zum Verdampfer.
- **Antrieb:** Sonnenwärme, Tag/Nacht-Wechsel, Schwerkraft, Kamineffekt und wachsgesteuerte Klappen.
- **Strom und Verluste:** 0 W Strom, 0 L Wasserverlust.

**Wo bleibt die Kondensationswärme?** Sie geht am Kondensator bei etwa 42 °C an die 32 °C warme Tagluft. Das ist wärmer als die Luft, also fließt sie von selbst dorthin. Die Leitung bleibt kalt, weil Verdampfung (5 °C) und Kondensation (42 °C) zeitlich und räumlich getrennt auf zwei Temperaturen liegen. Das Gel puffert den Dampf dazwischen. Ohne Sonne gäbe es netto null Kühlung.

**Ergebnis Auslegungsfall (klarer Sommertag, stündlich gerechnet, mit Bandbreite):**

| | Balkon | Fassade (4 Geschosse) |
|---|---|---|
| Kollektorfläche | 3,6 m² (2,75 × 1,3 m, 50° Neigung) | 4 × 3,6 = 14,4 m² |
| Silikagel | 56 kg | 224 kg |
| Nutzkälte ans Leitungswasser (netto) | 0,84 kWh/Tag (Mittel 35 W) | 4,0 kWh/Tag (Mittel 166 W) |
| Menge 24 °C → im Mittel 11 °C | **ca. 55 L/Tag** (Band 30–75) | **ca. 260 L/Tag** (Band 130–330) |
| Auslauftemperatur | 9–12 °C bei 3 L/min, 12–15 °C bei 5 L/min | ebenso, 600-L-Speicher |
| Strom / Wasserverlust | 0 W / 0 L | 0 W / 0 L |
| Klarer Himmel / Dunst / bedeckt | 55 L / ca. 8 L / 0 L | 260 L / ca. 40 L / 0 L |

Die 59 L aus Runde 2 gelten als Obergrenze. Die Ursachen für die Abweichung sind in den Abschnitten 4 und 8 dokumentiert.

---

## 2. Energiepfad und zweiter Hauptsatz

```
 TAG (Sonne)                                   NACHT
 Sonne --> Kollektor/Adsorber 80-110 C         Bad 6-10 C --> Verdampfer 4-9 C
   Gel gibt Dampf ab (Klappe R1)                 Dampf (Klappe R2) --> Adsorber 25-40 C
   --> Kondensator 42 C --> Tagluft 32 C          Bindungswaerme --> Rueckkanal --> Nachtluft
   Kondensat --> Siphon --> Verdampfer            R1 zu (Kondensator trocken)
```

Es gibt drei Temperaturen: Antrieb 100–110 °C, Wärmeabgabe 25–42 °C, Kälte 5 °C. Der Carnot-Grenzwert liegt bei COP ≈ 1,5. Realisiert werden **COP_th = 0,24**, das sind etwa 16 % von Carnot. Das ist für ein einbettiges Gerät ohne Wärmerückgewinnung ehrlich. Der Solar-COP (Kälte / Einstrahlung) beträgt nur 0,045.

---

## 3. Aufbau Balkon

**Voraussetzungen:**
- Ausrichtung nach Süden (±30°).
- Von 9 bis 17 Uhr unverschattet. Ein Balkon direkt unter einem anderen wirft Schatten, weil die Mittagssonne 60° hoch steht. Geeignet sind oberstes Geschoss, Dachterrasse oder Vorbaubalkon.
- Gewicht etwa 800 kg auf 3 m², das sind 2,6 kN/m². Das liegt unter der Balkon-Nutzlast von 4 kN/m², braucht aber einen Statiknachweis.
- Windsog am Kollektor etwa 4 kN, Verankerung an Wand und Brüstung.
- Genehmigung und Zustimmung des Eigentümers.

```
 Seitenansicht (Sued links, Wand rechts)

   Sonne \  \                    Kamin-Haube (Regenschutz, Insektengitter)
          \  \  Doppelglas 50 Grad     |  ~2,4 m
           \  \_______________________|__
            \  \ 30 Rohre + Gel  ||Rueckkanal 10 cm, Rippen|| --> Abluft
             \__\_________________||_________________________
   Zuluft-Lamellen unten (nach unten offen, Insektengitter) ^
   [Klappen im Rueckkanal, nicht im Glaskasten]
                                                          KONDENSATOR
   +--- Bad-Tank 2,8 x 0,30 x 0,42 m, 150 mm Daemmung ---+   (Rippen, Schatten)
   |  12 Docht-Verdampferrohre DN40 | Trinkwasser-Wendel  |        | Kondensat
   +------------------------------------------------------+   Siphon 1,4 m (Endfach)
   Grundflaeche 1,0 x 3,0 m (Modul 2,75 m + Endfach 0,25 m)
```

### 3.1 Bauteile

**Adsorber:**
- 30 Rohre Edelstahl 1.4404, Ø 42,4 × 1,0 mm, je 2,6 m lang, mit 0,72 kg Gel pro Meter und je einem zentralen Lochrohr für den Dampf. Das ergibt 56 kg Gel bei etwa 80 % Füllgrad.
- Ein Kupfer-Sternprofil verkürzt den Wärmeweg im Bett auf etwa 10 mm.
- Die Rohre sind rund und daher vakuumfest (Beulgrenze etwa 5 MPa gegen 0,1 MPa).
- Sammler, Dampfleitung und Flansche sind geschweißt oder metallgedichtet.
- Auf dem Absorberblech (Alu, selektive Beschichtung, nur außerhalb des Vakuums) sitzen rückseitig Längsrippen.

**Kollektor:**
- Doppelverglasung mit η₀ = 0,68, a₁ = 3,3 W/m²K (Windmittel), a₂ = 0,012 W/m²K².
- Der Glaskasten ist **dauerhaft geschlossen**. Der Druckausgleich läuft über eine Membran mit Trockenpatrone.

**Rückkanal, Klappen, Wachselemente:**
- Der Rückkanal (10 cm Tiefe) liegt hinter dem Absorber. Nachts strömt Luft an den Rippen entlang.
- Die Lamellen sind regengeschützt, mit Insektengitter und Haube. Alles ist zugänglich und abnehmbar zur Reinigung.
- Wachselement E1 sitzt an einem kleinen Strahlungssensor (schwarze Platte hinter Einfachglas).
  - Es schließt die Kanalklappen bei > 40 °C und öffnet bei < 35 °C.
  - Der Sensor schaltet etwa bei 90–150 W/m². Tagsüber ist der Kanal also zu, ab etwa 19 Uhr auf.
- Wachselement E2 sitzt am Sammler. Es öffnet die Klappen bei > 112 °C und schließt bei < 104 °C (Überhitzungsschutz).
- Der Glaskasten wird nicht geöffnet. Damit gelangen kein Regen, Staub oder Insekten an Dämmung und Beschichtung.

**Verdampfer:**
- 12 Rohre DN40 (48,3 × 1,6 mm), je 2,7 m lang, im Bad. Innen liegt ein Sinterfilz-Docht (1,5 mm) mit einem Sumpf von höchstens 10 mm.
- Der Docht beseitigt den Siedeverzug. Ein 1 cm hoher Pool würde bei 1 kPa etwa 1 K Verzug bringen.
- Docht-Fläche etwa 4,6 m², h_eff etwa 150 W/m²K. Zusammen mit der Badseite (etwa 200 W/m²K) ergibt das UA ≈ 400 W/K.
- Bei Spitze 350 W sind das etwa 0,9 K, ich rechne mit **2 K Reserve**: T_verd = T_bad − 2 K.
- Tank: 2,8 × 0,30 × 0,42 m, 350 L brutto. Einbauten sind 12 Rohre (etwa 60 L) und die Wendel (9 L). Es bleiben **etwa 270 L Wasser**.
- Trinkwasser-Wendel: Edelstahl-Wellrohr, 24 m DN20, UA ≈ 400 W/K, ohne Verbindung zum Vakuum.
- Dämmung 150 mm PU. Wenn A1-Nichtbrennbarkeit gefordert ist, geht auch Schaumglas mit 200 mm (etwas höhere Verluste).

**Kondensator:**
- Verrippte Rohre, etwa 8 m², UA ≈ 55 W/K, im Schatten hinter dem Kollektor.
- T_kond etwa 40 °C bei 32 °C Luft (ΔT ≈ 8 K bei 260 W Mittel während der Desorption).

**Siphon (Kondensatschleuse):**
- Tagsüber gilt Δp = p_kond − p_verd. Bei 42 °C sind das 8,2 − 1,0 = 7,2 kPa, also 0,73 m Wassersäule.
- Bei Hitzewelle (Kondensator 48 °C, 11,2 kPa) sind es 1,05 m. Bei 52 °C wären es 1,3 m.
- **Schenkel: 1,4 m**, gedämmt, im Endfach. Das ergibt 33 % Reserve bis 48 °C.
- Zusätzlich sitzt ein Schwimmer-Kondensatableiter (Edelstahl, ohne Strom, nur Wasser) in Reihe. Er hält das Wasser auch dann zurück, wenn der Siphon leergedrückt wird.

**Dampfdiode R2 (Verdampfer → Adsorber):**
- Folienklappe aus PTFE (0,1 mm) auf geläpptem, waagerechtem Edelstahl-Sitz, als Doppelklappe in Reihe.
- Öffnungsdruck etwa 2 Pa, das entspricht 0,03 K.
- Zulässige Rückleckage etwa 10 % des Dampfstroms, also 0,01 g/s.
- Das größte Prototyprisiko ist ein festklebender Kondensatfilm.
- R1 (Adsorber → Kondensator) ist Komfort, weil der Kondensator nachts trocken ist.

**Frostwächter:** Ein Wachsthermostat mit Faltenbalg-Durchführung sperrt R2 bei Bad < 3 °C. Im Winter wird die Anlage entleert und abgedeckt.

### 3.2 Nichtkondensierbare Gase

- **Wo sich Gas sammelt:**
  - Nachts strömt der Dampf zum Adsorber. Das Gas wandert dabei ans Bettende.
  - Deshalb hängt ein Gassammler (5 L) als Sackgasse am fernen Ende des Adsorber-Sammlers.
  - Ein zweiter Sammler (2 L) sitzt am Kondensatorende für den Tagbetrieb.
- **Vor der Inbetriebnahme:**
  - Das Wasser wird beim Befüllen unter Vakuum entgast.
  - Das Gel wird bei 150 °C unter Vakuum ausgeheizt.
  - Jedes Bauteil erhält eine He-Lecktest-Abnahme.
- **Leckbudget:**
  - Gesamt ≤ 5·10⁻⁸ mbar·L/s (alle Bauteile zusammen).
  - Das sind etwa 1600 Pa·L in 10 Jahren. In 2 Jahren sind es 320 Pa·L, verteilt auf 7 L also etwa 46 Pa.
  - Der Dampfdruck im Kondensator ist 8000 Pa. Das ist unschädlich.
- **Wartung:** Alle 2 Jahre wird über einen Service-Stutzen nachevakuiert. Das ist eine Handpumpe oder ein Servicegerät und kein Betriebsstrom.
- **Ehrlich:** Faltenbalg, Folienklappen und Ventile sind die Leckrisiken. Die Dichtheit muss der Prototyp belegen.

### 3.3 Sicherheit

- Wenn der Kondensatorweg blockiert ist und der Kollektor stagniert (bis 150 °C), gilt bei Gel x = 0,073: p = 0,177 · p_s(150 °C) ≈ 84 kPa abs, also unter 1 bar.
- Rohre und Sammler sind für 1 MPa ausgelegt. Zusätzlich sitzt ein Sicherheitsventil bei 150 kPa abs.
- Es gibt Berührungsschutz und Verbundglas.

---

## 4. Rechnung Balkon (klarer Tag)

### 4.1 Isotherme (Modellannahme) und Δx

Näherung für Silikagel RD im Bereich φ = 0,05–0,3: **x = 0,02 + 0,3·φ** mit φ = p/p_s(T_Bett). Das ist eine Modellannahme (±30 %) und muss am Prototyp gemessen werden.

**Regeneration (p_kond = 8,2 kPa):**

| Bett-Endtemperatur | φ | x_des |
|---|---|---|
| 90 °C | 0,117 | 0,055 |
| 100 °C | 0,081 | **0,044** (Auslegung) |
| 108 °C | 0,061 | 0,038 |

Das Desorptionsende bei 100 °C entspricht x_des ≈ 0,045.

**Adsorption:** Am Morgen erreicht das Bett x_ads ≈ **0,073**. Das liegt bewusst unter dem Gleichgewicht, denn Kinetik und Frostwächter begrenzen. Bei 23,5 °C Bett und 6 °C Verdampfer wäre das Gleichgewicht x ≈ 0,11. Die Differenz ist Reserve für warme Nächte.

**Δx_Auslegung = 0,073 − 0,045 = 0,028.** Daraus folgen 56 kg × 0,028 = **1,57 kg Wasser pro Tag**.

**Δx-Bandbreite:**
- Warme Nacht (Luft +4 K, Bett etwa 30 °C): Δx ≈ 0,017–0,022.
- Hitzewelle (Kondensator 48 °C, T_end maximal 108 °C): Δx ≈ 0,022.
- Kühle Nacht: bis 0,04, begrenzt durch Bad und Frostwächter.

Das ergibt **30–75 L/Tag**.

### 4.2 Massenliste und Wärmebedarf

| Bauteil | Masse | Wärmekapazität |
|---|---|---|
| Gel | 56 kg | 51 kJ/K |
| Adsorbiertes Wasser (Mittel x ≈ 0,06) | 3,4 kg | 14 kJ/K |
| Stahlrohre 78 m × 1,03 kg/m | 80 kg | 40 kJ/K |
| Kupfer-Stern 0,4 kg/m | 31 kg | 12 kJ/K |
| Alu-Absorberblech 1 mm | 10 kg | 9 kJ/K |
| Alu-Rippen im Rückkanal | 16 kg | 14 kJ/K |
| Sammler, Dampfleitung, Flansche | 20 kg | 10 kJ/K |
| Kleinteile, Innenscheibe (anteilig) | – | 10 kJ/K |
| **Summe** | | **C ≈ 160 kJ/K** |

- Fühlbare Wärme: 160 kJ/K × 75 K (25 → 100 °C) = 12,0 MJ.
- Desorption: 1,57 kg × 2,8 MJ/kg = 4,4 MJ.
- **Summe 16,4 MJ = 4,56 kWh** (Mittel 190 W).
- COP_th = 3,90 / 16,4 = **0,24**.

### 4.3 Kollektor stündlich

Profil: 800 W/m² Spitze auf 50° Neigung, 5,2 kWh/m²·Tag, also 18,7 kWh auf 3,6 m². Luft: 22 °C um 8 Uhr, 32 °C ab 13 Uhr. Ausgangs-Bett 25 °C. Die Rechnung ist eine Stundenbilanz mit η₀ = 0,68, a₁ = 3,3, a₂ = 0,012 und C = 160 kJ/K.

| Uhr | G (W/m²) | Bett-T Ende | x | Bemerkung |
|---|---|---|---|---|
| 08:30 | 60 | 27 °C | 0,073 | R2 schließt |
| 09:30 | 220 | 37 °C | 0,073 | |
| 10:30 | 420 | 54 °C | 0,073 | |
| 11:30 | 610 | 75 °C | 0,073 | Desorption beginnt bei ca. 79 °C |
| 12:30 | 740 | 85 °C | 0,061 | |
| 13:30 | 800 | 97 °C | 0,048 | |
| 14:30 | 760 | 100–108 °C | 0,045–0,038 | E2 begrenzt bei 112 °C |

**Wichtig:** Die Desorption beginnt erst bei etwa 79 °C, weil der Kondensator bei 8,2 kPa liegt. Runde 2 nannte 62–65 °C, das war zu niedrig.

- Windstill ist das Desorptionsende (100 °C) um etwa 13:20 erreicht.
- Bei **3 m/s Wind** (a₁ 3,3 → 4,0, Verluste etwa +20 %) ist es etwa 14:15. Der Wind kostet eine Stunde, aber keine Menge, weil Reserve da ist.
- Der Nutzungsgrad der Einstrahlung beträgt 16,4 MJ / 67 MJ ≈ 24 %.

### 4.4 Nachtwärmeabfuhr: gekoppelte Kaminrechnung

Rückkanal: 3,0 m breit, 0,10 m tief, Rippenlänge 1,2 m, 100 Alu-Rippen (0,5 mm, 30 mm Abstand), freie Fläche 0,29 m², Kaminhöhe H = 2,0 m.

**Ansatz (gekoppelt):**
- Auftrieb: Δp_b = ρ·g·H·β·ΔT_eff. ΔT_eff ist die *Lufterwärmung im Kanal* (nicht Bett minus Luft), gewichtet über die Höhe: Δp_b ≈ 0,055 Pa/K · ΔT_Luft.
- Druckverlust: Δp = 0,288·v (laminare Rippenpackung) + 2,07·v² (Lamellen, Gitter, Haube; K ≈ 3,5).
- Wärme: Q = ṁ·c_p·ε·(T_Bett − T_Luft). Dabei ist ε = 1 − e^(−NTU), NTU = UA/(ṁ·c_p), UA_Luft = h·A_Rippen·η = 3,3 · 24 · 0,88 ≈ 65 W/K.

**Iteration bei 15 K Bett–Luft:**

| v (m/s) | NTU | ε | ΔT_Luft (K) | Auftrieb (Pa) | Verlust (Pa) |
|---|---|---|---|---|---|
| 0,15 | 1,36 | 0,74 | 11,1 | 0,61 | 0,09 |
| 0,30 | 0,68 | 0,49 | 7,4 | 0,41 | 0,27 |
| **0,35** | 0,58 | 0,44 | 6,6 | **0,365** | **0,355** |
| 0,40 | 0,51 | 0,40 | 6,0 | 0,33 | 0,45 |

- Ergebnis: v ≈ 0,35 m/s, 0,10 m³/s, Q ≈ 0,79 kW bei 15 K, also **UA_eff ≈ 50 W/K** (45–53 W/K je nach Bett–Luft-ΔT).
- Runde 2 setzte 33 W/K an, aber mit dem falschen ΔT von 10 K. Hier ist die Rippenfläche gegenüber Runde 2 deutlich größer.
- Bei 350 W Spitze liegt das Bett damit etwa 7–8 K über der Luft, im Mittel etwa 5 K.
- Die Adsorptionswärme beträgt 1,57 kg × 2,8 MJ = 4,4 MJ in etwa 9 h.

**Nachtprofil (stündlich gerechnet mit Kinetik τ = 1,5 h):**

| Uhr | Luft | T_Bett | Bad | T_Verd | p_Verd | x |
|---|---|---|---|---|---|---|
| 19:30 | 27 °C | 110 °C | – | – | – | 0,04 |
| 21:00 | 26 °C | 41 °C | 10,0 °C | 8,5 °C | 1,11 kPa | 0,052 |
| 23:00 | 24 °C | 32 °C | 8,8 °C | 7,3 °C | 1,02 kPa | 0,063 |
| 01:00 | 22 °C | 28 °C | 7,9 °C | 6,6 °C | 0,97 kPa | 0,069 |
| 03:00 | 21 °C | 25,5 °C | 7,3 °C | 6,3 °C | 0,95 kPa | 0,072 |
| 05:00 | 20 °C | 23,5 °C | 6,9 °C | 6,1 °C | 0,93 kPa | 0,073 |

- Die Adsorption beginnt gegen 20:15, sobald das Bett unter etwa 52 °C fällt.
- Das mittlere Luftfenster von 21:00 bis 07:00 liegt bei etwa 22 °C.
- Warme Nacht (+4 K): Bett +4 K, Δx sinkt auf etwa 0,02.

### 4.5 Kälte und Auslauf

**Nutzkälte:**
- Verdampfung: 1,57 kg × 2,49 MJ/kg = 3,90 MJ = **1,085 kWh**.
- Kondensat (40 → 8 °C): 1,57 × 4,19 × 32 = 0,21 MJ = 0,058 kWh.
- Speicherverlust (150 mm, 2,15 m², ΔT ≈ 18 K, plus Leitungen): 0,19 kWh.
- **Netto 0,837 kWh/Tag (34,9 W).**

**Menge:** 0,837 / (1,163 Wh/kgK · 13 K) = **55 L/Tag**.

**Auslauf** (Bad 270 L = 314 Wh/K; Schwingung 3,5 K, 6,6 °C morgens bis 10,2 °C abends, Mittel 8,4 °C). Die Wendel hat UA = 400 W/K und das Bad wirkt als Reservoir, also ε = 1 − exp(−UA/(ṁ·c_p)):

| Zapfrate | ε | T_aus morgens | T_aus abends | Mittel |
|---|---|---|---|---|
| 3 L/min | 0,85 | 9,2 °C | 12,3 °C | **10,8 °C** |
| 5 L/min | 0,68 | 12,2 °C | 14,6 °C | 13,4 °C |
| 8 L/min | 0,51 | 15,1 °C | 17,0 °C | 16,1 °C |

Kälte ist also nur bei sparsamer Zapfung deutlich unter der Luft (32 °C) und deutlich unter der Wasser-Eintrittstemperatur (24 °C). Das ist die ehrliche Grenze.

### 4.6 Energiebilanz (24-h-Mittel, Balkon, klarer Tag)

Es gibt keinen stationären Zustand, in dem Tag- und Nachtvorgang gleichzeitig laufen. Die Bilanz ist deshalb ein 24-h-Mittel. Die Knotentemperaturen sind Zyklusmittel.

| Strom | Leistung |
|---|---|
| Sonne → Kollektor (0,68 · 779 W) | 530 W |
| Kollektor → Adsorber | 190 W |
| Kollektor → Tagluft (Verluste, Überschuss) | 340 W |
| Verdampfer → Adsorber (Dampf, latent) | 45,3 W |
| Adsorber → Kondensator (Dampf) | 44,5 W |
| Adsorber → Nachtluft | 190,8 W |
| Kondensator → Tagluft (**Kondensationswärme**) | 42,1 W |
| Kondensator → Verdampfer (Kondensat, fühlbar) | 2,4 W |
| Kältespeicher → Verdampfer | 42,9 W |
| Leitungswasser → Kältespeicher (**Nutzkälte**) | 34,9 W |
| Tagluft → Kältespeicher (Verlust) | 8,0 W |

Zufuhr: 530 + 34,9 + 8,0 = 572,9 W. Abfuhr an die Luft: 340 + 190,8 + 42,1 = 572,9 W.

---

## 5. Fassadenvariante (4 Geschosse, 12–14 m)

**Aufbau:**
- Vier Module (je 3,6 m², 56 kg Gel) auf Höhe der Fensterbrüstung, eines pro Geschoss.
- Die Module verdecken keine Fenster und verschatten sich nicht: Die Sonne steht mittags 63° hoch, der Schatten einer Modul-Unterkante fällt etwa 1,5 m nach unten auf die Wand. Das nächste Modul liegt bei 3 m Geschosshöhe außerhalb des Schattens.
- Alle vier hängen an einem gemeinsamen Dampfsteigrohr DN150 (12 m). Jedes Modul hat **eigene R1/R2**, eigenen Siphon und eigenen Frostwächter.
- Zwischen den Modulen läuft ein gemeinsamer Kaminschacht hinter der Fassadenverkleidung, mit Haube und Windschutz gegen Rückströmung.

**Wie die Höhe genutzt wird:**
- Der gemeinsame Kamin (H = 10–11 m) liefert etwa 1,3–1,5 Pa Auftrieb. Das ist etwa das Vierfache der Balkonvariante.
- Das ist der einzige Weg, dichtere Rippenpakete (20 mm Abstand, UA ≈ 110 W/K) zu betreiben, die auf dem Balkon den Luftstrom abwürgen würden. Ein Modul erreicht dann **UA_eff ≈ 85 W/K** (Balkon 50 W/K).
- Höhe allein bringt bei gleichen Rippen nur etwa 15 % mehr, denn die Rippen begrenzen. Der Gewinn kommt aus Höhe plus mehr Fläche.
- Das Bett ist dadurch 3–4 K kälter, Δx ≈ **0,030**.
- Das obere Modul hat weniger Auftrieb (nur die eigene Rückkanal-Höhe) und liegt bei etwa 55–60 W/K. Es adsorbiert etwas weniger, das gleicht sich über den gemeinsamen Dampfdruck von selbst aus.

**Dampfleitung 12 m, DN150:**
- Dampfstrom nachts etwa 0,25 g/s, Spitze 0,7 g/s. Mit ρ = 0,0066 kg/m³ sind das 38–110 L/s, also bis 6 m/s.
- Der Druckabfall beträgt etwa 1 Pa und ist gegen 65–80 Pa/K vernachlässigbar.
- Die Kondensatleitung wird zum Fallrohr.

**Rechnung:**

| Größe | Wert |
|---|---|
| Gel, Δx | 224 kg, 0,030 |
| Wasser | 6,7 kg/Tag |
| Verdampfung | 16,7 MJ = 4,65 kWh |
| Kondensat-Abzug | 0,25 kWh |
| Speicherverlust (600 L, 150 mm, 4,5 m²) | 0,42 kWh |
| **Netto ans Leitungswasser** | **4,0 kWh/Tag (166 W)** |
| Menge bei 24 → 11 °C | **ca. 260 L/Tag** (Band 130–330) |
| Wärmebedarf | 18,2 kWh = 24 % der Einstrahlung (75 kWh) |

- Der 600-L-Speicher (0,70 kWh/K) steht im Keller. Seine Schwingung beträgt etwa 6,6 K.
- Die Wendel muss für Fassadenzapfraten ausgelegt werden: 72 m DN20 in drei Strängen, UA ≈ 1200 W/K.
- Die 260 L decken etwa 3–4 Wohnungen zu je 60–100 L.

**Fassaden-spezifische Punkte:**
- **Tragwerk:** Gel 224 kg, Stahl etwa 400 kg, Speicher im Keller, Kollektorkästen etwa 500 kg. Das sind rund 1,3 t an der Fassade auf 8 Konsolen mit Statiknachweis.
- **Windlast:** Sog etwa 1,2 kN/m² × 14,4 m² ≈ 17 kN. Die Verankerung muss im tragenden Mauerwerk sitzen.
- **Brandschutz:** Wo Nichtbrennbarkeit gefordert ist, kommen nur A1-Materialien (Stahl, Glas, Mineralwolle) in Frage. Das Wasser als Arbeitsmittel ist unkritisch.
- **Genehmigung:** Fassadenanbau, Denkmalschutz, Eigentümergemeinschaft.

---

## 6. Wetter und Betrieb

Die Leistung ist nicht proportional zur Einstrahlung, weil die Desorption eine Schwellentemperatur braucht (etwa 79 °C).

| Wetter | Einstrahlung | Bett-Endtemperatur | Δx | Balkon netto |
|---|---|---|---|---|
| Klar | 5,2 kWh/m²d | 100–108 °C | 0,028 | 55 L/Tag (Band 30–75) |
| Heller Dunst | ca. 3,1 kWh/m²d | ca. 85 °C | ca. 0,008 | ca. 8 L (deckt nur Speicherverlust) |
| Bedeckt | ≤ 2 kWh/m²d | 45–65 °C | ≈ 0 | 0 |

- Die Dunst-Zeile ist eine Stundenrechnung mit 60 % Einstrahlung: Das Bett kommt nur knapp über 80 °C.
- Der Kältespeicher (270 L) puffert etwa einen Tag. Bei drei Regentagen fällt die Kälte aus. Das ist ohne Strom nicht behebbar.
- Ein Vakuumröhren-Absorber (a₁ ≈ 1,5, a₂ ≈ 0,005) würde bei Dunst nach Abschätzung etwa 65 % der Klarmenge halten, also etwa 35 L. Er kostet etwa 2500 € mehr und ist im Prototyp mit Wärmeübertrager-Verlusten zu prüfen.

---

## 7. Kosten, Wartung, Rückfallebene

**Kosten Balkon (Einzelstück, ohne Herstellerangebote, aus Bauteilen geschätzt):**

| Posten | Betrag |
|---|---|
| Edelstahlrohre, Sammler, Schweißen, He-Test | ≈ 4.500 € |
| Gel, Glas, Rahmen, Dämmung | ≈ 2.000 € |
| Tank, Wendel, Verdampferrohre | ≈ 1.500 € |
| Kondensator | ≈ 700 € |
| Klappen, Wachselemente, Balg, Ventile (Sonderteile) | ≈ 2.500 € |
| Montage, Statik, Genehmigung | ≈ 3.000 € |
| **Summe** | **≈ 14.000–18.000 €** |

- Fassade: etwa 45.000–70.000 €. Serie Balkon: etwa 6.000–8.000 €.
- Wirtschaftlich ist das einer Kompressoranlage klar unterlegen. Deren 0,84 kWh Kälte brauchen etwa 0,25 kWh Strom. Der Nutzen liegt in der Stromfreiheit und der Betriebssicherheit ohne Kältemittel.

**Wartung:**
- Alle 2 Jahre Nachevakuieren.
- Glas und Rückkanal reinigen.
- Frostwächter im Herbst prüfen.
- Wenn im Winter Frost droht, wird die Anlage entleert.

**Unsicherheit:** ±30 %. Zu messen sind vor allem die Isotherme, die Klappendichtheit, der Docht-Verdampfer (h_eff) und die reale Nachtabfuhr.

### Variante B: rein passiv, ohne Sorbens (schwächer, Rückfallebene)

- Ein evakuiertes Wasser-Wärmerohr verbindet die Speicherwendel mit einer nachts zum klaren Himmel abstrahlenden Fläche (Berdahl-Martin: Himmel etwa 6 °C bei 20 °C Luft und 17 °C Taupunkt).
- Netto-Abstrahlung etwa 10–20 W/m², bei 3 m² und 8 h etwa 0,36 kWh/Nacht.
- Das sind etwa 30 L auf etwa 15 °C, also nicht deutlich kälter als die Luft.
- Bei bedecktem Himmel fällt auch das aus. Als Zusatz zur Hauptvariante taugt es deshalb nicht gegen Schlechtwetter.

---

## 8. Was gegenüber Runde 2 korrigiert wurde

| Kritik | Korrektur |
|---|---|
| Nachtluft 21 °C als Minimum | Stündliches Nachtprofil (26 → 20 °C, Mittel 22 °C), Δx-Band 0,017–0,04, 59 L nur noch Obergrenze |
| Kamin widersprüchlich | Gekoppelte Iteration aus Auftrieb, Druckverlust, Wärme (UA_eff ≈ 50 W/K, 0,35 m/s) |
| C = 100 kJ/K zu niedrig | Massenliste, C = 160 kJ/K, COP_th 0,24 |
| Verdampfer unbelegt | Docht-Verdampfer, UA ≈ 400 W/K, 2 K Reserve, Tank 270 L netto |
| Siphon-Reserve minimal | Schenkel 1,4 m (33 % Reserve bis 48 °C) plus Schwimmer-Ableiter |
| Nichtkondensierbare Gase | Sammler am Bettende, Entgasung, Leckbudget je Bauteil, Wartung |
| Offene Klappen im Glaskasten | Glaskasten geschlossen, Klappen im geschützten Rückkanal, Insektengitter, Reinigung |
| Solarbilanz uneinheitlich | Stundenrechnung mit Wind, Desorptionsbeginn bei 79 °C korrigiert, Überschuss ehrlich benannt |
| Fassade = 4× Skalierung | Verschattung geprüft, Kamin plus dichtere Rippen, Statik, Brandschutz, Windlast, Modul-R1/R2 |
| Kosten optimistisch | Aufstellung, 14.000–18.000 € |
| Trübwetter | Dunst 8 L, Vakuumröhren als Option quantifiziert, Passivvariante nur als Rückfallebene |

---

## 9. Energiebilanz (Auslegungsfall Balkon, 24-h-Mittel)

```json
{
  "knoten": {
    "Sonne": {"T_C": 5500, "rolle": "umgebung"},
    "Luft_Tag": {"T_C": 32, "rolle": "umgebung"},
    "Luft_Nacht": {"T_C": 21, "rolle": "umgebung"},
    "Leitungswasser": {"T_C": 24, "rolle": "umgebung"},
    "Kollektor": {"T_C": 85, "rolle": "komponente"},
    "Adsorber": {"T_C": 60, "rolle": "komponente"},
    "Kondensator": {"T_C": 42, "rolle": "komponente"},
    "Verdampfer": {"T_C": 6.4, "rolle": "komponente"},
    "Kaeltespeicher": {"T_C": 8.4, "rolle": "komponente"}
  },
  "stroeme": [
    {"von": "Sonne", "nach": "Kollektor", "W": 530.0, "art": "strahlung"},
    {"von": "Kollektor", "nach": "Adsorber", "W": 190.0, "art": "waerme"},
    {"von": "Kollektor", "nach": "Luft_Tag", "W": 340.0, "art": "waerme"},
    {"von": "Verdampfer", "nach": "Adsorber", "W": 45.3, "art": "stoff"},
    {"von": "Adsorber", "nach": "Kondensator", "W": 44.5, "art": "stoff"},
    {"von": "Adsorber", "nach": "Luft_Nacht", "W": 190.8, "art": "waerme"},
    {"von": "Kondensator", "nach": "Luft_Tag", "W": 42.1, "art": "waerme"},
    {"von": "Kondensator", "nach": "Verdampfer", "W": 2.4, "art": "stoff"},
    {"von": "Kaeltespeicher", "nach": "Verdampfer", "W": 42.9, "art": "waerme"},
    {"von": "Leitungswasser", "nach": "Kaeltespeicher", "W": 34.9, "art": "waerme"},
    {"von": "Luft_Tag", "nach": "Kaeltespeicher", "W": 8.0, "art": "waerme"}
  ],
  "nutzen": {"knoten": "Leitungswasser", "T_ein_C": 24, "T_aus_C": 11, "kuehlleistung_W": 34.9},
  "luft_T_C": 32,
  "wasserverlust_l_pro_tag": 0
}
```