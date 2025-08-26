"""
Ejercicio 8: Matriz y suma de filas/columnas

Crea una función `suma_filas_columnas(matriz)` que reciba una matriz 3x3 (lista de listas)
y regrese un diccionario con:
- "filas": lista con la suma de cada fila
- "columnas": lista con la suma de cada columna
"""

def suma_filas_columnas(matriz):
    suma_filas = [sum(fila) for fila in matriz]
    suma_columnas = [sum(matriz[i][j] for i in range(3)) for j in range(3)]

    return {
        "filas": suma_filas,
        "columnas": suma_columnas
    }
    pass
