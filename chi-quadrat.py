from numpy import log, log10, square, true_divide
import scipy.stats
import wk_verteilungen

print("\n")

def printLine(n):
    for i in range(0,n):
        print("-", end="", sep="")

def putInCentreOfField(fieldWidth, input):
    inputlen = len(str(input))
    diff = (fieldWidth - inputlen)/2

    if diff % 1 == 0:
        print("|", end = "")
        for i in range(0, int(diff)):
            print(" ", end = "", sep="")
        print(input, end="", sep="")
        for i in range(0, int(diff)):
            print(" ", end = "", sep="")
    else:
        print("|", end = "")
        diff = int(diff-0.5)
        for i in range(0, diff+1):
            print(" ", end = "", sep="")
        print(input, end ="")
        for i in range(0, diff):
            print(" ", end = "", sep="")
        
def chiSquareTest(alpha, n, classes:list, prevalences:list, probabilities:list):
    """alpha = Irrtumswahrscheinlichkeit; n = Anz. d. Durchführungen; classes = Klassen, z.B. Augenzahl...; prevalences = absolute Häufigkeiten; probabilities = WK für Klassen"""
    
    print(f"\ngeg: α = {alpha}; n = {n}; Klassen = {classes}; absolute Häufigkeiten = {prevalences}")

    lowerWK = 1 - alpha

    f = len(classes) - 1

    nTheorie = []
    for i in probabilities:
        nTheorie.append(round(n * i, 5))

    deltaN = []
    for i in range(0, len(prevalences)):
        deltaN.append(round(prevalences[i] - nTheorie[i], 6))

    chi = []  
    z = 0                                                       #Testwert
    for i in range(0, len(deltaN)):
        j = round((square(deltaN[i]) / nTheorie[i]), 5)
        chi.append(j)
        z += j

    z = round(z,5)
    c = round(scipy.stats.chi2.ppf(lowerWK, f),5)                        #Quantil

    if c>=z:
        passed = True
    else:
        passed = False

    #AUSGABE
    tableHead = ["Klasse i", "n(i) (SP)", "p(i) (theoretisch)", "n(i)* = n*p(i) (theoretisch)", "deltaN(i) = n(i) - n(i)*", "(deltaN(i))^2 / n(i)*"]
    COLUMNWIDTHS = [16, 17, 26, 36, 32, 29]

    #Tabelle
    print(); printLine(163); print()
    for i in range(0, (len(classes) + 1)):
        #print("|    ", end="")
        for j in range(1, 7):
            if i == 0:
                if j == 1: print("|", end="    ")
                print(tableHead[j-1], end = "    |    ")
                if j == 6: print()
            else:
                if j == 1:
                    putInCentreOfField(COLUMNWIDTHS[j-1], classes[i-1])
                elif j == 2:
                    putInCentreOfField(COLUMNWIDTHS[j-1], prevalences[i-1])
                elif j == 3:
                    putInCentreOfField(COLUMNWIDTHS[j-1], probabilities[i-1])
                elif j == 4:
                    putInCentreOfField(COLUMNWIDTHS[j-1], nTheorie[i-1])
                elif j == 5:
                    putInCentreOfField(COLUMNWIDTHS[j-1], deltaN[i-1])
                elif j == 6:
                    putInCentreOfField(COLUMNWIDTHS[j-1], chi[i-1])
                    print("|")
        printLine(163)
        print()

    print(f"\nP(Z<=c) = 1 - α = {lowerWK}    |    gesucht: {lowerWK}-Quantil der Chi-Quadrat-Verteilung mit f={f} (n-1 Freiheitsgrade)")
    if passed == True:
        print(f"    --> c = {c} --> z = {z} <= {c} = c --> Test bestanden")
    else:
        print(f"    --> c = {c} --> z = {z} >= {c} = c --> Test NICHT bestanden     |    z(Dach) = Testwert; Muss kleiner als Quantile sein")
    print()


################################################input########################################################
classes = [0,1,2,3,4]
prevalences = [14,28,15,3,0]
probabilities = wk_verteilungen.hypergeometricXList(32,4,10,classes)


chiSquareTest(0.05, 60, classes, prevalences, probabilities)