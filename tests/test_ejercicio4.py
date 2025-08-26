import unittest
from ejercicios.ejercicio4 import analizar_calificaciones

class TestEjercicio4(unittest.TestCase):
    def test_calificaciones(self):
        datos = {"Ana":90,"Luis":70,"Marta":100}
        resultado = analizar_calificaciones(datos)
        self.assertEqual(resultado["promedio"], 86.66666666666667)
        self.assertEqual(resultado["max"], ("Marta", 100))
        self.assertEqual(resultado["min"], ("Luis", 70))

if __name__ == "__main__":
    unittest.main()
