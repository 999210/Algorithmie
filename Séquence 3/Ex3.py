# Voici l'utilisation d'une boucle
def boucle_factorielle(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

# Voici l'utilisation d'une récursive
def recursive_factorielle(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * recursive_factorielle(n - 1)
    