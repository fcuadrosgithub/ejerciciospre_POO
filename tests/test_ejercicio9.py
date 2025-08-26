import unittest
from ejercicios.ejercicio9 import celsius_a_fahrenheit, fahrenheit_a_celsius, celsius_a_kelvin

class TestEjercicio9(unittest.TestCase):
    def test_conversores(self):
        self.assertEqual(celsius_a_fahrenheit(0), 32)
        self.assertEqual(fahrenheit_a_celsius(32), 0)
        self.assertEqual(celsius_a_kelvin(0), 273.15)

if __name__ == "__main__":
    unittest.main()
