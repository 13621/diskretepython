from typing import List
import math

class nomial:
    def binomial(n: int, k: int) -> int:
        return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

    def multinomial(n: int, k: List[int]) -> int:
        rt = 1
        for num in k:
            rt *= math.factorial(num)

        return math.factorial(n) / rt

# def siebformel(menge: List[int], zu_pruefen_teilbar: List[int]) -> List[int]:
#     # prinzip der in-exklusion
#     pass

def ellenbogen(checks_angabe: int):
    checks = 0
    for s in range(2, checks_angabe):
        for p in range(2, checks_angabe):
            singles = nomial.binomial(s, 2)
            singlesundpaare = 2 * s * p
            paare = nomial.binomial(2*p, 2) - p

            checks = singles + singlesundpaare + paare
            if checks == checks_angabe:
                print(f"{checks} durch {s} singles und {p} paare ({singles} singlechecks, {singlesundpaare} beideschecks, {paare} paarchecks)")
            # if (checks >= checks_angabe):
            #     return s, p

# eins = 0
# zwei = 0
# drei = 0

# for i in range(408, 5178+1):
#     if (i % 6 == 0):
#         eins += 1
#     if (i % 6 == 0) or (i % 8 == 0):
#         zwei += 1
#     if (i % 6 == 0) or (i % 8 == 0) or (i % 14 == 0):
#         drei += 1

# print(f"{eins} durch 6, {zwei} durch 6 oder 8, {drei} durch 6 oder 8 oder 14")

# print(ellenbogen(318))