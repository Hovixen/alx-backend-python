#!/usr/bin/env python3
"""
Type-annotated function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of v as a float.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v.
    """
    return (k, float(v) ** 2)
