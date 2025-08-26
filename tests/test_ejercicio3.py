import unittest
from ejercicios.ejercicio3 import contar_palabras

class TestEjercicio3(unittest.TestCase):
    def test_frase_simple(self):
        self.assertEqual(contar_palabras("Hola mundo"), 2)

    def test_frase_vacia(self):
        self.assertEqual(contar_palabras(""), 0)

if __name__ == "__main__":
    unittest.main()
