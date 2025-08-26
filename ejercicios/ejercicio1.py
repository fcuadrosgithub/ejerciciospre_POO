"""
Ejercicio 1: Operaciones básicas

Crea una función `operaciones_basicas(a, b)` que reciba dos números
y regrese un diccionario con:

- "suma": a + b
- "resta": a - b
- "multiplicacion": a * b
- "division": a / b  (si b != 0, de lo contrario regresa None)
"""

def operaciones_basicas(a, b):
    resultado ={
        "suma": a + b,
        "resta": a- b,
        "multiplicacion": a * b,
        "division": a / b if b !=0 else None
    }
    return resultado
a= int(input("Ingrese el prmer número (num1):"))
b= int(input("Ingrese el segundo número (num2):"))
resultado = operaciones_basicas(a, b)
print(operaciones_basicas(a,b)) 
pass
