"""
Ejercicio 5: Frecuencia de caracteres

Crea una función `frecuencia_caracteres(texto)` que reciba un string
y regrese un diccionario con la frecuencia de cada caracter.
"""

def frecuencia_caracteres(texto):
    f={}

    for letter in texto:
        if letter in f:
            f[letter]+=1
        else:
            f[letter]=1
    
    return f
    pass
