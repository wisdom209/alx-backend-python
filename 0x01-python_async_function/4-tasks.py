#!/usr/bin/env python3
"""Executing multiple coroutines"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return a list of values in async"""
    seconds_list = []
    for _ in range(0, n):
        sec = await task_wait_random(max_delay)
        seconds_list.append(sec)
    return seconds_list
