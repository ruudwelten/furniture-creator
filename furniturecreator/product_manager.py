"""Furniture Creator's product manager."""

from __future__ import annotations
from typing import List, Optional
import random

from furniturecreator.dataclasses import Part, Product, Design
from furniturecreator.utilities import filter_parts_list_by_size
from furniturecreator.part_repository import PartRepository
from furniturecreator.design_repository import DesignRepository


class ProductManager:
    """Processes designs and creates products from parts in stock."""

    def __init__(self, part_repository: PartRepository) -> None:
        """Initialize Stock and design repository.

        Part repository must be supplied, empty
        design repository will be created.
        """
        self.part_repository: PartRepository = part_repository
        self.design_repository: DesignRepository = DesignRepository()

    def save_design(self, design_str: str) -> None:
        """Pass design to design repository."""
        self.design_repository.save(design_str)

    def create_product(self) -> Optional[Product]:
        """Create a new product.

        If enough parts are in stock for a design, create it
        otherwise return None.
        """
        if not (design := self.select_design()):
            return None

        product = Product(design.name, design.size, {})

        for part, amount in design.parts.items():
            self.part_repository.remove(part, amount)
            product.add_part(part, amount)

        extra_parts = design.total_parts - sum(design.parts.values())
        while extra_parts > 0:
            extra_part = self.select_extra_part(design.size)

            product.add_part(extra_part, 1)
            self.part_repository.remove(extra_part)
            extra_parts -= 1

        return product

    def select_extra_part(self, size: str) -> Part:
        """Select and return the part best suited to complete a product."""
        # First select all parts in stock that are not included in any
        # product design, filtered by size. If there are none left without
        # a product design, choose the part with most in stock.
        parts_without_design = filter_parts_list_by_size(
            self.get_all_parts_in_stock_without_design(),
            size
        )
        extra_part: Part
        if parts_without_design:
            extra_part = random.choice(parts_without_design)
        else:
            extra_part = self.part_repository.get_part_with_most_in_stock(size)

        return extra_part

    def select_design(self) -> Optional[Design]:
        """Select a product design to be created from stock or return None."""
        for design in self.design_repository:
            if self.enough_stock_for_design(design):
                return self.design_repository.select_design_for_creation()
        return None

    def enough_stock_for_design(self, design: Design) -> bool:
        """Check if enough parts are in stock for the specified design."""
        if self.part_repository.sum_stock(design.size) < design.total_parts:
            return False
        for part, amount in design.parts.items():
            if self.part_repository.sum_stock(part) < amount:
                return False
        return True

    def get_all_parts_in_stock_without_design(self) -> List[Part]:
        """Return all parts in stock that are not included in a design."""
        all_parts = self.part_repository.get_part_list()
        return [x for x in all_parts
                if x not in self.design_repository.get_parts_in_designs()]
