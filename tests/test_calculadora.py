import unittest
from main import calcular_media

class TestCalculadora(unittest.TestCase):

   def test_media(self):
      self.assertEqual(calcular_media([10, 20, 30, 40, 50]), 30)

   def test_lista_vazia(self):
      with self.assertRaises(ValueError):
         calcular_media([])
   
   def test_media_negativos(self):
      self.assertEqual(calcular_media([-10, -20, -30, -40, -50]), -30)

if __name__ == "__main__":
   unittest.main()
   