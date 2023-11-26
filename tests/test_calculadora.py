import unittest
from main import calculate_average


class TestCalculator(unittest.TestCase):

    def test_media_lista_positivos(self):
        self.assertEqual(calculate_average
        ([10, 20, 30, 40, 50]), 30)

    def test_media_lista_negativos(self):
        self.assertEqual(calculate_average
        ([-10, -20, -30, -40, -50]), -30)

    def test_media_mista(self):
        self.assertEqual(calculate_average
        ([-10, 20, -30, 40, -50]), -6)

    def test_media_decimal(self):
        self.assertAlmostEqual(calculate_average([1.5, 2.5, 3.5, 4.5, 5.5]), 3.5, places=2)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_lista_nao_numerica(self):
        with self.assertRaises(TypeError):
            calculate_average
            (["a", "b", "c"])

    def test_media_one_element(self):
        self.assertEqual(calculate_average([42]), 42)

if __name__ == "__main__":
    unittest.main()