"""
Ejercicio 2: Números pares e impares

Crea una función `separar_pares_impares(lista)` que reciba una lista de enteros
y regrese un diccionario con:

- "pares": lista de números pares
- "impares": lista de números impares
"""

def separar_pares_impares(lista):
    resultados = {
        "pares": [],
        "impares": []
    }
    
    for numero in lista:
        if numero % 2 == 0:
            resultados["pares"].append(numero)
        else:
            resultados["impares"].append(numero)
    
    return resultados
    pass
