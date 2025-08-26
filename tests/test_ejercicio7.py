import unittest
from ejercicios.ejercicio7 import es_primo, primos_hasta

class TestEjercicio7(unittest.TestCase):
    def test_es_primo(self):
        self.assertTrue(es_primo(7))
        self.assertFalse(es_primo(8))

    def test_primos_hasta(self):
        self.assertEqual(primos_hasta(10), [2,3,5,7])

if __name__ == "__main__":
    unittest.main()
