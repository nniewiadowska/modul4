import unittest

from a import multiply

class Test_program(unittest.TestCase):
  def test_multiply(self):
    self.assertEqual(multiply(3, 5, 7))
    
