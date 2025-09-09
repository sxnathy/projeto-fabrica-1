import unittest
from media import calcular_media, classificar_media

class TestMedia(unittest.TestCase):
    def test_classificar_media_aprovado(self):
        """Verifica a classificação 'Aprovado(a)'."""
        self.assertEqual(classificar_media(7.0), "Aprovado(a) ✅")
        self.assertEqual(classificar_media(9.5), "Aprovado(a) ✅")

    def test_classificar_media_recuperacao(self):
        """Verifica a classificação 'Recuperação'."""
        self.assertEqual(classificar_media(5.0), "Recuperação ⚠️")
        self.assertEqual(classificar_media(6.9), "Recuperação ⚠️")

    def test_classificar_media_reprovado(self):
        """Verifica a classificação 'Reprovado(a)'."""
        self.assertEqual(classificar_media(4.99), "Reprovado(a) ❌")


if __name__ == '__main__':
    unittest.main()
