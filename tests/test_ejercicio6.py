import unittest
from ejercicios.ejercicio6 import agregar, eliminar, mostrar

class TestEjercicio6(unittest.TestCase):
    def test_lista_compras(self):
        lista = []
        agregar(lista, "pan")
        self.assertIn("pan", lista)
        eliminar(lista, "pan")
        self.assertNotIn("pan", lista)
        lista = ["leche","huevos"]
        self.assertEqual(mostrar(lista), ["leche","huevos"])

if __name__ == "__main__":
    unittest.main()
