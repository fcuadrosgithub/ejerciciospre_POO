"""
Ejercicio 5: Frecuencia de caracteres

Crea una función `frecuencia_caracteres(texto)` que reciba un string
y regrese un diccionario con la frecuencia de cada caracter.
"""

def frecuencia_caracteres(texto):
    frecuencia = {}
    for char in texto:
        if char in frecuencia:
            frecuencia[char] += 1
        else:
            frecuencia[char] = 1
    return frecuencia


    pass
