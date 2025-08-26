import unittest
from ejercicios.ejercicio8 import suma_filas_columnas

class TestEjercicio8(unittest.TestCase):
    def test_matriz(self):
        matriz = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        resultado = suma_filas_columnas(matriz)
        self.assertEqual(resultado["filas"], [6,15,24])
        self.assertEqual(resultado["columnas"], [12,15,18])

if __name__ == "__main__":
    unittest.main()
