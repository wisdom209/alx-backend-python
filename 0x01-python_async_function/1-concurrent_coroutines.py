#!/usr/bin/env python3
"""Executing multiple coroutines"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """return a list of values in async"""
    seconds_list = []
    for _ in range(0, n):
        seconds_list.append(wait_random(max_delay))
    return await asyncio.gather(*seconds_list)
