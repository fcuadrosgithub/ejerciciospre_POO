"""
Ejercicio 8: Matriz y suma de filas/columnas

Crea una función `suma_filas_columnas(matriz)` que reciba una matriz 3x3 (lista de listas)
y regrese un diccionario con:
- "filas": lista con la suma de cada fila
- "columnas": lista con la suma de cada columna
"""

def suma_filas_columnas(matriz):
    suma_filas = []  
    suma_columnas = [0] * 3  

    for fila in matriz:
        suma_fila = sum(fila)
        suma_filas.append(suma_fila)

        for i in range(3):
            suma_columnas[i] += fila[i]

    return {
        "filas": suma_filas,
        "columnas": suma_columnas
    }

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
pass
