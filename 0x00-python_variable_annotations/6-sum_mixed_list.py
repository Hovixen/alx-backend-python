#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function returns the sum of the given list argument """
    return sum(mxd_lst)
