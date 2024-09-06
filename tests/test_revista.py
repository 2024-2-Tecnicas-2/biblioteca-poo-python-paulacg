import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestRevista(unittest.TestCase):
def setUp(self):
        self.revista = Revista("Revista de Ciencia", 2023, 25, "Ciencia y Tecnología")

    def test_get_numero_revista(self):
        self.assertEqual(self.revista.numero_revista, 25)

    def test_set_numero_revista(self):
        self.revista.numero_revista = 25
        self.assertEqual(self.revista.numero_revista, 25)

    def test_get_nombre_revista(self):
        self.assertEqual(self.revista.nombre_revista, "Ciencia y Tecnología")

    def test_set_nombre_revista(self):
        self.revista.nombre_revista = "Innovación y Futuro"
        self.assertEqual(self.revista.nombre_revista, "Innovación y Futuro")

    def test_get_titulo(self):
        self.assertEqual(self.revista.titulo, "Revista de Ciencia")

    def test_set_titulo(self):
        self.revista.titulo = "Revista de Tecnología"
        self.assertEqual(self.revista.titulo, "Revista de Tecnología")

    def test_get_ano_publicacion(self):
        self.assertEqual(self.revista.ano_publicacion, 2023)

    def test_set_ano_publicacion(self):
        self.revista.ano_publicacion = 2023
        self.assertEqual(self.revista.ano_publicacion, 2023)

if __name__ == "__main__":
    unittest.main()