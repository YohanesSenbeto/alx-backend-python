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

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that creates and returns an asyncio.Task for wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
