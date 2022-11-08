import unittest

from 3b import find_max

class test_program(unittest.TestCase):
  def test_finding(self):
    self.assertEqual(find_max([2, 4, 6, 10, 28, 77]))
