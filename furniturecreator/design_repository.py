"""Furniture Creator's product design repository."""

from __future__ import annotations
from typing import Set, List, Dict
import re

from furniturecreator.dataclasses import Part, Design


class DesignRepository:
    """Processes and tracks product designs."""

    def __init__(self) -> None:
        """Initialize empty design list and parts set."""
        self.designs: List[Design] = []
        self.parts_in_designs: Set[Part] = set()
        self.index = 0

    def __iter__(self) -> DesignRepository:
        """Return self as Iterator object."""
        return self

    def __next__(self) -> Design:
        """Return the next Design from DesignRepository list."""
        if self.index < len(self.designs):
            result = self.designs[self.index]
            self.index += 1
            return result
        self.index = 0
        raise StopIteration

    def save(self, design_str: str) -> None:
        """Pass design into parser and store result internally."""
        design = self.parse_design(design_str)
        self.add(design)

    def parse_design(self, design_str: str) -> Design:
        """Parse and convert design string into a Design object."""
        if not (match := re.match(
            r'^\[(.+)\]([SL])((?:\d+[a-z])+)(\d+)$',
            design_str
        )):
            raise ValueError(
                f'Incorrect design format (\'{design_str}\').')

        name = match.group(1)
        size = match.group(2)
        parts_str = match.group(3)
        total_parts = int(match.group(4))

        parts = self.parse_parts(parts_str, size)

        return Design(name, size, parts, total_parts)

    def parse_parts(self, parts_str: str, size: str) -> Dict[Part, int]:
        """Parse string of parts and convert it into a Dict of Part objects."""
        parts = {}
        for part_match in re.finditer(r'(\d+[a-z])', parts_str):
            part_type = part_match.group(1)[-1:]
            part_amount = int(part_match.group(1)[:-1])
            parts[Part(part_type, size)] = part_amount

        return parts

    def add(self, design: Design) -> None:
        """Add design and its parts to internal list."""
        self.add_parts(design.parts)
        self.designs.append(design)

    def add_parts(self, parts: Dict[Part, int]) -> None:
        """Add parts to internal list."""
        for part in parts.keys():
            self.parts_in_designs.add(part)

    def get_parts_in_designs(self) -> Set[Part]:
        """Get all parts in designs."""
        return self.parts_in_designs

    def select_design_for_creation(self) -> Design:
        """Return product design, reset iter and move design to end of list."""
        design = self.designs[self.index - 1]
        self.designs.append(self.designs.pop(self.index - 1))
        self.index = 0
        return design
