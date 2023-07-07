#!/usr/bin/python3 env
"""8-make_multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier function"""
    def fun(x: float) -> float:
        return x * multiplier
    return fun
