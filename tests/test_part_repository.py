from __future__ import annotations
import unittest
from unittest.mock import MagicMock

from furniturecreator.dataclasses import Part
from furniturecreator.part_repository import PartRepository


class TestPartRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.part_repository = PartRepository()

    def tearDown(self) -> None:
        del self.part_repository

    # __str__
    def test_str(self) -> None:
        self.part_repository.save('dL')
        self.part_repository.save('eS')
        self.part_repository.save('dL')
        self.part_repository.save('eL')
        self.part_repository.save('dS')
        self.part_repository.save('aS')
        self.part_repository.save('eS')
        self.assertEqual(
            self.part_repository.__str__(),
            'aS: 1\ndL: 2\ndS: 1\neS: 2\neL: 1\nTotal: 7'
        )

        self.part_repository.save('fL')
        self.part_repository.save('dS')
        self.part_repository.save('aS')
        self.part_repository.save('aS')
        self.assertEqual(
            self.part_repository.__str__(),
            'aS: 3\ndL: 2\ndS: 2\neS: 2\neL: 1\nfL: 1\nTotal: 11'
        )

    # save
    def test_save(self) -> None:
        self.part_repository.save('dL')
        self.part_repository.save('eS')
        self.assertEqual(
            self.part_repository.parts,
            {Part('d', 'L'): 1, Part('e', 'S'): 1}
        )

    def test_save_invalid(self) -> None:
        with self.assertRaises(ValueError):
            self.part_repository.save('dLS')

    # add
    def test_add(self) -> None:
        self.part_repository.add(Part('a', 'L'), 12)
        self.part_repository.add(Part('b', 'S'), 5)
        self.part_repository.add(Part('a', 'L'))
        self.assertEqual(
            self.part_repository.parts,
            {Part('a', 'L'): 13, Part('b', 'S'): 5}
        )

    def test_add_amount(self) -> None:
        self.part_repository.add(Part('a', 'L'), 12)
        self.part_repository.add(Part('b', 'L'), 5)
        self.assertEqual(self.part_repository.total_per_size,
                         {'S': 0, 'L': 17})

    def test_add_too_few(self) -> None:
        with self.assertRaises(ValueError):
            self.part_repository.add(Part('t', 'L'), 0)

    # remove
    def test_remove(self) -> None:
        self.part_repository.add(Part('t', 'S'), 9)
        self.part_repository.add(Part('z', 'L'), 5)
        self.part_repository.remove(Part('t', 'S'))
        self.part_repository.remove(Part('z', 'L'), 3)
        self.assertEqual(
            self.part_repository.parts,
            {Part('t', 'S'): 8, Part('z', 'L'): 2}
        )

    def test_remove_amount(self) -> None:
        self.part_repository.add(Part('a', 'L'), 12)
        self.part_repository.add(Part('b', 'L'), 5)
        self.part_repository.remove(Part('a', 'L'), 9)
        self.part_repository.remove(Part('b', 'L'), 5)
        self.assertEqual(self.part_repository.total_per_size, {'S': 0, 'L': 3})

    def test_remove_too_few(self) -> None:
        with self.assertRaises(ValueError):
            self.part_repository.remove(Part('a', 'L'), 0)

    def test_remove_part_from_stock_too_many(self) -> None:
        self.part_repository.add(Part('a', 'L'), 12)
        with self.assertRaises(ValueError):
            self.part_repository.remove(Part('a', 'L'), 13)

    # sum_stock
    def test_sum_stock_calls_sum_all_stock(self) -> None:
        self.part_repository.sum_all_stock = MagicMock()
        self.part_repository.sum_stock('A')
        self.part_repository.sum_all_stock.assert_called_with()

    def test_sum_stock_calls_sum_size_stock(self) -> None:
        self.part_repository.sum_size_stock = MagicMock()
        self.part_repository.sum_stock('L')
        self.part_repository.sum_size_stock.assert_called_with('L')

    def test_sum_stock_calls_sum_part_stock(self) -> None:
        self.part_repository.sum_part_stock = MagicMock()
        self.part_repository.sum_stock(Part('a', 'L'))
        self.part_repository.sum_part_stock.assert_called_with(Part('a', 'L'))

    # sum_all_stock
    def test_sum_all_stock_add(self) -> None:
        self.part_repository.add(Part('s', 'S'), 17)
        self.part_repository.add(Part('a', 'L'), 11)
        self.assertEqual(self.part_repository.sum_all_stock(), 28)

    def test_sum_all_stock_add_and_remove(self) -> None:
        self.part_repository.add(Part('s', 'S'), 17)
        self.part_repository.add(Part('q', 'S'), 9)
        self.part_repository.add(Part('a', 'L'), 11)
        self.part_repository.add(Part('b', 'L'), 5)
        self.part_repository.remove(Part('q', 'S'), 6)
        self.part_repository.remove(Part('q', 'S'))
        self.part_repository.remove(Part('b', 'L'), 2)
        self.part_repository.remove(Part('a', 'L'), 11)
        self.assertEqual(self.part_repository.sum_all_stock(), 22)

    # sum_size_stock
    def test_sum_size_stock_add(self) -> None:
        self.part_repository.add(Part('s', 'S'), 17)
        self.part_repository.add(Part('q', 'S'), 9)
        self.part_repository.add(Part('a', 'L'), 11)
        self.part_repository.add(Part('b', 'L'), 5)
        self.assertEqual(self.part_repository.sum_size_stock('S'), 26)
        self.assertEqual(self.part_repository.sum_size_stock('L'), 16)

    def test_sum_size_stock_add_and_remove(self) -> None:
        self.part_repository.add(Part('s', 'S'), 17)
        self.part_repository.add(Part('q', 'S'), 9)
        self.part_repository.add(Part('a', 'L'), 11)
        self.part_repository.add(Part('b', 'L'), 5)
        self.part_repository.remove(Part('q', 'S'), 6)
        self.part_repository.remove(Part('q', 'S'))
        self.part_repository.remove(Part('b', 'L'), 2)
        self.part_repository.remove(Part('a', 'L'), 11)
        self.assertEqual(self.part_repository.sum_size_stock('S'), 19)
        self.assertEqual(self.part_repository.sum_size_stock('L'), 3)

    def test_sum_size_stock_invalid(self) -> None:
        self.part_repository.add(Part('a', 'S'), 10)
        with self.assertRaises(ValueError):
            self.part_repository.sum_size_stock('X')

    # sum_part_stock
    def test_sum_part_stock_zero(self) -> None:
        result = self.part_repository.sum_part_stock(Part('a', 'S'))
        self.assertEqual(result, 0)

    def test_sum_part_stock(self) -> None:
        self.part_repository.save('aS')
        self.part_repository.save('aS')
        self.part_repository.save('aS')
        result = self.part_repository.sum_part_stock(Part('a', 'S'))
        self.assertEqual(result, 3)

    # get_part_list
    def test_get_part_list_empty(self) -> None:
        result = self.part_repository.get_part_list()
        self.assertEqual(result, [])

    def test_get_part_list_three_types(self) -> None:
        self.part_repository.save('aS')
        self.part_repository.save('aS')
        self.part_repository.save('bS')
        self.part_repository.save('aL')
        self.part_repository.save('aS')

        result = self.part_repository.get_part_list()
        expected = [
            Part('a', 'S'),
            Part('b', 'S'),
            Part('a', 'L'),
        ]
        self.assertEqual(result, expected)

    # get_part_with_most_in_stock
    def test_get_part_with_most_in_stock(self) -> None:
        self.part_repository.save('dL')
        self.part_repository.save('eS')
        self.part_repository.save('dL')
        self.part_repository.save('eL')
        self.part_repository.save('dS')
        self.part_repository.save('aS')
        self.part_repository.save('eS')

        self.assertEqual(
            self.part_repository.get_part_with_most_in_stock(),
            Part('d', 'L')
        )
        self.part_repository.save('fL')
        self.part_repository.save('dS')
        self.part_repository.save('aS')
        self.part_repository.save('aS')
        self.assertEqual(
            self.part_repository.get_part_with_most_in_stock(),
            Part('a', 'S')
        )

    def test_get_part_with_most_in_stock_size(self) -> None:
        self.part_repository.save('dL')
        self.part_repository.save('eS')
        self.part_repository.save('dL')
        self.part_repository.save('eL')
        self.part_repository.save('dS')
        self.part_repository.save('aS')
        self.part_repository.save('eS')

        self.assertEqual(
            self.part_repository.get_part_with_most_in_stock('S'),
            Part('e', 'S')
        )
        self.part_repository.save('fL')
        self.part_repository.save('dS')
        self.part_repository.save('aS')
        self.part_repository.save('aS')
        self.assertEqual(
            self.part_repository.get_part_with_most_in_stock('L'),
            Part('d', 'L')
        )


if __name__ == "__main__":
    unittest.main()
