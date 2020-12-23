from __future__ import annotations
import unittest

from furniturecreator.dataclasses import Part
from furniturecreator.utilities import filter_parts_list_by_size, \
                                       filter_parts_dict_by_size


class TestFurnitureCreatorUtilities(unittest.TestCase):

    # filter_parts_list_by_size
    def test_filter_parts_list_by_size(self) -> None:
        input = [
            Part('a', 'S'), Part('u', 'L'), Part('b', 'S'),
            Part('v', 'L'), Part('c', 'S'), Part('w', 'L'),
            Part('d', 'S'), Part('x', 'L'), Part('e', 'S'),
            Part('y', 'L'), Part('f', 'S'), Part('z', 'L'),
        ]
        expected = [
            Part('a', 'S'), Part('b', 'S'), Part('c', 'S'),
            Part('d', 'S'), Part('e', 'S'), Part('f', 'S'),
        ]
        self.assertEqual(filter_parts_list_by_size(input, 'S'), expected)

    def test_filter_parts_list_by_size_invalid_size(self) -> None:
        with self.assertRaises(ValueError):
            filter_parts_list_by_size([], 'X')

    # filter_parts_dict_by_size
    def test_filter_parts_dict_by_size(self) -> None:
        input = {
            Part('a', 'S'): 1, Part('u', 'L'): 2, Part('b', 'S'): 3,
            Part('v', 'L'): 1, Part('c', 'S'): 2, Part('w', 'L'): 3,
            Part('d', 'S'): 1, Part('x', 'L'): 2, Part('e', 'S'): 3,
            Part('y', 'L'): 1, Part('f', 'S'): 2, Part('z', 'L'): 3,
        }
        expected = {
            Part('a', 'S'): 1, Part('b', 'S'): 3, Part('c', 'S'): 2,
            Part('d', 'S'): 1, Part('e', 'S'): 3, Part('f', 'S'): 2,
        }
        self.assertEqual(filter_parts_dict_by_size(input, 'S'), expected)

    def test_filter_parts_dict_by_size_invalid_size(self) -> None:
        with self.assertRaises(ValueError):
            filter_parts_dict_by_size({}, 'X')


if __name__ == "__main__":
    unittest.main()
