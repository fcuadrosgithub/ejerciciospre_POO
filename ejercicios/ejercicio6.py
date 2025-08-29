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
    print(f"{producto} agregado a la lista.")


def eliminar(lista, producto):
    if producto in lista:
        lista.remove(producto)
        print(f"{producto} eliminado de la lista.")
    else:
        print(f"{producto} no se encuentra en la lista.")


def mostrar(lista):
    print("Lista de compras:")
    for producto in lista:
        print("-", producto)
    return lista



compras = []

agregar(compras, "manzanas")
agregar(compras, "pan")
eliminar(compras, "pan")
mostrar(compras)
