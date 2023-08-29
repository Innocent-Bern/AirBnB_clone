#!/usr/bin/python3
"""unit test for base_model.py"""


import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def test_id_is_uique(self):
        base_1 = BaseModel()
        base_2 = BaseModel()
        self.assertNotEqual(base_1.id, base_2.id)

if __name__ == '__main__':
    unittest.main()
