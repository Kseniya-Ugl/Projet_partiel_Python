# a) Implémenter la fonction polynomiale

def function(polynome, n, x):
    result = polynome[0]

    for i in range(1, n):
        result = result * x + polynome[i]

    return result
#1x3 - 1.5x2 + 6x + 5 pour x = 5
polynome = [1, -1.5, -6, 5]
x = 5
n = len(polynome)

#le resultat
result = 0

print("Le resultat est:", function(polynome, n, x))

