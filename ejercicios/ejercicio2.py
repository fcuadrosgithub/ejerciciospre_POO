"""
Ejercicio 2: Números pares e impares

Crea una función `separar_pares_impares(lista)` que reciba una lista de enteros
y regrese un diccionario con:

- "pares": lista de números pares
- "impares": lista de números impares
"""

def separar_pares_impares(lista):
    # TODO: implementar
    pass
    return {
        "pares": [x for x in lista if x % 2 == 0],
        "impares": [x for x in lista if x % 2 != 0]
    }

# Ejemplo de uso
resultado = separar_pares_impares([1, 2, 3, 4, 5, 6])
print(resultado)
