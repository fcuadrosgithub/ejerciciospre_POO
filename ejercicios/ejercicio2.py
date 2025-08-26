"""
Ejercicio 2: Números pares e impares

Crea una función `separar_pares_impares(lista)` que reciba una lista de enteros
y regrese un diccionario con:

- "pares": lista de números pares
- "impares": lista de números impares
"""

def separar_pares_impares(lista):
    resultado = {
        "pares": [],
        "impares": []
    }

    for num in lista:
        if num % 2 == 0:
            resultado["pares"].append(num)
        else:
            resultado["impares"].append(num)
            print("Números pares:", resultado["pares"])
            print("Números impares:", resultado["impares"])
    return resultado

    pass
