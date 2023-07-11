#!/usr/bin/env python3
"""async comprehension module"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension function"""
    numbers = [x async for x in async_generator()]
    return numbers
