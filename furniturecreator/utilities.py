"""Furniture Creator global utility functions."""

from __future__ import annotations
from typing import List, Dict

from furniturecreator.dataclasses import Part


def filter_parts_list_by_size(
        parts: List[Part],
        size: str) -> List[Part]:
    """Filter a list of parts by size."""
    if size != 'S' and size != 'L':
        raise ValueError(f'''Wrong size supplied: {'size'}. Should be
            either of: [S]mall or [L]arge.''')
    return [f for f in parts if f.size == size]


def filter_parts_dict_by_size(
        parts: Dict[Part, int],
        size: str) -> Dict[Part, int]:
    """Filter a dict of parts by size."""
    if size != 'S' and size != 'L':
        raise ValueError(f'''Wrong size supplied: {'size'}. Should be
            either of: [S]mall or [L]arge.''')
    return {f: n for f, n in parts.items() if f.size == size}
