"""
Ejercicio 2: Números pares e impares

Crea una función `separar_pares_impares(lista)` que reciba una lista de enteros
y regrese un diccionario con:

- "pares": lista de números pares
- "impares": lista de números impares
"""

def separar_pares_impares(lista):
    return{
        "pares":[ b for b in lista if b % 2 == 0] ,
        "impares": [b for b in lista if b % 2 != 0] 
    }
    pass
