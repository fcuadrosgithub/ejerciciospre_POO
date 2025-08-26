import unittest
from ejercicios.ejercicio10 import adivinar

class TestEjercicio10(unittest.TestCase):
    def test_adivinar(self):
        self.assertEqual(adivinar(10, 15), "Demasiado alto")
        self.assertEqual(adivinar(10, 5), "Demasiado bajo")
        self.assertEqual(adivinar(10, 10), "Correcto")

if __name__ == "__main__":
    unittest.main()
