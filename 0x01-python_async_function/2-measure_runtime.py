#!/usr/bin/env python3

import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns

    Args:
        n: The number of calls to wait_n.
        max_delay: The maximum delay for each call to wait_n.

    Returns:
        The average execution time per call in seconds (float).
    """

    start_time = time.time()

    wait_n(n, max_delay)

    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
