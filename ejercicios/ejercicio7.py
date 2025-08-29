"""
Ejercicio 7: Números primos

Crea una función `es_primo(n)` que devuelva True si n es primo, False si no.

Crea otra función `primos_hasta(n)` que devuelva una lista de primos hasta n.
"""

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    pass

def primos_hasta(n):
        return [i for i in range(2, n + 1) if es_primo(i)]
     
    
