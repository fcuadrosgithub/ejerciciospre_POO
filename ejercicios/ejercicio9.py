"""
Ejercicio 9: Conversor de temperaturas

Crea tres funciones:
- celsius_a_fahrenheit(c)
- fahrenheit_a_celsius(f)
- celsius_a_kelvin(c)
"""

def celsius_a_fahrenheit(c):
    return(c * 9/5) + 32
    pass

def fahrenheit_a_celsius(f):
    return(f - 32) * 5/9
    pass

def celsius_a_kelvin(c):
    return c + 273.15
celsius = 15
fahrenheit = 67
kelvin = 0

print(f"{celsius}°C a Fahrenheit: {celsius_a_fahrenheit(celsius)}°F")
print(f"{fahrenheit}°F a Celsius: {fahrenheit_a_celsius(fahrenheit)}°C")
print(f"{celsius}°C a Kelvin: {celsius_a_kelvin(celsius)} K")
pass
