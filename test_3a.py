import unittest

from 3a import multiply

class test_program(unittest.TestCase):
  def test_multiply(self):
    self.assertEqual(multiply(3, 5, 7))
    
