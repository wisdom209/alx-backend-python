#!/usr/bin/env python3
"""async generator module"""
import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """generator coroutine"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)