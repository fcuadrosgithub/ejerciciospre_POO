"""
Ejercicio 6: Lista de compras

Crea las siguientes funciones:

- agregar(lista, producto)
- eliminar(lista, producto)
- mostrar(lista), regresa la lista completa 

Cada función recibe la lista de compras y hace la operación correspondiente.
"""

def agregar(lista, producto):
    """Agrega un producto a la lista de compras."""
    lista.append(producto)
    # TODO: implementar
    pass

def eliminar(lista, producto):
    """Elimina un producto de la lista de compras si existe."""
    if producto in lista:
        lista.remove(producto)
    else:
        print(f"El producto '{producto}' no está en la lista.")
    # TODO: implementar
    pass

def mostrar(lista):
    """Regresa la lista completa de compras."""
    return lista

# TODO: implementar
    pass
