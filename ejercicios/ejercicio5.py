"""
Ejercicio 5: Frecuencia de caracteres

Crea una función `frecuencia_caracteres(texto)` que reciba un string
y regrese un diccionario con la frecuencia de cada caracter.
"""

def frecuencia_caracteres(texto):
    frecuencia = {}

    for caracter in texto: 
        if caracter in frecuencia:
            frecuencia[caracter] += 1 
        else:
            frecuencia[caracter] = 1 

    return frecuencia 
texto = "hola mundo"
resultado = frecuencia_caracteres(texto)
print(resultado)
pass
