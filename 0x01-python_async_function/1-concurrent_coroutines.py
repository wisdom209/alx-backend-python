#!/usr/bin/env python3
"""Executing multiple coroutines"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return a list of values in async"""
    seconds_list = []
    for _ in range(0, n):
        sec = await wait_random(max_delay)
        seconds_list.append(sec)
    return seconds_list
