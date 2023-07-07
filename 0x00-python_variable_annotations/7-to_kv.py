#!/usr/bin/env python3
"""7-to_kv module"""
from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """7-to_Kv function"""
    second_arg: float = math.pow(v, 2)
    return (k, second_arg)
