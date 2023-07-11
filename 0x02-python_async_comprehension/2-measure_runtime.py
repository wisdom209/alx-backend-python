#!/usr/bin/env python3
"""parallel async_comprehension"""
import asyncio
import time
async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure function runtime"""
    start = time.time()
    t = asyncio.create_task(async_comprehension())
    func_list = [t for _ in range(4)]
    await asyncio.gather(*func_list)
    end = time.time()
    total_time = end - start
    return total_time
