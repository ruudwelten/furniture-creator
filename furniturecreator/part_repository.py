"""Furniture Creator's product parts repository."""

from __future__ import annotations
from typing import List, Dict, Union
import re
from operator import itemgetter

from furniturecreator.dataclasses import Part
from furniturecreator.utilities import filter_parts_dict_by_size


class PartRepository:
    """Processes and tracks parts in stock."""

    def __init__(self) -> None:
        """Initialize empty parts dictionary and empty totals."""
        self.parts: Dict[Part, int] = {}
        self.total_per_size: Dict[str, int] = {'S': 0, 'L': 0}

    def __str__(self) -> str:
        """Create plain text representation of current stock for humans."""
        stock = '\n'.join(
            '{}: {}'.format(part, amount)
            for part, amount in
                sorted(
                    self.parts.items(),
                    key=lambda x: x[0].type
                )
        )
        total = self.sum_stock()
        return f'{stock}\nTotal: {total}'

    def save(self, part_str: str) -> None:
        """Convert text format part into Part object and store it."""
        if not re.match(r'^[a-z][SL]$', part_str):
            raise ValueError(f'Incorrect part format (\'{part_str}\').')
        self.add(Part(part_str[0], part_str[1]))

    def add(self, part: Part, amount: int = 1) -> None:
        """Add part to internal dictionary and raise total."""
        if amount < 1:
            raise ValueError('Can not add less than one part.')
        self.parts[part] = self.sum_stock(part) + amount
        self.total_per_size[part.size] += amount

    def remove(self, part: Part, amount: int = 1) -> None:
        """Remove part from internal dictionary and decrease total."""
        if amount < 1:
            raise ValueError('Can not remove less than one part.')
        if amount > self.sum_stock(part):
            raise ValueError(
                f'''Not enough parts in stock to remove
                ({amount} > {self.parts.get(part, 0)}.'''
            )
        self.parts[part] = self.sum_stock(part) - amount
        if self.parts[part] == 0:
            del self.parts[part]
        self.total_per_size[part.size] -= amount

    def sum_stock(self, selection: Union[str, Part] = 'A') -> int:
        """Return sum of all parts in stock for given selection."""
        if isinstance(selection, str) and selection == 'A':
            return self.sum_all_stock()
        elif isinstance(selection, str):
            return self.sum_size_stock(selection)
        return self.sum_part_stock(selection)

    def sum_all_stock(self) -> int:
        """Return sum of all parts in stock."""
        return sum(self.parts.values())

    def sum_size_stock(self, size: str) -> int:
        """Return sum of all parts in stock for given size."""
        if size == 'S' or size == 'L':
            return self.total_per_size[size]
        raise ValueError('sum_size_stock() only accepts [S]mall or [L]arge.')

    def sum_part_stock(self, part: Part) -> int:
        """Return sum of specified part in stock."""
        return self.parts.get(part, 0)

    def get_part_list(self) -> List[Part]:
        """Return a list of all parts in stock."""
        return list(self.parts.keys())

    def get_part_with_most_in_stock(self, size: str = '') -> Part:
        """Return the part of which there are the most of in stock."""
        scope = self.parts
        if size:
            scope = filter_parts_dict_by_size(self.parts, size)
        return max(scope.items(), key=itemgetter(1))[0]
