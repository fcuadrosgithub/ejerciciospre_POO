"""
Ejercicio 9: Conversor de temperaturas

Crea tres funciones:
- celsius_a_fahrenheit(c)
- fahrenheit_a_celsius(f)
- celsius_a_kelvin(c)
"""


def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9


def celsius_a_kelvin(c):
    return c + 273.15



temp_c = float(input("Ingresa temperatura en Celsius: "))
print("Celsius a Fahrenheit:", celsius_a_fahrenheit(temp_c))
print("Celsius a Kelvin:", celsius_a_kelvin(temp_c))

temp_f = float(input("Ingresa temperatura en Fahrenheit: "))
print("Fahrenheit a Celsius:", fahrenheit_a_celsius(temp_f))
