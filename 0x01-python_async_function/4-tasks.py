#!/usr/bin/env python3
"""
Module for working with asyncio Tasks
"""
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_dely
    seconds and eventually returns it.
    """
    return await wait_n(n, max_delay)
