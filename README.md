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
