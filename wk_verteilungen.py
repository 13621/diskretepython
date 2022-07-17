import scipy.special

#Hypergeometrische
def hypergeometricX(N, M, n, x):
    print("Hypergeometrische Verteilung: P(X=x) = (binom(M,x) * binom(N-M, n-x)) / binom(N,n)")
    return round((scipy.special.binom(M,x) * scipy.special.binom(N-M, n-x)) / scipy.special.binom(N,n), 6)

#print(hypergeometricX(48, 8, 12, 0))

def hypergeometricLowerAndEqualX(N, M, n, x):
    print("Hypergeometrische Verteilung: P(X<=x) = (binom(M,x) * binom(N-M, n-x)) / binom(N,n)")
    result = 0
    for i in range(0,x+1):
        result += round((scipy.special.binom(M,i) * scipy.special.binom(N-M, n-i)) / scipy.special.binom(N,n), 6)
    return result
    
#print(1 - hypergeometricLowerAndEqualX(48, 8, 12, 4))

def hypergeometricXList(N, M, n, x:list):
    print("Hypergeometrische Verteilung: P(X=x) = (binom(M,x) * binom(N-M, n-x)) / binom(N,n)")
    result = []

    for i in x:
        result.append(round((scipy.special.binom(M,i) * scipy.special.binom(N-M, n-i)) / scipy.special.binom(N,n),6))
    return result

#print(hypergeometricXList(48, 8, 12, [0,1,2,3,4,5,6,7,8]))