class euklidalgos:
    def euklid(a: int, b: int, prnt: bool = True) -> int:
        if (a == 0):
            return abs(b)
        elif (b == 0):
            return abs(a)

        while (b != 0):
            r = a % b
            if (prnt):
                print(f"{a} = {a//b} * {b} + {r}")
            a = b
            b = r
        return abs(a)

    def erweuklid(a: int, b: int, prnt:bool = True):
        if (b == 0):
            return a, 1, 0

        d2, s2, t2, = euklidalgos.erweuklid(b, a % b, prnt)
        d, s, t = d2, t2, s2 - (a//b) * t2
        if prnt:
            print(f"{d} = {s} * {a} + {t} * {b} = {d2} {t2} ({s2} - {a//b} * {t2})")
        return d, s, t
        #ggt=d, afaktor=s, bfaktor=t
        #ggt=d, multiplikativinverse=s

class diophantisch:
    def diophantisch_durch_probieren(afaktor: int, bfaktor: int, ergebnis: int, prnt:bool = True) -> int:
        counter = 0
        konstanten = []
        kfaktoren = []
        for i in range(ergebnis):
            for j in range(ergebnis):
                if (i*afaktor + j*bfaktor == ergebnis):
                    if prnt:
                        print(f"({counter}) {i}*{afaktor} + {j}*{bfaktor} = {ergebnis}")
                    if counter == 0:
                        # k = 0, das sind unsere konstanten
                        konstanten.append(i)
                        konstanten.append(j)
                    if counter == 1:
                        # jetzt können wir gucken wie die kfaktoren sind
                        kfaktoren.append( i - konstanten[0] )
                        kfaktoren.append( j - konstanten[1] )

                    counter += 1

        if prnt:
            print(f"Ergebnis: a = {kfaktoren[0]}k + {konstanten[0]}; b = {kfaktoren[1]}n + {konstanten[1]}\nAlso: {afaktor} * ({kfaktoren[0]}k + {konstanten[0]}) + {bfaktor} * ({kfaktoren[1]}n + {konstanten[1]}) = {ergebnis}")
        return counter

def multiplikativinverse(a, b, prnt: bool = False) -> int:
    return euklidalgos.erweuklid(a, b, prnt)[1]

def ggT(a, b, prnt: bool = False) -> int:
    return euklidalgos.euklid(a, b, prnt)
