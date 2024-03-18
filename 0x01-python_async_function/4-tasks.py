#!/usr/bin/env python3
"""
Module for working with asyncio Tasks
"""

import asyncio
import random

async def wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values).
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
