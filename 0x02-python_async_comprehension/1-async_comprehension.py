#!/usr/bin/env python3
"""
Async Comprehension file
"""

from typing import List
from asyncio import gather

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension funct
    """
    return [i async for i in async_generator()]
