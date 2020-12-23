from __future__ import annotations
import unittest

from furniturecreator.dataclasses import Part, Product, Design
from furniturecreator.part_repository import PartRepository
from furniturecreator.product_manager import ProductManager


class TestProductManager(unittest.TestCase):

    def setUp(self):
        self.part_repository = PartRepository()
        self.manager = ProductManager(self.part_repository)
        self.maxDiff = None

    def tearDown(self):
        del self.manager

    # create_product
    def test_create_product(self) -> None:
        self.manager.save_design('[Chair]S1a1b1c4')
        self.part_repository.save('aS')
        self.part_repository.save('bS')
        self.part_repository.save('cS')

        self.assertIsNone(self.manager.create_product())

        self.part_repository.save('dS')

        expected = Product('Chair', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 1,
            Part('c', 'S'): 1,
            Part('d', 'S'): 1
        })
        self.assertEqual(self.manager.create_product(), expected)

    # select_extra_part
    def test_select_extra_part(self) -> None:
        self.manager.save_design('[Bookcase]S1a1b1c4')
        self.part_repository.save('aS')
        self.part_repository.save('bS')
        self.part_repository.save('bS')
        self.part_repository.save('cS')
        self.assertEqual(
            self.manager.select_extra_part('S'),
            Part('b', 'S')
        )
        self.part_repository.save('dS')
        self.assertEqual(
            self.manager.select_extra_part('S'),
            Part('d', 'S')
        )

    # select_design
    def test_select_design(self) -> None:
        self.manager.save_design('[Chair]S1a1b1c4')
        self.part_repository.save('aS')
        self.part_repository.save('bS')
        self.part_repository.save('cS')

        self.assertIsNone(self.manager.select_design())

        self.part_repository.save('dS')

        expected = Design('Chair', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 1,
            Part('c', 'S'): 1
        }, 4)
        self.assertEqual(self.manager.select_design(), expected)

    # enough_stock_for_design
    def test_enough_stock_for_design(self) -> None:
        self.part_repository.save('aS')
        self.part_repository.save('bS')
        self.part_repository.save('cS')

        input = Design('Table', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 1,
            Part('c', 'S'): 1,
        }, 4)

        result = self.manager.enough_stock_for_design(input)
        self.assertFalse(result)

        self.part_repository.save('dS')

        result = self.manager.enough_stock_for_design(input)
        self.assertTrue(result)

    # get_all_parts_in_stock_without_design
    def test_get_all_parts_in_stock_without_design(self) -> None:
        self.manager.save_design('[Chair]S1a1b1c4')
        self.part_repository.save('aS')
        self.part_repository.save('bS')
        self.part_repository.save('cS')

        self.assertFalse(
            self.manager.get_all_parts_in_stock_without_design()
        )

        self.part_repository.save('dS')
        self.part_repository.save('eS')

        self.assertEqual(
            self.manager.get_all_parts_in_stock_without_design(),
            [Part('d', 'S'), Part('e', 'S')]
        )


if __name__ == "__main__":
    unittest.main()
