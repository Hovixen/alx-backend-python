#!/usr/bin/env python3
"""
Type-annotated function sum_list
"""
from typing import List


def sum_list(n: List[float]) -> float:
    """ function takes a list as argument and returns their sum """
    return sum(n)
