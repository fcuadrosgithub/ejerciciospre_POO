"""
Ejercicio 6: Lista de compras

Crea las siguientes funciones:

- agregar(lista, producto)
- eliminar(lista, producto)
- mostrar(lista), regresa la lista completa 

Cada función recibe la lista de compras y hace la operación correspondiente.
"""

def agregar(lista, producto):
    lista.append(producto)
pass

def eliminar(lista, producto):
    if producto in lista:
        lista.remove(producto)
    else:
        print(f"El producto '{producto}' no está en la lista.")
pass
def mostrar(lista):
    return lista

    pass
