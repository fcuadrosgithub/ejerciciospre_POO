"""
Ejercicio 6: Lista de compras

Crea las siguientes funciones:

- agregar(lista, producto)
- eliminar(lista, producto)
- mostrar(lista), regresa la lista completa 

Cada función recibe la lista de compras y hace la operación correspondiente.
"""


def agregar(lista, producto):
    # Agrega un producto a la lista
    lista.append(producto)
    pass

def eliminar(lista, producto):
    # Elimina un producto de la lista si existe
    if producto in lista:
        lista.remove(producto)
    pass

def mostrar(lista):
    # Muestra la lista de productos
    return lista
    pass