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
    promedio = sum(calificaciones.values()) / len(calificaciones)
    max_alumno = max(calificaciones.items(), key=lambda x: x[1])
    min_alumno = min(calificaciones.items(), key=lambda x: x[1])

    return {
        "promedio": promedio,
        "max": max_alumno,
        "min": min_alumno
    }


califs = {
    "Ana": 85,
    "Luis": 90,
    "Maria": 70,
    "Pedro": 95
}

resultado = analizar_calificaciones(califs)
print(resultado)

