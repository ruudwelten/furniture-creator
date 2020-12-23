from __future__ import annotations
import unittest

from furniturecreator.dataclasses import Part, Product, Design


class TestFurnitureCreatorDataClasses(unittest.TestCase):

    # Part
    def test_part_compare(self) -> None:
        self.assertEqual(Part('c', 'S'), Part('c', 'S'))
        self.assertEqual(Part('m', 'L'), Part(size='L', type='m'))

    def test_part_compare_different(self) -> None:
        self.assertNotEqual(Part('c', 'S'), Part('c', 'L'))

    def test_part_str(self) -> None:
        part = Part('a', 'L')
        self.assertEqual(part.__str__(), 'aL')

    # Product
    def test_product_compare(self) -> None:
        product1 = Product('Lounge chair', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 10,
            Part('c', 'S'): 6,
        })
        product2 = Product('Lounge chair', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 10,
            Part('c', 'S'): 6,
        })
        self.assertEqual(product1, product2)

    def test_product_compare_different(self) -> None:
        product1 = Product('Lounge chair', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 10,
            Part('c', 'S'): 6,
        })
        product2 = Product('Couch', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 11,
            Part('c', 'S'): 6,
        })
        self.assertNotEqual(product1, product2)

    def test_product_str(self) -> None:
        product = Product('Side table', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 10,
            Part('c', 'S'): 6,
        })
        self.assertEqual(product.__str__(), '[Side table]S1a10b6c')

    # Design
    def test_design_compare(self) -> None:
        product1 = Design('Chair', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 10,
            Part('c', 'S'): 6,
        }, 20)
        product2 = Design('Chair', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 10,
            Part('c', 'S'): 6,
        }, 20)
        self.assertEqual(product1, product2)

    def test_design_compare_different(self) -> None:
        product1 = Design('Bed', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 10,
            Part('c', 'S'): 6,
        }, 20)
        product2 = Design('Table', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 11,
            Part('c', 'S'): 6,
        }, 20)
        self.assertNotEqual(product1, product2)

    def test_design_str(self) -> None:
        product = Design('Bed', 'S', {
            Part('a', 'S'): 1,
            Part('b', 'S'): 10,
            Part('c', 'S'): 6,
        }, 20)
        self.assertEqual(product.__str__(), '[Bed]S1a10b6c20')


if __name__ == "__main__":
    unittest.main()
