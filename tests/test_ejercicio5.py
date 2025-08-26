import unittest
from ejercicios.ejercicio5 import frecuencia_caracteres

class TestEjercicio5(unittest.TestCase):
    def test_texto(self):
        resultado = frecuencia_caracteres("aabcc")
        self.assertEqual(resultado["a"], 2)
        self.assertEqual(resultado["b"], 1)
        self.assertEqual(resultado["c"], 2)

if __name__ == "__main__":
    unittest.main()
