"""
Ejercicio 8: Matriz y suma de filas/columnas

Crea una función `suma_filas_columnas(matriz)` que reciba una matriz 3x3 (lista de listas)
y regrese un diccionario con:
- "filas": lista con la suma de cada fila
- "columnas": lista con la suma de cada columna
"""

def suma_filas_columnas(matriz):
    resultado = {
        "filas": [],
        "columnas": [0, 0, 0]  # Inicializamos la suma de columnas
    }
    
    for fila in matriz:
        suma_fila = sum(fila)
        resultado["filas"].append(suma_fila)
        
        for i in range(3):  # Asumiendo que la matriz es 3x3
            resultado["columnas"][i] += fila[i]
    
    return resultado
    pass