#!/usr/bin/env python3

import time
import asyncio
<<<<<<< HEAD
from time import time
from 1 - concurrent_coroutines import wait_n

=======
from typing import List
>>>>>>> 0a61e29a5a9448d816320f5b3df8016d2d8e874e

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
