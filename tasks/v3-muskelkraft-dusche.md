# Aufgabe: Kühlkabine mit Fahrrad und kalter Dusche – geschlossener Wasserkreislauf, Muskelkraft erlaubt

## Idee
Ein Mensch steht in einer kleinen Anlage auf dem Balkon oder an der Fassade.
Er tritt auf einem Fahrrad (Ergometer) und erzeugt damit Antriebsenergie
(mechanisch direkt oder als Strom). Mit dieser Energie – zusammen mit Sonne
und Umgebung – wird Leitungswasser gekühlt. Danach duscht er sich mit dem
kalten Wasser ab, um sich selbst abzukühlen und an heißen Tagen nicht warm zu
sein.

## Was wir aus zwei früheren Durchläufen schon wissen
1. **Ein geschlossener Verdunsten-Kondensieren-Kreislauf auf einem Druck
   kühlt nicht.** Dampf strömt immer zur kältesten Stelle. Die
   Kondensationswärme kann nur dann an die 32 °C warme Luft abfließen, wenn
   der Kondensator wärmer als die Luft ist (z. B. ~40 °C). Also braucht der
   Kreislauf einen Druckhub zwischen Verdampfer (kalt, niedriger Druck) und
   Kondensator (warm, hoher Druck). Den liefert entweder Arbeit (Verdichter)
   oder Wärme hoher Temperatur (Sorption).
2. **Die offene Verdunstung** (nasser Lappen) schafft bei 32 °C / 40 % r. F.
   höchstens die Kühlgrenze von ~22 °C und verliert Wasser.
3. **Durchlauf 1 (verworfen):** Kompressor mit Propan (R290), ~275 W Strom
   für 50 l/h von 24 auf 12 °C. Funktioniert, verletzt aber die Vorgabe
   „nur Wasser, nichts Brennbares“. Wasserdampf direkt zu verdichten braucht
   sehr große Saugvolumina (~160 m³/h für 0,7 kW Kälte bei 6 °C), weil
   Wasserdampf bei niedrigem Druck sehr dünn ist.
4. **Durchlauf 2 (beste Lösung bisher, 7,65/10):** Solar getriebener
   Zeolith-Wasser-Adsorptionskühler im Tag-Nacht-Takt, 0 W Strom. Balkon:
   2,7 m² Kollektor, 40 kg Zeolith, ≈ 65 l/Tag von 24 auf ~11 °C (Klartag),
   ≈ 470 kg, grob 12–18 k€. Schwächen: Ertrag hängt an unbelegter
   Zeolith-Isotherme, schwache passive Nachtkühlung, heikle
   Dampf-Rückschlagklappe und hohe Dichtheitsanforderung, schwer, bei
   Bewölkung kein Ertrag, Fassadenhöhe kaum genutzt.

Nutze diese Erkenntnisse. Wiederhole die Fehler nicht, und prüfe, ob
Muskelkraft die Schwächen von Durchlauf 2 beheben kann (z. B. Pumpen,
Lüften, Vakuum halten, Dampf verdichten, Kältespeicher laden) – oder ob
eine ganz andere Lösung jetzt besser ist.

## Harte Vorgaben (nicht verhandelbar)
1. **Arbeitsmittel des Kühlkreislaufs ist ausschließlich Wasser.** Kein
   Propan, kein anderes Kältemittel, nichts Brennbares, nichts Giftiges.
   Feste, ungiftige, nicht brennbare Hilfsstoffe (Zeolith, Silikagel) sind
   erlaubt; Salzlösungen nur, wenn ungiftig und nicht brennbar, mit
   Begründung.
2. **Erlaubte Antriebe:** Sonne, Wind, Schwerkraft, Nachthimmel,
   Tag/Nacht-Wechsel und **menschliche Muskelkraft** (Fahrrad). Strom aus
   Solarmodulen an der Anlage nur, wenn es nachweislich nicht anders geht –
   dann so wenig wie möglich und ehrlich beziffert. Kein Netzstrom.
3. **Größe:** Balkon (Grundfläche ca. 1 × 3 m, Höhe bis ca. 2,5 m) oder
   Fassade eines vierstöckigen Gebäudes (Höhe ca. 12–14 m). Ein Mensch mit
   Fahrrad und Duschplatz muss hineinpassen.
4. **Der Kühlkreislauf bleibt geschlossen** (kein Verdunstungsverlust in die
   Atmosphäre). Das Duschwasser selbst ist Leitungswasser und darf ablaufen.

## Die entscheidende Frage: lohnt sich das für den Menschen?
Ein Mensch auf dem Fahrrad wandelt Nahrungsenergie nur mit etwa 20–25 %
Wirkungsgrad in mechanische Leistung um; der Rest wird Körperwärme. Rechne
ehrlich die **Wärmebilanz des Menschen** durch:
- Wie viel zusätzliche Körperwärme erzeugt das Treten?
- Wie viel Wärme nimmt die kalte Dusche dem Körper ab (Menge, Temperatur,
  Dauer, realistischer Wärmeübergang Haut/Wasser)?
- Wie viel Kälte erzeugt die Anlage pro Wattstunde Tretarbeit?
- Ist der Mensch am Ende kühler oder wärmer als ohne Treten? Unter welchen
  Bedingungen (Tretdauer, Leistung, Tageszeit, Sonne als Hilfe, Speicher)
  wird die Bilanz positiv?

Wenn die Bilanz für den Tretenden negativ ist, sag das klar und zeig die
beste Variante, die trotzdem Sinn ergibt (z. B. Kälte über den Tag sammeln
und nur kurz treten, Treten in den kühlen Morgenstunden, Kälte für eine
andere Person, Sonne als Hauptantrieb und Muskelkraft nur als Hilfe).

## Auslegungsfall (zum Rechnen)
- Sommertag, Lufttemperatur 32 °C, relative Luftfeuchte 40 %
- Sonneneinstrahlung bis 800 W/m², Wind 0–3 m/s, klarer Himmel; nachts ca. 20 °C
- Leitungswasser: Eintritt 24 °C
- Eine erwachsene Person, untrainiert bis mäßig trainiert: Dauerleistung
  ca. 75–100 W mechanisch über 30 min, kurzzeitig mehr
- Eine Dusche: ca. 30–60 Liter

## Hinweis zur Energiebilanz (JSON)
Muskelkraft modellieren als Knoten "Nahrung" (rolle "umgebung") → "Mensch"
(rolle "komponente", ca. 37 °C) mit art "arbeit" (chemische Energie). Der
Mensch gibt Arbeit an das Fahrrad/den Antrieb ab und Wärme an Luft und
Duschwasser.

Gesucht ist die bestmögliche, physikalisch korrekte und praktisch baubare
Lösung, die alle harten Vorgaben einhält und die Frage nach der Wärmebilanz
des Menschen ehrlich beantwortet.
