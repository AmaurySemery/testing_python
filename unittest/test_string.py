import unittest
"""
python -m unittest nom_du_fichier

python nom_du_fichier.py

python -m unittest nom_du_fichier.<nom du test>

python -m unittest discover <nom du répertoire de test>/
"""
class TestString(unittest.TestCase):
    def test_should_capitalize_string(self):
        string = "hello"
        expected_value = "Hello"
        self.assertEqual(string.capitalize(), expected_value)


    def test_should_upper_string(self):
        string = "hello"
        expected_value = "HELLO"
        self.assertEqual(string.upper(), expected_value)


    def test_should_trim_string(self):
        string = "  hello "
        expected_value = "hello"
        self.assertEqual(string.strip(), expected_value)


if __name__ == "__main__":
    unittest.main()