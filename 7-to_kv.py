#!/usr/bin/env python3
"""
Function that convert string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
        '''Convert a string and int/float to tuple.'''
        return (k, v ** 2)
