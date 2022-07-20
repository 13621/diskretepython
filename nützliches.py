import math


import math
import sympy

def findPrim(x):
    """Findet Primzahl, die größer als der eingegebene Wert ist"""
    n = x + 1
    while not sympy.isprime(n):
        n += 1

    return n

#############################################input#############################################
print(findPrim(2474))
