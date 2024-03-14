#!/usr/bin/env python3
"""
Function that return list of tuple
"""
from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
        '''Return a list of tuples containing elements and their lengths.'''
        return [(i, len(i)) for i in lst]
