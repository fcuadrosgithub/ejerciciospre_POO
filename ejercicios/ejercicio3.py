"""
Ejercicio 3: Contador de palabras

Crea una función `contar_palabras(frase)` que reciba una cadena
y regrese el número de palabras (separadas por espacios).
"""

def contar_palabras(frase):
    palabras = frase.split()
    
    return len(palabras)
    pass
