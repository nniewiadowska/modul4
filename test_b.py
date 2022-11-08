import unittest

from b import adding

class Test_program(unittest.TestCase):
  def test_adding(self):
    self.assertEqual(adding(1, 2, 6, 8))
