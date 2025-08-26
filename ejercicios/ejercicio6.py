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
    pass

def mostrar(lista):
    return lista  


lista_compras = []
agregar(lista_compras, "huevo")
agregar(lista_compras, "harina")
agregar(lista_compras, "azucar")

print("Lista de compras:", mostrar(lista_compras))

# Eliminar un producto
eliminar(lista_compras, "azucar")

# Mostrar la lista actualizada
print("Lista de compras actualizada:", mostrar(lista_compras))
pass
