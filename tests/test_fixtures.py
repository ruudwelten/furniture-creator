from __future__ import annotations
import unittest
import sys
import io

from tests.test_furniturecreator import TestFurnitureCreator


class TestFixtures(unittest.TestCase):

    # fixture_stdin_one_line_type
    def test_fixture_stdin_one_line(self) -> None:
        tfc = TestFurnitureCreator()
        tfc.fixture_stdin_one_line()
        self.assertIsInstance(sys.stdin, io.TextIOWrapper)
        for line in sys.stdin:
            self.assertEqual(line.strip(), '[Cabinet]L20a15c45')

    # fixture_stdin_multi_line_type
    def test_fixture_stdin_multi_line(self) -> None:
        tfc = TestFurnitureCreator()
        tfc.fixture_stdin_multi_line()
        self.assertIsInstance(sys.stdin, io.TextIOWrapper)
        expected = ['[Cabinet]L20a15c45', '[Couch]S16b8k3z27',
                    '',
                    'cL', 'zS', 'aS', 'aL', 'cL', 'zS']

        i = 0
        for line in sys.stdin:
            self.assertEqual(line.strip(), expected[i])
            i += 1


if __name__ == "__main__":
    unittest.main()
