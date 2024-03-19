#!/usr/bin/env python3

import asyncio
import random


async def async_generator():
    """
    Coroutine that generates random numbers asynchronously.

    Loops 10 times, each time asynchronously waits for 1 second,
    then yields a random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
