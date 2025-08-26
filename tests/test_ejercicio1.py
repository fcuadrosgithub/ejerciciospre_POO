import unittest
from ejercicios.ejercicio1 import operaciones_basicas

class TestEjercicio1(unittest.TestCase):
    def test_operaciones_normales(self):
        resultado = operaciones_basicas(10, 2)
        self.assertEqual(resultado["suma"], 12)
        self.assertEqual(resultado["resta"], 8)
        self.assertEqual(resultado["multiplicacion"], 20)
        self.assertEqual(resultado["division"], 5)

    def test_division_por_cero(self):
        resultado = operaciones_basicas(5, 0)
        self.assertIsNone(resultado["division"])

if __name__ == "__main__":
    unittest.main()
