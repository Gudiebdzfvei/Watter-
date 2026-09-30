# Aufgabe: Zimmer kühlen mit Muskelkraft (mechanisch) – DIY-Balkongerät, geschlossener Wasserkreislauf

## Idee
Ein Mensch sitzt **in seiner Wohnung** (im Zimmer, das gekühlt werden soll)
auf einem Fahrrad (Ergometer) und treibt damit ein selbst gebautes
**Außengerät auf dem Balkon** an, das nach dem Prinzip der Verdunstungskälte
arbeitet und das **Zimmer kühlt**. Es gibt keine Kabine draußen – der Mensch
bleibt drinnen.

**Antrieb: mechanisch ist ausdrücklich erlaubt und oft besser.** Was der
Mensch tritt, muss nicht in Strom umgewandelt werden. Die Tretbewegung darf
direkt etwas bewegen, damit die Kühlung funktioniert – z. B. über Kette,
Welle, Riemen, Seilzug oder Hydraulik eine Kolben- oder Membranpumpe, ein
Gebläse, eine Vakuumpumpe, einen Dampfverdichter antreiben, ein Gewicht
heben oder eine Feder spannen (mechanischer Speicher, der danach weiter
antreibt), Wasser hochpumpen usw. Strom (Generator) nur, wenn er klar
besser ist; Umwandlungsverluste dann mitrechnen.

**Ablauf:** Der Mensch tritt eine Runde (z. B. 20–60 min). Danach verlässt
er das Zimmer, geht ins Bad und kühlt sich dort mit normalem Leitungswasser
ab (Dusche). Die Körperwärme, die er während des Tretens im Körper
speichert und im Bad abgibt, belastet das Zimmer also nicht. Nur was er
während des Tretens im Zimmer abgibt (Wärmestrahlung, Konvektion, Schweiß
als Luftfeuchte), zählt für das Zimmer. Die Kälte kann über einen
Wasserkreislauf (Gebläsekonvektor, Kühldecke/-wand) oder einen
Kältespeicher ins Zimmer kommen und darf nach dem Treten weiter wirken.

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
   für ~0,7 kW Kälte. Funktioniert, verletzt aber die Vorgabe „nur Wasser,
   nichts Brennbares“. Wasserdampf direkt zu verdichten braucht sehr große
   Saugvolumina (~160 m³/h für 0,7 kW Kälte bei 6 °C), weil Wasserdampf bei
   niedrigem Druck sehr dünn ist.
4. **Durchlauf 2 (beste Lösung bisher, 7,65/10):** Solar getriebener
   Zeolith-Wasser-Adsorptionskühler im Tag-Nacht-Takt, 0 W Strom. Balkon:
   2,7 m² Kollektor, 40 kg Zeolith, ≈ 1 kWh Kälte pro Klartag (≈ 41 W im
   Mittel), ≈ 470 kg, grob 12–18 k€. Schwächen: Ertrag hängt an unbelegter
   Zeolith-Isotherme, schwache passive Nachtkühlung, heikle
   Dampf-Rückschlagklappe, schwer, bei Bewölkung kein Ertrag. Außerdem
   **nicht selbst baubar**: vollgeschweißter Edelstahl-Vakuumaufbau mit
   Helium-Lecktest, Sonderklappen, Dichtheit ≤ 5·10⁻⁸ mbar·l/s.

Nutze diese Erkenntnisse. Wiederhole die Fehler nicht, und prüfe, ob
Muskelkraft die Schwächen von Durchlauf 2 beheben kann (z. B. Dampf
verdichten, Vakuum halten, Pumpen, Lüften, Kältespeicher laden) – oder ob
eine ganz andere Lösung jetzt besser ist.

## Harte Vorgaben (nicht verhandelbar)
1. **Arbeitsmittel des Kühlkreislaufs ist ausschließlich Wasser.** Kein
   Propan, kein anderes Kältemittel, nichts Brennbares, nichts Giftiges.
   Feste, ungiftige, nicht brennbare Hilfsstoffe (Zeolith, Silikagel) sind
   erlaubt; Salzlösungen nur, wenn ungiftig und nicht brennbar, mit
   Begründung.
2. **Erlaubte Antriebe:** **menschliche Muskelkraft** (Fahrrad in der
   Wohnung), Sonne, Wind, Schwerkraft, Nachthimmel, Tag/Nacht-Wechsel.
   Strom aus Solarmodulen am Balkon nur, wenn es nachweislich nicht anders
   geht – dann so wenig wie möglich und ehrlich beziffert. Kein Netzstrom.
3. **Außengerät nur auf dem Balkon.** Grundfläche ca. 1 × 3 m, Höhe bis
   ca. 2,5 m, Brüstung und Wand nutzbar. Gewicht betriebsbereit angeben und
   begründen, dass ein normaler Wohnungsbalkon es trägt. Verbindung in die
   Wohnung durch Fenster, Balkontür oder eine kleine Wanddurchführung.
