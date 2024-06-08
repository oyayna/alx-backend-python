#!/usr/bin/env python3

"""
    make multiplier (callback function)
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        return a callback function
    """
    def fun(n: float) -> float:
        return n * multiplier
    return fun
