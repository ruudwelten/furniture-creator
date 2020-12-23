from __future__ import annotations
import unittest
import sys
import io

from furniturecreator import FurnitureCreator


class TestFurnitureCreator(unittest.TestCase):

    def setUp(self):
        self.app = FurnitureCreator()

    def fixture_stdin_one_line(self) -> None:
        wrapper = io.TextIOWrapper(io.BytesIO())
        wrapper.write('[Cabinet]L20a15c45\n')
        wrapper.seek(0, 0)
        sys.stdin = wrapper

    def fixture_stdin_multi_line(self) -> None:
        wrapper = io.TextIOWrapper(io.BytesIO())
        wrapper.write('\n'.join(
            ['[Cabinet]L20a15c45', '[Couch]S16b8k3z27', '',
             'cL', 'zS', 'aS', 'aL', 'cL', 'zS']
        ))
        wrapper.seek(0, 0)
        sys.stdin = wrapper

    # read_stdin
    def test_read_stdin_one_line(self) -> None:
        self.fixture_stdin_one_line()
        self.assertEqual(list(self.app.read_stdin()), ['[Cabinet]L20a15c45'])

    def test_read_stdin_multi_line(self) -> None:
        self.fixture_stdin_multi_line()
        self.assertEqual(
            list(self.app.read_stdin()),
            ['[Cabinet]L20a15c45', '[Couch]S16b8k3z27', '',
             'cL', 'zS', 'aS', 'aL', 'cL', 'zS']
        )

    # read_design
    def test_read_design_one_line(self) -> None:
        self.fixture_stdin_one_line()
        self.assertEqual(list(self.app.read_design()), ['[Cabinet]L20a15c45'])

    def test_read_design_multi_line(self) -> None:
        self.fixture_stdin_multi_line()
        self.assertEqual(
            list(self.app.read_design()),
            ['[Cabinet]L20a15c45', '[Couch]S16b8k3z27']
        )

    # read_part
    def test_read_part(self) -> None:
        self.fixture_stdin_multi_line()
        for i in self.app.read_design():
            pass
        self.assertEqual(
            list(self.app.read_design()),
            ['cL', 'zS', 'aS', 'aL', 'cL', 'zS']
        )


if __name__ == "__main__":
    unittest.main()
