#!/usr/bin/python3
""" protocol of unitest for the project Python_almost a circle"""
import unittest
from models.base import Base
from unittest.mock import patch
from io import StringIO

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
    def test_id_assignment(self):
        # Créez une instance de la classe Base
        instance1 = Base()
        instance2 = Base()
        instance3 = Base(12)
        # Vérifiez si les identifiants sont attribués correctement
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 12)

if __name__ == '__main__':
    unittest.main()
