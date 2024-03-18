#!/usr/bin/env python3
"""
Measure runtime module
"""

from typing import Callable
import asyncio


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    """
    start_time = asyncio.get_event_loop().time()
    await __import__('1-concurrent_coroutines').wait_n(n, max_delay)
    end_time = asyncio.get_event_loop().time()
    total_time = end_time - start_time
    return total_time / n
