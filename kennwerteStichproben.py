import math

class stichprobe:
    def __init__(self, stichprobe: list) -> None:
        self.stichprobe = stichprobe

    def mittelwert(self):
        return sum(self.stichprobe)/len(self.stichprobe)

    def median(self):
        return self.quantil(0.5)

    def range(self):
        return max(self.stichprobe) - min(self.stichprobe)

    def varianz(self):  #mit Quadrat
        result = 0
        mw = self.mittelwert()
        for i in self.stichprobe:
            result += (i - mw) ** 2
        
        return result/(len(self.stichprobe)-1)

    def standardabweichung(self):   #ohne Quadrat
        return math.sqrt(self.varianz())

    def quantil(self, q):
        stichsorted = sorted(self.stichprobe)
        n = len(stichsorted)*q

        if n % 1 == 0:
            return (stichsorted[int(n-1)] + stichsorted[int(n)]) / 2
        else:
            return stichsorted[int(n)]

    def variationskoeffizient(self):
        return (self.standardabweichung() / self.mittelwert())*100

    #Umrechnung absolute/relative Häufigkeit
    def absoluteToRelative(self):
        result = []

        for i in self.stichprobe:
            result.append(round(i/sum(self.stichprobe),5))
        
        return result

    def relativeToAbsolute(self, n):
        result = []

        for i in self.stichprobe:
            result.append(round(i * n, 0))

        return result

    def __str__(self) -> str:
        return f"Stichprobe: {self.stichprobe}\n\tartihmetisches Mittel: {self.mittelwert()}\n\tMedian: {self.median()}\n\tRange: {self.range()}\n\tStichprobenvarianz: {self.varianz()}\n\tStichprobenabweichung: {self.standardabweichung()}\n\tVariationskoeffizient: {self.variationskoeffizient()}"


##########################################################input##################################################

#Formeln siehe "Kennwerte einer Stichprobe Formeln.png" 

stich = stichprobe([1, 2, 3])

print(stich.varianz())
print(stich.median())
print(stich.mittelwert())

print(stich.quantil(0.7))

print(stich)
