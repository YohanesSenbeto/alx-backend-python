#!/usr/bin/env python3
"""
Fuction that make multi pliea
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
        '''Return a function that multiplies a float by multiplier.'''
            def multiplier_function(n: float) -> float:
                return n * multiplier
                    return multiplier_function
