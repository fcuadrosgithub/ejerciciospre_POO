"""
Ejercicio 8: Matriz y suma de filas/columnas

Crea una función `suma_filas_columnas(matriz)` que reciba una matriz 3x3 (lista de listas)
y regrese un diccionario con:
- "filas": lista con la suma de cada fila
- "columnas": lista con la suma de cada columna
"""

def suma_filas_columnas(matriz):
    suma_filas = []
    for fila in matriz:
        suma_filas.append(sum(fila))
    
    suma_columnas = []
    for j in range(len(matriz[0])):  
        suma_col = 0
        for i in range(len(matriz)):
            suma_col += matriz[i][j]
        suma_columnas.append(suma_col)
    
    return {"filas": suma_filas, "columnas": suma_columnas}



matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = suma_filas_columnas(matriz)
print(resultado)
