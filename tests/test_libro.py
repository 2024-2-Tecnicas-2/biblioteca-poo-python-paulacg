import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestLibro(unittest.TestCase):
 def setUp(self):
        self.libro = Libro("Satanás", 2002, "Mario Mendoza", 280)

    def test_get_autor(self):
        self.assertEqual(self.libro.autor, "Mario Mendoza")

    def test_set_autor(self):
        self.libro.autor = "Mario Mendoza"
        self.assertEqual(self.libro.autor, "Mario Mendoza")

    def test_get_numero_paginas(self):
        self.assertEqual(self.libro.numero_paginas, 280)

    def test_set_numero_paginas(self):
        self.libro.numero_paginas = 280
        self.assertEqual(self.libro.numero_paginas, 280)

    def test_get_titulo(self):
        self.assertEqual(self.libro.titulo, "Satanás")

    def test_set_titulo(self):
        self.libro.titulo = "Satanás"
        self.assertEqual(self.libro.titulo, "Satanás")

    def test_get_ano_publicacion(self):
        self.assertEqual(self.libro.ano_publicacion, 2002)

    def test_set_ano_publicacion(self):
        self.libro.ano_publicacion = 2002
        self.assertEqual(self.libro.ano_publicacion, 2002)

if __name__ == "__main__":
    unittest.main()
