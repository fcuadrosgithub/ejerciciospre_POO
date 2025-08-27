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
    c_max = max(calificaciones, key=calificaciones.get)
    c_min = min(calificaciones, key=calificaciones.get)
    
    return {
        "promedio": sum(calif)/len(calif),
        "max": (c_max, calificaciones[c_max]),
        "min": (c_min, calificaciones[c_min])
    }
    pass
