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

    if not calificaciones:
        return {"promedio": 0, "max": None, "min": None}
    
    total_calificaciones = sum(calificaciones.values())
    promedio = total_calificaciones / len(calificaciones)
    
    nombre_max = max(calificaciones, key=calificaciones.get)
    nombre_min = min(calificaciones, key=calificaciones.get)
    
    resultado = {
        "promedio": promedio,
        "max": (nombre_max, calificaciones[nombre_max]),
        "min": (nombre_min, calificaciones[nombre_min])
    }
    
    return resultado
