# diskretepython
## Verwendung
### Zahlentheorie
- Euklidischer Algorithmus: In `diskrete_python.py` zum Beispiel für den ggT(7, 28) `print(euklidalgos.euklid(7, 28)` eingeben. Der Rechenweg wird ausgegeben.
- Erweiterter Euklid: In `diskrete_python.py` z.B. `print(euklidalgos.erweuklid(7, 28))` eingeben
### Kombinatorik
- Im Bild https://github.com/13621/diskretepython/blob/1bc11bff9a69884ec9761acf4d9619d913db7fcf/kombinatorik_entscheidungsbaum.png stehen die generellen Formeln
### Kryptographie
- Caesar: In `diskrete_python.py` z.B. um 'abc' um 1 zu verschieben `print(symmetric.caesar("abc", 1))` eingeben. Der Rechenweg wird ausgegeben
- Vigenere: In `diskrete_python.py` z.B. um 'trytotakeovertheworld' mit dem Schlüssel 'brain' zu verschlüsseln, `print(symmetric.vigenere("trytotakeovertheworld", "brain"))` eingeben. Rechenweg auch hier
- One Time Pad: In `diskrete_python.py` den Vigenere mit einem gleich langen Schlüssel aufrufen, also z.B. `print(symmetric.vigenere("dings", "brain"))`
- RSA public key: Für Primzahlen 13 und 17 und e=9 `print(rsa.publickey(13, 17, 9))`. Die Funktion sucht nach einem neuen e und benutzt den, falls das eingegebene e nicht funktioniert. Ausgabe: (e, N)
- RSA private key: `print(rsa.publickey(13, 17, 9))` für gleiches Beispiel wie oben. Ausgabe: (d, N)
- RSA verschlüsseln: Um 'DINGSBUMS' mit dem öffentlichen Schlüssel von oben zu verschlüsseln, `print(rsa.chiffrieren("DINGSBUMS ", 7, 221))`
  - <b>Achtung:</b> Wenn die Länge der Nachricht ungerade ist, muss am Ende ein Leerzeichen sein! Die nachricht muss auch großgeschrieben sein
- RSA entschlüsseln: `print(rsa.dechiffrieren([188, 11, 156], 55, 221))`
### Chi-Quadrat-Test
- um zum Input zu gelangen, in `chi-quadrat.py` ganz nach unten scrollen und dort ist es dann kommentiert
- zu den Variablen:
  - `classes` (Liste) enthält einfach nur die Klassen der zu testenden Stichprobe (z.B. Würfelaugen etc.) 
  - `prevalences` (Liste) enthält die zu den einzelnen Klassen gegebenen absoluten Häufigkeiten (z.B. 22-mal die 1 geworfen); Reihenfolge passend zu `classes` beachten!
  - `probabilities` (Liste) enthält die theoretischen Wahrscheinlichkeit, der Verteilung, auf die getestet werden soll. Um die Liste zu erstellen können die vorgefertigten Funktionen in `wk-verteilungen.py` genutzt werden (z.B. `hypergeometricXList(...)` --> siehe unten)
   - sollte die Verteilung nicht implementiert sein, kann die Liste natürlich auch manuell an der Stelle gefüllt werden mit `append()`
 - zum Ausführen dann einfach `chiSquareTest(...)` nutzen
  - Erklärungen zu Übergabeparametern sind in der Definition der Funktion (in VS-Code Rechtklick) zu finden 
