#!/usr/bin/env python3

import asyncio
from 1-concurrent_coroutines import wait_n

async def main():
    print(await wait_n(5, 5))
    print(await wait_n(10, 7))
    print(await wait_n(10, 0))

asyncio.run(main())
