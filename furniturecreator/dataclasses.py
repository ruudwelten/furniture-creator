"""Furniture Creator's dataclasses."""

from __future__ import annotations
from typing import Dict
from dataclasses import dataclass


@dataclass(frozen=True)
class Part:
    """Part for creating Products from multiple Parts."""

    type: str
    size: str

    def __str__(self) -> str:
        """Output readable representation (eg. 'aS')."""
        return f'{self.type}{self.size}'


@dataclass
class Product:
    """Product consisting of multiple Parts, based on Design."""

    name: str
    size: str
    parts: Dict[Part, int]

    def __str__(self) -> str:
        """Output readable representation (eg. '[Name]S1a2b3c')."""
        parts = ''.join(
            '{}{}'.format(amount, part.type)
            for part, amount in
                sorted(self.parts.items(), key=lambda x: x[0].type)
        )
        return f'[{self.name}]{self.size}{parts}'

    def add_part(self, part: Part, amount: int = 1):
        """Add a Part to the Product."""
        self.parts[part] = self.parts.get(part, 0) + amount


@dataclass(frozen=True)
class Design:
    """Design to produce Products by these Designs."""

    name: str
    size: str
    parts: Dict[Part, int]
    total_parts: int

    def __str__(self) -> str:
        """Output readable representation (eg. '[Name]S1a2b3c10')."""
        parts = ''.join(
            '{}{}'.format(amount, part.type)
            for part, amount in
                sorted(self.parts.items(), key=lambda x: x[0].type)
        )
        return f'[{self.name}]{self.size}{parts}{self.total_parts}'
