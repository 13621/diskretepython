import math

def mittelwert(stichprobe:list):
    return sum(stichprobe)/len(stichprobe)

def median(stichprobe:list):
    return quantil(stichprobe,0.5)

def range(stichprobe:list):
    return max(stichprobe) - min(stichprobe)

def varianz(stichprobe:list):  #mit Quadrat
    result = 0
    for i in stichprobe:
        result = result + (i - mittelwert(stichprobe)) * (i - mittelwert(stichprobe))
    
    return result/(len(stichprobe)-1)

def standardabweichung(stichprobe:list):   #ohne Quadrat
    return math.sqrt(varianz(stichprobe))

def quantil(stichprobe:list, q):
    stichprobe.sort()
    n = len(stichprobe)*q

    if n % 1 == 0:
        return (stichprobe[int(n-1)] + stichprobe[int(n)]) / 2
    else:
        return stichprobe[int(n)]

def variationskoeffizient(stichprobe:list):
    return (standardabweichung(stichprobe) / mittelwert(stichprobe))*100

#Umrechnung absolute/relative Häufigkeit
def absoluteToRelative(stichprobe:list):
    result = []

    for i in stichprobe:
        result.append(round(i/sum(stichprobe),5))
    
    return result

def relativeToAbsolute(stichprobe:list, n):
    result = []

    for i in stichprobe:
        result.append(round(i * n, 0))

    return result