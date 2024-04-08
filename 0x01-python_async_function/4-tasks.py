#!/usr/bin/env python3
"""
Module for working with asyncio Tasks
"""
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

<<<<<<< HEAD

async def wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> list:
=======

async def task_wait_n(n: int, max_delay: int) -> List[float]:
>>>>>>> 0a61e29a5a9448d816320f5b3df8016d2d8e874e
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_dely
    seconds and eventually returns it.
    """
    return await wait_n(n, max_delay)
