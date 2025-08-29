"""
Ejercicio 10: Juego de adivinar el número

Crea una función `adivinar(numero_secreto, intento)` que reciba
el número secreto y un intento del jugador.

Debe regresar:
- "Demasiado alto" si el intento > numero_secreto
- "Demasiado bajo" si el intento < numero_secreto
- "Correcto" si el intento == numero_secreto
"""

def adivinar(numero_secreto, intento):
     
    if intento > numero_secreto:
        return "Demasiado alto"
    elif intento < numero_secreto:
        return "Demasiado bajo"
    else:
        return "Correcto"

pass
