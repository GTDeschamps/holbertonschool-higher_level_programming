#!/usr/bin/python3
""" protocol of unitest for the project Python_almost a circle"""
import unittest
from models.base import Base
from models.square import Square
from unittest.mock import patch
from io import StringIO

class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
    def test_id_assignment(self):
        # Créez une instance de la classe Base
        instance1 = Square(5)
        instance2 = Square(5, 0, 0, 9)
        instance3 = Square(7, 5, 3)
        # Vérifiez si les identifiants sont attribués correctement
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 9)
        self.assertEqual(instance3.id, 2)
    def test_display_2(self):
        s1 = Square(2)
        s2 = Square(3, 1, 1)
        expected_output1 = "##\n##\n"
        expected_output2 = "\n ###\n ###\n ###\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s1.display()
            actual_output = mock_stdout.getvalue()
        self.assertEqual(actual_output, expected_output1)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s2.display()
            actual_output = mock_stdout.getvalue()
        self.assertEqual(actual_output, expected_output2)
    def test_str_method3(self):
        # Test if that model is respected:
        # [Square] (<id>) <x>/<y> - <size>
        Base._Base__nb_objects = 0
        s3 = Square(5)
        s4 = Square(2, 2)
        s5 = Square(3, 1, 3)
        self.assertEqual(s3.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(s4.__str__(), "[Square] (2) 2/0 - 2")
        self.assertEqual(s5.__str__(), "[Square] (3) 1/3 - 3")
    def test_invalid_size(self):
        # Test d'une taille invalide (doit lever une exception TypeError)
        with self.assertRaises(TypeError):
            s = Square("invalid")
    def test_negative_size(self):
        # Test d'une taille négative (doit lever une exception ValueError)
        with self.assertRaises(ValueError):
            s = Square(-5)
    def test_zero_value_size(self):
        # Test d'une taille égale à zéro (doit lever une exception ValueError)
        with self.assertRaises(ValueError):
            s = Square(0)
    def test_update_kwargs2(self):
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")

if __name__ == '__main__':
    unittest.main()
