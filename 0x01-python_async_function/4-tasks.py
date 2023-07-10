#!/usr/bin/env python3
"""Executing multiple coroutines"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """return a list of values in async"""
    seconds_list = []
    for _ in range(0, n):
        seconds_list.append(task_wait_random(max_delay))
    return await asyncio.gather(*seconds_list)
