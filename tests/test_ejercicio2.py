import unittest
from ejercicios.ejercicio2 import separar_pares_impares

class TestEjercicio2(unittest.TestCase):
    def test_lista_mixta(self):
        resultado = separar_pares_impares([1,2,3,4,5])
        self.assertEqual(resultado["pares"], [2,4])
        self.assertEqual(resultado["impares"], [1,3,5])

    def test_lista_vacia(self):
        resultado = separar_pares_impares([])
        self.assertEqual(resultado["pares"], [])
        self.assertEqual(resultado["impares"], [])

if __name__ == "__main__":
    unittest.main()
