import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestPublicacion(unittest.TestCase):
    def test_constructor_and_get_titulo(self):
        publicacion = Publicacion("Satanás", 2002)
        self.assertEqual(publicacion.titulo, "Satanás", "El título debe ser 'Satanás'")

    def test_constructor_and_get_ano_publicacion(self):
        publicacion = Publicacion("Satanás", 2002)
        self.assertEqual(publicacion.ano_publicacion, 2002, "El año de publicación debe ser 2002")

    def test_mostrar_info(self):
        publicacion = Publicacion("Satanás", 2002)
        expected_output = "Título: Satanás\nAño de Publicación: 2002\n"
        self.assertEqual(self.get_output_from_mostrar_info(publicacion), expected_output)

    def test_set_and_get_titulo(self):
        publicacion = Publicacion("Satanás", 2002)
        publicacion.titulo = "Satanás"
        self.assertEqual(publicacion.titulo, "Satanás", "El título debe ser 'Satanás'")

    def test_set_and_get_ano_publicacion(self):
        publicacion = Publicacion("Satanás", 2002)
        publicacion.ano_publicacion = 2002
        self.assertEqual(publicacion.ano_publicacion, 2002, "El año de publicación debe ser 2002")

    def get_output_from_mostrar_info(self, publicacion):
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        publicacion.mostrar_info()
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        return output

if __name__ == "__main__":
    unittest.main()