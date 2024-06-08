#!/usr/bin/env python3

"""
    function return string and square of a number
"""

from typing import Union, Tuple


def to_kv(K: str, v: Union[int, float]) -> Tuple[str, float]:

    """
        return tuple of K and v
    """
    return (K, v * v)
