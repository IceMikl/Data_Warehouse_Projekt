This small project is a homework for "Übungsprojekt" from lecture "Data Warehousing 2019".
Theme of project is "ETL: Deduplication", it will read file RestaurantNames.txt and with different
methods analyse and deduplicate entities.

   Teilaufgabe 1:
Programm besteht aus zwei Klassen:
- Main: da werden die daten aus RestaurantNames.txt gelesen, Ähnlichkeitsmatrix erstellt.
- EditDistance: da wird iterative levenstein distance algorithm implementiert.

   Teilaufgabe 2:
Es werden die Schwellwerte von 1 bis 5 ausprobiert, die Ergebnissen werden in die Ausgabedatein geschreiben
und dann analysiert.
Für Schwellwert kleiner gleich:
- 5: