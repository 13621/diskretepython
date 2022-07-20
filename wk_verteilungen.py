import scipy.special
import scipy.stats
import math

# Binomialverteilung
def binomialX(x, n, p):
    '''Parameter: x... Wert für zu berechnende WK; n... Stichprobenumfang; p... Erfolgswahrscheinlichkeit'''
    print("Binomialverteilung: P(X=x) = binom(n,x) * p^x * (1-p)^(n-x) für 0 <= x <= n, sonst 0")

    if 0<=x<=n:
        return round(scipy.special.binom(n,x) * p**x * (1-p)**(n-x) , 5)
    else:
        return 0

def binomialLowerAndEqualX(n, p, x):
    '''Parameter: x... Wert für zu berechnende WK; n... Stichprobenumfang; p... Erfolgswahrscheinlichkeit'''
    print("Binomialverteilung: P(X <= x) = Summe über alle x (binom(n,x) * p^x * (1-p)^(n-x) für 0 <= x <= n, sonst 0)")

    sum = 0
    for i in range(0,x+1):
        if 0<=x<=n:
            sum += round(scipy.special.binom(n,i) * p**i * (1-p)**(n-i) , 5)

    return round(sum, 5)

def binomialXList(n, p, x:list):
    '''Parameter: x als Liste... Werte für zu berechnende WK; n... Stichprobenumfang; p... Erfolgswahrscheinlichkeit'''
    print("Binomialverteilung: P(X <= x) = binom(n,x) * p^x * (1-p)^(n-x) für 0 <= x <= n, sonst 0")

    result = []
    if 0<=x<=n:
        result.append(round(scipy.special.binom(n,x) * p**x * (1-p)**(n-x) , 5))
    else:
        result.append(0)

    return result

# Normalverteilung
def normalLowerAndEqualX(x, my, sigma):
    """Parameter: x... Wert zur Berechnung der WK; my... Erwartungswert; sigma... Standardabweichung"""
    print("Normalverteilung muss erst auf Standardnormalverteilung gebracht werden: U = (X-μ) / σ")
    u = (x-my / sigma)
    print(f"P(X <= x) = P(U <= U(x) = P(U <= ({x}-μ) / σ) = P(U <= ({x}-{my}) / {sigma}) = P(U<={u}) = Φ({u})") 

    return scipy.stats.norm.pdf(u)

# Hypergeometrische
def hypergeometricX(N, M, n, x):
    '''Parameter: N... Anzahl an Gegenständen; M... Anzahl an Gegenständen mit "Erfolg"; n... Anzahl der Durchführungen; x... Wert für die zu berechnende WK'''
    print("Hypergeometrische Verteilung: P(X=x) = (binom(M,x) * binom(N-M, n-x)) / binom(N,n)")
    return round((scipy.special.binom(M,x) * scipy.special.binom(N-M, n-x)) / scipy.special.binom(N,n), 6)

def hypergeometricLowerAndEqualX(N, M, n, x):
    '''Parameter: N... Anzahl an Gegenständen; M... Anzahl an Gegenständen mit "Erfolg"; n... Anzahl der Durchführungen; x... Wert für die zu berechnende WK'''
    print("Hypergeometrische Verteilung: P(X<=x) = Summe über alle x ((binom(M,x) * binom(N-M, n-x)) / binom(N,n))")
    result = 0
    for i in range(0,x+1):
        result += round((scipy.special.binom(M,i) * scipy.special.binom(N-M, n-i)) / scipy.special.binom(N,n), 6)
    return result

def hypergeometricXList(N, M, n, x:list):
    '''Parameter: N... Anzahl an Gegenständen; M... Anzahl an Gegenständen mit "Erfolg"; n... Anzahl der Durchführungen; x als Liste... Werte für die zu berechnenden WK'''
    print("Hypergeometrische Verteilung: P(X=x) = (binom(M,x) * binom(N-M, n-x)) / binom(N,n)")
    result = []

    for i in x:
        result.append(round((scipy.special.binom(M,i) * scipy.special.binom(N-M, n-i)) / scipy.special.binom(N,n),6))
    return result

# Geometrische Verteilung:
def geometricX(x, p):
    """Parameter: x... Wert zur Berechnung der WK; p... Erfolgswahrscheinlichkeit"""
    print("Geometrische Verteilung: P(X=x) = p*((1-p)^(x-1)) für x>0; sonst 0")

    if x > 0:
        return round(p*((1-p)**(x-1)), 5)
    else:
        return 0
    
def geometricLowerAndEqualX(x, p):
    """Parameter: x... Wert zur Berechnung der WK; p... Erfolgswahrscheinlichkeit"""
    print("Geometrische Verteilung: P(X<=x) = Summe über alle x (1 - (1 - p)^x)")
    return 1-(1-p)**x

def geometricXList(x:list, p):
    """Parameter: x... Wert zur Berechnung der WK; p... Erfolgswahrscheinlichkeit"""
    print("Geometrische Verteilung: P(X<=x) = p*((1-p)^(x-1)) für x>0; sonst 0")
    
    result = []
    
    for i in x:
        if i > 0:
            result.append(round(p*((1-p)**(i-1)), 5))
        else:
            result.append(0)

    return result

# Poisson-Verteilung:
def poissonX(x, y):
    '''Parameter: x... Wert für zu berechnende WK; y... lambda = n*p'''
    print("Poisson-Verteilung: λ = n*p --> P(X=x) = ((λ^x) / fakultät(x)) * exp(-λ) für x >= 0, sonst 0")
    
    if x >= 0:
        return round(((y**x) / math.factorial(x)) * math.exp(-y), 5)
    else:
        return 0 

def poissonLowerAndEqualX(x, y):
    '''Parameter: x... Wert für zu berechnende WK; y... lambda = n*p'''
    print("Poisson-Verteilung: λ = n*p --> P(X<=x) = Summe über alle x (((λ^x) / fakultät(x)) * exp(-λ) für x >= 0, sonst 0)")
    
    sum = 0
    for i in range (0,x+1):
        if x >= 0:
            sum += round(((y**i) / math.factorial(i)) * math.exp(-y), 5)

    return round(sum, 5)

def poissonXList(x:list, y):
    '''Parameter: x als Liste... Werte für zu berechnende WK; y... lambda = n*p'''
    print("Poisson-Verteilung: λ = n*p --> P(X=x) = ((λ^x) / fakultät(x)) * exp(-λ) für x >= 0, sonst 0")
    
    result = []
    for i in x:
        if i >= 0:
            result.append(round(((y**i) / math.factorial(i)) * math.exp(-y), 5))
        else:
            result.append(0)

    return result

#Benfordsche Verteilung
def benfordX(x):
    '''Parameter: x... Werte zur Berechnung der WK'''
    print("Benfordsche Verteilung: P(X=x) = log10(1 + 1/z) ==> da für Ziffern nur für 1<=x<=9 sinnvoll")
    return math.log(1+(1/x),10)

#################################################input##########################################################
#print(binomialX(50, 0.42, 25))

#print(binomialLowerAndEqualX(50, 0.42, 25))

#print(binomialXList(50, 0.42, [24,25,26,27]))

#print(hypergeometricX(48, 8, 12, 0))

#print(hypergeometricLowerAndEqualX(48, 8, 12, 4))

#print(hypergeometricXList(48, 8, 12, [0,1,2,3,4,5,6,7,8]))

#print(poissonX(5, 6))

#print(poissonLowerAndEqualX(5, 6))

#print(poissonXList([5,6,7,8], 6))

#print(normalLowerAndEqualX(5.326, 6, 1))

#print(geometricX(5, 0.3))

#print(geometricLowerAndEqualX(5, 0.3))

#print(geometricXList([5,6,7,8], 0.3))

#print(benfordX(4))