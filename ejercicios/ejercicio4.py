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
    calif=list(calificaciones.values())
    n_max = max(calificaciones, key=calificaciones.get)
    n_min = min(calificaciones, key=calificaciones.get)
    
    return {
        "promedio": sum(calif)/len(calif),
        "max": (n_max, calificaciones[n_max]),
        "min": (n_min, calificaciones[n_min])
    }
    pass
