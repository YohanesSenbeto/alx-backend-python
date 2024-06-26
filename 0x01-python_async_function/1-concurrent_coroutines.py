#!/usr/bin/env python3
"""
Module for executing multiple coroutines concurrently
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

<<<<<<< HEAD

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> list:
=======

async def wait_n(n: int, max_delay: int) -> List[float]:
>>>>>>> 0a61e29a5a9448d816320f5b3df8016d2d8e874e
    """
    Asynchronous routine that spawns wait_random n times with the specified m
    Returns the list of all the delays (float values) in ascending order.
    """
    return sorted([await wait_random(max_delay) for _ in range(n)])
