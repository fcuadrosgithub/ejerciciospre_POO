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
    calificaciones_totales = 0 
    max_nombre = None
    max_calificacion = float("-inf")
    min_nombre = None
    min_calificacion = float("inf")
    for nombre, calificacion in calificaciones.items():
        calificaciones_totales += calificacion
        
        if calificacion > max_calificacion:
            max_calificacion = calificacion
            max_nombre = nombre
        
        if calificacion < min_calificacion:
            min_calificacion = calificacion
            min_nombre = nombre

    promedio = calificaciones_totales / len(calificaciones) if calificaciones else 0
    return {
        "promedio": promedio,
        "max": (max_nombre, max_calificacion) if max_nombre else (None, None),
        "min": (min_nombre, min_calificacion) if min_nombre else (None, None)
    }
    pass