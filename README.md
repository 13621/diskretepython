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
- RSA verschlüsseln: Um 'DINGSBUMS' mit dem öffentlichen Schlüssel von oben zu verschlüsseln, `print(rsa.chiffrieren("DINGSBUMS ", 7, 221))`. Achtung: Wenn die Länge der Nachricht ungerade ist, muss am Ende ein Leerzeichen sein! Die nachricht muss auch großgeschrieben sein
- RSA entschlüsseln: `print(rsa.dechiffrieren([188, 11, 156], 55, 221))`
