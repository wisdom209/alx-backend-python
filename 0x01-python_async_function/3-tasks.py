#!/usr/bin/python3 env
"""return an asyncio task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """wait randomly"""
    return asyncio.create_task(wait_random(max_delay))