4. **Selbst baubar (DIY).** Ein handwerklich geschickter Laie muss die
   Anlage selbst bauen können:
   - Teile aus Baumarkt, Sanitär-/Heizungshandel, Fahrrad- oder
     Elektronikbedarf oder gängigen Online-Shops; keine Sonderanfertigungen,
     die nur Industriebetriebe herstellen können.
   - Werkzeug für Heimwerker (Bohrmaschine, Rohrschneider, Pressfitting-
     oder Lötzange, ggf. einfache Vakuumpumpe aus dem Klimatechnik-Bedarf);
     kein Orbitalschweißen, keine Helium-Lecksuche, keine Druckbehälter-
     Abnahme.
   - Keine gefährlichen Drücke, Temperaturen oder Spannungen für Laien;
     Sicherheitsrisiken beim Selbstbau klar benennen.
   - Eine Stückliste mit ungefähren Preisen und eine Bauanleitung in
     Schritten mitliefern. Budget möglichst niedrig, ehrlich beziffert.
   - Wenn ein Bauteil für DIY zu heikel ist (z. B. dauerhaft dichtes
     Vakuum), eine einfachere Alternative wählen oder zeigen, wie man es mit
     Hausmitteln prüft und nachbessert.
5. **Der Kühlkreislauf bleibt geschlossen** (kein Verdunstungsverlust in die
   Atmosphäre).

## Die entscheidende Frage: wird das Zimmer wirklich kühler?
Der Mensch wandelt Nahrungsenergie nur mit etwa 20–25 % Wirkungsgrad in
mechanische Leistung um; der Rest (das 3- bis 4-Fache der Tretleistung)
wird Körperwärme. Ein Teil davon geht während des Tretens ins Zimmer
(Konvektion, Strahlung, verdunsteter Schweiß), ein Teil wird im Körper
gespeichert (Körpertemperatur steigt) und im Bad mit Leitungswasser
abgeführt. Rechne ehrlich:
- Wie viel Wärme gibt der Tretende während der Runde an das Zimmer ab
  (fühlbar und latent), wie viel nimmt er mit ins Bad? Mit realistischen
  Werten (Speicherfähigkeit des Körpers, zumutbarer Anstieg der
  Körpertemperatur, Schweißrate) – nicht schönrechnen.
- Wie viel Kälte liefert das Gerät pro Wattstunde Tretarbeit (inkl. aller
  Verluste: Mechanik, Pumpe/Verdichter, Lüfter)? Wirkt ein mechanischer
  oder Kältespeicher nach, wenn der Mensch schon im Bad ist?
- Welche Leistungszahl ist mindestens nötig, damit dem Zimmer über den
  ganzen Ablauf (Treten + Nachwirkzeit) netto Wärme entzogen wird?
  Erreicht das Gerät sie?
- Um wie viel wird das Zimmer kühler als ohne Gerät, bei welcher Tretdauer
  und wie oft am Tag?

Wenn die Bilanz negativ ist, sag das klar und zeig die beste Variante, die
trotzdem Sinn ergibt (z. B. Treten in den kühlen Nachtstunden und Kälte
speichern, Sonne als Hauptantrieb und Muskelkraft nur als Hilfe,
mehrere kurze Runden).

## Auslegungsfall (zum Rechnen)
- Sommertag, Außenluft 32 °C, relative Luftfeuchte 40 %
- Sonneneinstrahlung bis 800 W/m², Wind 0–3 m/s, klarer Himmel; nachts ca. 20 °C
- Ein Raum mit 15–25 m² (z. B. Schlaf- oder Wohnzimmer); Wärmelast an einem
  heißen Tag selbst begründet abschätzen. Ziel: spürbar kühler als ohne
  Gerät, idealerweise ≤ 26 °C
- Eine erwachsene Person, untrainiert bis mäßig trainiert: Dauerleistung
  ca. 75–100 W mechanisch über 20–60 min pro Runde, kurzzeitig mehr;
  realistisch 1–3 Runden pro Tag, danach jeweils Dusche im Bad

## Hinweis zur Energiebilanz (JSON)
- Die Wohnung ist der Nutz-Knoten: `"nutzen": {"knoten": "Wohnung", "T_ein_C":
  <Raumtemperatur ohne Gerät>, "T_aus_C": <Raumtemperatur mit Gerät>,
  "kuehlleistung_W": <netto>}`; die Wohnung als rolle "umgebung".
- Muskelkraft: Knoten "Nahrung" (rolle "umgebung") → "Mensch" (rolle
  "komponente", ca. 37 °C) mit art "arbeit" (chemische Energie). Der Mensch
  gibt Arbeit an den Antrieb ab, Körperwärme als "waerme" an die
  **Wohnung** (nur der Anteil während des Tretens im Zimmer) und den Rest an
  einen Knoten "Bad" (rolle "umgebung", Leitungswasserdusche). Der
  automatische Prüfer rechnet nach, ob der Wohnung netto Wärme entzogen
  wird – die im Zimmer abgegebene Körperwärme zählt dabei mit.
- Bilanz als Mittel über die Tretzeit oder über 24 h, klar angeben.

Gesucht ist die bestmögliche, physikalisch korrekte und selbst baubare
Lösung, die alle harten Vorgaben einhält und die Frage nach der
Wärmebilanz der Wohnung ehrlich beantwortet.
