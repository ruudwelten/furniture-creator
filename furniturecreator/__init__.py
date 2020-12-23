"""Furniture Creator package for technical challenge.

This command line application for a simplified furniture production facility is
created for a technical challenge. It can be run in a Docker container and
accepts product designs and parts as input through standard input (see
README.md) and outputs products whenever one can be created from the current
parts in stock.
"""

from __future__ import annotations
from typing import Iterator
import sys

from furniturecreator.part_repository import PartRepository
from furniturecreator.product_manager import ProductManager


class FurnitureCreator:
    """Furniture Creator main class.

    Run FurnitureCreator.main() to start the furniture creator.
    """

    def __init__(self) -> None:
        """Initialize the application."""
        self.part_repository = PartRepository()
        self.product_manager = ProductManager(self.part_repository)

    def main(self) -> None:
        """Start the furniture creator."""
        for design_str in self.read_design():
            self.product_manager.save_design(design_str)
        for part_str in self.read_part():
            self.part_repository.save(part_str)

            if product := self.product_manager.create_product():
                print(product)

    def read_stdin(self) -> Iterator[str]:
        """Read standard input and yield line by line."""
        for line in sys.stdin:
            yield line.strip()

    def read_design(self) -> Iterator[str]:
        """Retrieve product designs from STDIN before the first empty line."""
        for design_str in self.read_stdin():
            # Upon reaching empty line stop reading product designs as
            # following lines contain parts only.
            if not design_str:
                return
            yield design_str

    def read_part(self) -> Iterator[str]:
        """Retrieve parts from STDIN after the first empty line."""
        yield from self.read_stdin()
