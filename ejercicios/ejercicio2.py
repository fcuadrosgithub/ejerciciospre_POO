"""
Ejercicio 2: Números pares e impares

Crea una función `separar_pares_impares(lista)` que reciba una lista de enteros
y regrese un diccionario con:

- "pares": lista de números pares
- "impares": lista de números impares
"""

def separar_pares_impares(lista):
    return{
        "pares": [a for a in lista if a % 2 == 0],
        "impares":[a for a in lista if a % 2 != 0]
    }
    pass
