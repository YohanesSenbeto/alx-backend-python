#!/usr/bin/env python3

import time
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns

    Args:
        n: The number of calls to wait_n.
        max_delay: The maximum delay for each call to wait_n.

    Returns:
        The average execution time per call in seconds (float).
    """

    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed_time = time.perf_counter() - first_time
    total_time = elapsed_time / n

    return total_time
