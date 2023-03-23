import unittest

from util import array_flatten

class TestArrayFlatten(unittest.TestCase):

  def test_nested_list(self):
    array = [1, [2, [3, [4, 5]]]]
    expected = [1, 2, 3, 4, 5]
    self.assertEqual(array_flatten(array), expected)

  def test_multiple_types_list_values(self):
    array = [1, ['2', [{'3':3}, [4.0, False]]]]
    with self.assertRaises(TypeError):
      array_flatten(array)

  def test_empty_list(self):
    array = []
    expected = []
    self.assertEqual(array_flatten(array), expected)

  def test_non_list_input(self):
    array = 'string'
    with self.assertRaises(TypeError):
      array_flatten(array)