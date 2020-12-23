from __future__ import annotations
import unittest

from furniturecreator.dataclasses import Part, Design
from furniturecreator.design_repository import DesignRepository


class TestDesignRepository(unittest.TestCase):

    def setUp(self):
        self.design_repository = DesignRepository()

    def tearDown(self):
        del self.design_repository

    # save
    def test_save(self) -> None:
        self.design_repository.save('[Desk]S10a5b3c20')
        self.design_repository.save('[Trash can]L1a12b4c6d30')

        expected = [
            Design('Desk', 'S', {
                Part('a', 'S'): 10,
                Part('b', 'S'): 5,
                Part('c', 'S'): 3
            }, 20),
            Design('Trash can', 'L', {
                Part('a', 'L'): 1,
                Part('b', 'L'): 12,
                Part('c', 'L'): 4,
                Part('d', 'L'): 6
            }, 30),
        ]
        self.assertEqual(self.design_repository.designs, expected)

    def test_save_invalid(self) -> None:
        with self.assertRaises(ValueError):
            self.design_repository.save('[Table]L1a12b4c6d')
        with self.assertRaises(ValueError):
            self.design_repository.save('TableL1a12b4c6d30')

    # parse_design
    def test_parse_design_invalid(self) -> None:
        with self.assertRaises(ValueError):
            self.design_repository.parse_design('[Basket]S4t10x1z6d')
            self.design_repository.parse_design('[Chair]L10')
            self.design_repository.parse_design('[Chair]1a2b3c6')

    def test_parse_design(self) -> None:
        result = self.design_repository.parse_design('[Table]S9b5c8d29')
        expected = Design('Table', 'S', {
            Part('b', 'S'): 9,
            Part('c', 'S'): 5,
            Part('d', 'S'): 8
        }, 29)
        self.assertEqual(result, expected)

        result = self.design_repository.parse_design('[Bed]L8a6c4d18')
        expected = Design('Bed', 'L', {
            Part('a', 'L'): 8,
            Part('c', 'L'): 6,
            Part('d', 'L'): 4
        }, 18)
        self.assertEqual(result, expected)

    # parse_parts
    def test_parse_parts(self) -> None:
        result = self.design_repository.parse_parts('1q', 'S')
        self.assertEqual(result, {Part('q', 'S'): 1})

        result = self.design_repository.parse_parts('1a2b3c', 'L')
        self.assertEqual(result, {
            Part('a', 'L'): 1,
            Part('b', 'L'): 2,
            Part('c', 'L'): 3,
        })

        result = self.design_repository.parse_parts('50d1q1177x', 'L')
        self.assertEqual(result, {
            Part('d', 'L'): 50,
            Part('q', 'L'): 1,
            Part('x', 'L'): 1177,
        })

    # add
    def test_add(self) -> None:
        self.design_repository.add(
            Design('B', 'L', {
                Part('x', 'L'): 1,
                Part('y', 'L'): 1,
                Part('z', 'L'): 1,
            }, 4)
        )

        expected = [
            Design('B', 'L', {
                Part('x', 'L'): 1,
                Part('y', 'L'): 1,
                Part('z', 'L'): 1,
            }, 4)
        ]
        self.assertEqual(self.design_repository.designs, expected)

    # add_parts
    def test_add_parts(self) -> None:
        self.design_repository.add_parts({
            Part('a', 'S'): 1,
            Part('b', 'S'): 9,
            Part('e', 'S'): 21
        })
        expected = {
            Part('a', 'S'),
            Part('b', 'S'),
            Part('e', 'S'),
        }
        self.assertEqual(self.design_repository.parts_in_designs, expected)

        self.design_repository.add_parts({
            Part('a', 'S'): 2,
            Part('g', 'S'): 2,
            Part('j', 'S'): 10,
        })
        expected = {
            Part('a', 'S'),
            Part('b', 'S'),
            Part('e', 'S'),
            Part('g', 'S'),
            Part('j', 'S'),
        }
        self.assertEqual(self.design_repository.parts_in_designs, expected)


if __name__ == "__main__":
    unittest.main()
