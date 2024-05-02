#!/usr/bin/env python3
"""
Type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function takes a float and returns a function that multiplies
    a float
    """

    def multi_function(x: float) -> float:
        """ inner functio that multiplies a float by a given multiplier """
        return multiplier * x
    return multi_function
