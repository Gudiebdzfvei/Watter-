# Aufgabe: Zimmer mit kaltem Leitungswasser kühlen – möglichst nur drinnen, selbst gebaut

## Idee
Statt Kälte draußen selbst zu erzeugen, wird das **kalte Wasser aus der
Leitung** als Kältequelle genutzt. Vielleicht muss draußen gar nichts gebaut
werden, und die Kühlung passiert komplett **in der Wohnung**. Gesucht ist,
**wie** man damit ein Zimmer am besten kühlt.

## Was wir aus drei früheren Durchläufen schon wissen
1. **Ohne kältere Senke oder Antrieb gibt es keine Kühlung unter
   Außentemperatur.** Ein geschlossener Verdunsten-Kondensieren-Kreislauf
   braucht einen Druckhub; mit Wasser als Arbeitsmittel ist das im Selbstbau
   kaum machbar (Wasserdampf-Verdichter braucht Vakuum und riesige
   Saugvolumina, Zeolith-Sorption braucht Industrie-Vakuumtechnik).
2. **Muskelkraft lohnt sich als Kältequelle nicht:** Beim Treten entsteht das
   3- bis 4-Fache der Tretleistung als Körperwärme; ein Selbstbau-Gerät
   erreicht die nötige Leistungszahl von ≈ 2–3 nicht.
3. **Nachthimmel-Strahler** (Durchlauf 3) bringt ≈ 0,9 kWh Kälte pro klarer
   Nacht, im Mittel ≈ −1,6 K im Zimmer, ≈ 1.700 €, nur bei klarem Himmel.
4. **Nachtlüftung und Außenverschattung** sind oft wirksamer als jedes
   Wassergerät und sollten als Basis mitgedacht werden.
5. **Neu hier:** Leitungswasser ist bereits eine kältere Senke (typisch
   12–18 °C). Damit entfällt das Druckhub-Problem – es braucht keine
   Kältemaschine, nur einen guten Wärmetauscher.

## Vorgaben
1. **Kältequelle ist kaltes Leitungswasser.** Zusätzlich erlaubt: Sonne,
   Nachtluft, Nachthimmel, Muskelkraft. Strom möglichst gar nicht; falls ein
   kleiner Lüfter oder eine kleine Pumpe klar hilft, höchstens wenige Watt,
   ehrlich beziffert und begründet.
2. **Möglichst alles drinnen.** Draußen nur, wenn es klar besser ist –
   dann auf dem Balkon (ca. 1 × 3 m), mit Begründung.
3. **Nichts Brennbares, nichts Giftiges.** Nur Wasser als Kühlmedium.
4. **Selbst baubar (DIY)** mit Teilen aus Baumarkt, Sanitär-/Heizungshandel
   oder Online-Shops; Heimwerker-Werkzeug. Stückliste mit Preisen und
   Bauanleitung in Schritten. Budget möglichst niedrig.
5. **Trinkwasser-Sicherheit:** Die Trinkwasserinstallation darf nicht
   verunreinigt werden (Rückfluss, Stagnation, Erwärmung der
   Kaltwasserleitung, Legionellen). Wie wird das sicher angeschlossen?
6. **Wasser nicht verschwenden.** Wie viele Liter Leitungswasser pro Tag
   werden gebraucht, was kostet das (Wasser + Abwasser, ca. 4–5 €/m³), und
   wie wird das erwärmte Wasser **sinnvoll weiterverwendet** (z. B.
   Toilettenspülung, Duschen, Waschmaschine, Pflanzen) statt einfach
   weggeschüttet? Rechtliche Hinweise (Mietwohnung, kommunale
   Einschränkungen bei Trockenheit) kurz nennen.

## Wichtige Detailfragen
- **Kondensation:** Wasser mit 12–18 °C liegt unter dem Taupunkt der
  Zimmerluft (bei 28 °C / 50 % r. F. ≈ 17 °C). Tropft es? Wohin mit dem
  Kondenswasser? Ist die Entfeuchtung sogar ein Vorteil (Schwüle)?
- **Wärmeübertragung ohne Strom:** Reicht natürliche Konvektion (Heizkörper,
  Kühldecke, Kühlwand), oder braucht es einen Lüfter? Wie viel W bei welcher
  Fläche und Temperaturdifferenz?
- **Wie viel Kühlung pro Liter?** Wasser von 15 auf z. B. 22 °C erwärmt nimmt
  ≈ 8 Wh pro Liter auf – rechne, wie viel Wasser für eine spürbare
  Absenkung nötig ist.
- Lohnt ein **Speicher** (Wasser tagsüber gesammelt, nachts erneuert) oder
  lieber ein **kleiner Dauerdurchfluss**?

## Auslegungsfall (zum Rechnen)
- Außenluft tagsüber 30 °C, nachts ca. 18–20 °C, sonniger Sommertag
- Leitungswasser kalt: 15 °C (Empfindlichkeit für 12 °C und 20 °C zeigen;
  Leitungen im Haus können sich im Sommer erwärmen – Vorlaufen lassen?)
- Ein Zimmer mit 15–25 m²; Wärmelast selbst begründet abschätzen
- Ziel: spürbar kühler als ohne Gerät, idealerweise ≤ 26 °C

## Hinweis zur Energiebilanz (JSON)
- Die Wohnung ist der Nutz-Knoten (rolle "umgebung"):
  `"nutzen": {"knoten": "Wohnung", "T_ein_C": <ohne Gerät>, "T_aus_C": <mit
  Gerät>, "kuehlleistung_W": <netto>}`; `"luft_T_C": 30`.
- Das Leitungswasser als Knoten "Leitungswasser" (rolle "umgebung",
  Zulauftemperatur ≈ 15 °C). Die Wärme, die das durchfließende Wasser
  aufnimmt und mitnimmt, als "waerme" vom Kühler (Komponente, mittlere
  Wassertemperatur) zum Knoten "Leitungswasser".
- `"wasserverlust_l_pro_tag"` meint nur Wasser, das **in die Luft
  verdunstet**; das durchfließende Leitungswasser zählt nicht dazu. Gib den
  Leitungswasserverbrauch zusätzlich im Text an.
- Bilanz als 24-h-Mittel oder für die Betriebszeit, klar angeben.

Gesucht ist die bestmögliche, physikalisch korrekte, sichere und selbst
baubare Lösung, die ehrlich sagt, wie viel sie bringt und wie viel Wasser
sie kostet.
