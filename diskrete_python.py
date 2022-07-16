from euklid import euklidalgos, diophantisch
from chiffren import symmetric, rsa
from kombinatorik import nomial

# print(euklidalgos.erweuklid(128, 34, True))
# print(euklidalgos.euklid(128, 34, True))

# print(symmetric.vigenere("dingsbums", "tisch", True))

# print(euklidalgos.erweuklid(9, 4, True))

# print(diophantisch.diophantisch_durch_probieren(5, 45, 210))

# print(rsa.dechiffrieren([31, 33, 1, 72, 76], 5, 91 ))

# print(rsa.privatekey(7, 13, 29, True))

# print(symmetric.vigenere("hallo", "dings"))
# print(symmetric.vigenere("adieu", "kfqnm"))

# print(nomial.multinomial(23, [6, 6, 4, 7]))

# print(diophantisch.diophantisch_durch_probieren(4, 7, 317))

print(rsa.privatekey(13, 17, 9, True))

print(rsa.publickey(13, 17, 9, True))

print(symmetric.vigenere("trytotakeovertheworld", "brain"))

print(symmetric.caesar("abc", 1))