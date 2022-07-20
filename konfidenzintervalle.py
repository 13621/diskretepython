#Übersicht: Skript Seite 69

import scipy.stats
import math
import kennwerteStichproben

def binomialConfidenceP(x, n, y):    
    """x = Anzahl der Erfolge; n = Anzahl der Durchführungen des Bernoulli-Experiments"""
    p = x/n
    print(f"Schätzwert p' = x/n = {p}                                     | Maximum-Likelihood-Schätzfunktion", end ="\n\n")

    test = round(n*p*(1-p),5)

    if test >= 9:
        print(f"n*p'*(1-p') = {test} >= 9   --> hinreichende Bedingung erfüllt", end ="\n\n")
    else:
        print(f"n*p'*(1-p') = {test} >= 9   --> hinreichende Bedingung NICHT erfüllt", end ="\n\n")
        exit()

    print(f"U = (X - μ(x)) / (σ(x)) = (n*p' - n*p) / (sqrt(n*p*(1-p)))      | μ(x)...Erwartungswert; σ(x)...Standardabweichung; U ist standardnormalverteilt", end ="\n\n")

    print(f"P(-c <= U <= c) = γ = {y}                                      | γ... Konfidenzniveau", end ="\n\n")

    print(f"P(-c <= ((X - μ(x)) / (σ(x)) = (n*p' - n*p) / (sqrt(n*p*(1-p)))) <= c) = γ", end ="\n\n")

    print(f"P(U<=c) = (1 + γ)/ 2 = {round((1+y)/2, 5)}                                    | gesucht: c --> (1+γ)/2-Quantil der Standardnormalverteilung", end ="\n\n")

    c = round(scipy.stats.norm.ppf((1 + y)/ 2),5)
    print(f"c = {c}                                                     | -c <= U <= c umstellen, bis p allein in der Mitte ist und p durch p' ersetzen", end ="\n\n")

    print(f"p' - (c/n) * sqrt(n*p'*(1-p')) <= p <= p' + (c/n) * sqrt(n*p'*(1-p'))", end ="\n\n")

    print(f"{round(p - (c/n) * math.sqrt(n*p*(1-p)),5)} <= p <= {round(p + (c/n) * math.sqrt(n*p*(1-p)),5)}", end ="\n\n")

def normalConfidenceMy(stichprobe:list, y):
    """stichprobe = Liste mit Stichprobenwerten; y = Konfidenzniveau"""
    n = len(stichprobe)

    mittelwert = round(kennwerteStichproben.mittelwert(stichprobe),5)
    
    print(f"\nSchätzwert μ' = Mittelwert = (Summe über alle x(i)) / n = {mittelwert}")

    sigma = round(kennwerteStichproben.standardabweichung(stichprobe),5)

    print(f"Schätzwert σ' = s = (Summe über (x(i) - mittelwert)²) / (n-1) = {sigma}", end = "\n\n")

    print(f"U = (mittelwert - μ(mittelwert)) / σ(mittelwert) = (mittelwert - μ') / (σ / sqrt(n))")
    print(f"U...zu Mittelwert gehörige standardnormalvert. ZG; Problem: σ unbekannt --> ersetzen durch σ' bzw. s --> Student-T-Vert.", end = "\n\n")

    print(f"T = (mittelwert - μ') / (s / sqrt(n))", end = "\n\n")

    print(f"P(-c <= T <= c) = γ = {y}                                         | γ... Konfidenzniveau", end = "\n\n")

    print(f"P(-c <= (mittelwert - μ) / (s / sqrt(n)) <= c) = γ", end = "\n\n")

    print(f"P(T <= c) = (1 + γ)/ 2 = {round((1 + y)/ 2, 5)}                                     | gesucht: c --> (1+γ)/2-Quantil der Student-T-Verteilung mit f = n-1 = {n-1}", end ="\n\n")

    c = round(scipy.stats.t.ppf((1+y)/2, n-1),5)

    print(f"c = {c}                                                        | -c <= T <= c umstellen, bis μ allein in der Mitte ist", end = "\n\n")

    print(f"mittelwert - c * (s/sqrt(n)) <= μ <= mittelwert + c * (s/sqrt(n))", end = "\n\n")

    print(f"{mittelwert - c * (sigma/math.sqrt(n))} <= μ <= {mittelwert + c * (sigma/math.sqrt(n))}")

def normalConfidenceSigma(stichprobe:list, y):
    """stichprobe... Liste mit Stichprobenwerten; y... Konfidenzniveau"""
    n = len(stichprobe)

    mittelwert = round(kennwerteStichproben.mittelwert(stichprobe),5)
    
    print(f"\nSchätzwert μ' = Mittelwert = (Summe über alle x(i)) / n = {mittelwert}")

    sigma = round(kennwerteStichproben.standardabweichung(stichprobe),5)

    print(f"Schätzwert σ' = s = (Summe über (x(i) - mittelwert)²) / (n-1) = {sigma}", end = "\n\n")
    
    print(f"\nZ = (n - 1)*(s²/σ²)                                  | Chi-Quadrat-verteilt mit f = n-1 = {n-1} Freiheitsgraden", end = "\n\n")
    
    print(f"P(c1 <= Z <= c2) = γ = {y}                          | γ... Konfidenzniveau", end = "\n\n")

    print(f"P(c1 <= (n - 1)*(s²/σ²) <= c2) = γ", end = "\n\n")

    print(f"P(Z <= c1) = (1 - γ)/ 2 = {round((1 - y)/ 2, 5)}                      | gesucht: c1 --> (1-γ)/2-Quantil der Chi-Quadrat-Verteilung mit f = n-1 = {n-1}")
    print(f"P(Z <= c2) = (1 + γ)/ 2 = {round((1 + y)/ 2, 5)}                      | gesucht: c2 --> (1+γ)/2-Quantil der Chi-Quadrat-Verteilung mit f = n-1 = {n-1}", end ="\n\n")

    c1 = round(scipy.stats.chi2.ppf((1 - y)/ 2, n-1),5)
    c2 = round(scipy.stats.chi2.ppf((1 + y)/ 2, n-1),5)
    print(f"c1 = {c1}      c2 = {c2}                      | c1 <= Z <= c2 umstellen, bis σ bzw. σ² allein in der Mitte ist", end = "\n\n")

    print(f"((n-1) * s²) / c2 <= σ² <= ((n-1) * s²) / c1", end = "\n\n")

    print(f"{round(((n-1)*sigma*sigma)/c2, 5)} <= σ² <= {round(((n-1)*sigma*sigma)/c1, 5)}", end = "\n\n")
    print("bzw.", end = "\n\n")
    print(f"{round(math.sqrt(((n-1)*sigma*sigma)/c2),5)} <= σ <= {round(math.sqrt(((n-1)*sigma*sigma)/c1),5)}", end = "\n\n")

##########################################################input#########################################################

#binomialConfidenceP(90, 1200, 0.99)

#normalConfidenceMy([65,69,71,66,61,72,71,69,73,62,59,63,62,60,68,63], 0.95)

#normalConfidenceSigma([65,69,71,66,61,72,71,69,73,62,59,63,62,60,68,63], 0.95)





