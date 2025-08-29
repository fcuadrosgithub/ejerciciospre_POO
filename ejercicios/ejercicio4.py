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
        return {"promedio": None, "max": (None, None), "min": (None, None)}

    
    nombres, notas = zip(*calificaciones)

    promedio = sum(notas) / len(notas)
    calificacion_mayor = max(notas)
    calificacion_menor = min(notas)
    
   
    nombre_mayor = nombres[notas.index(calificacion_mayor)]
    nombre_menor = nombres[notas.index(calificacion_menor)]

    resultados = {
        "promedio": promedio,
        "max": (nombre_mayor, calificacion_mayor),
        "min": (nombre_menor, calificacion_menor)
    }

    return resultados
    pass