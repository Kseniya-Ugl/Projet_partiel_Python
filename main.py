# b)Implémenter la fonction factorielle (Approche récursive ou classique) :

def factorielle(n):
    if n == 0:
        return 1
    else:
        # definition de factorielle function
        return n * factorielle(n-1)

if __name__ == '__main__':
    print("Le resultat de factorielle(5):", factorielle(5))
    print("Le resultat de factorielle(-2):", factorielle(-2))
