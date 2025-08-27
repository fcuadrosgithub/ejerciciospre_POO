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

    pass
    promedio = sum(calificaciones.values()) / len(calificaciones)
    max_nombre, max_calificacion = max(calificaciones.items(), key=lambda x: x[1])
    min_nombre, min_calificacion = min(calificaciones.items(), key=lambda x: x[1])
    
    return {
        "promedio": promedio,
        "max": (max_nombre, max_calificacion),
        "min": (min_nombre, min_calificacion)
    }

# Ejemplo de uso
calificaciones = {"Alice": 85, "Bob": 90, "Charlie": 78}
resultado = analizar_calificaciones(calificaciones)
print(resultado)