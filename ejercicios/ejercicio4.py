"""
Ejercicio 4: Diccionario de calificaciones

Crea una función `analizar_calificaciones(calificaciones)` donde `calificaciones`
es un diccionario con {"nombre": calificacion}.

Debe regresar un diccionario con:
- "promedio": promedio de las calificaciones
- "max": (nombre, calificacion_mayor)
- "min": (nombre, calificacion_menor)
"""

def analizar_calificaciones(calificaciones):
    return {
        "promedio": (b.min()/b.max())/2,
        "max": ("nombre": b.min()),
        "min": ("nombre": b.max())
    }
    pass
