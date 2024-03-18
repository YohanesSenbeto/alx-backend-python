#!/bin/bash

# Create README.md
echo "# Python Async Functions\nThis repository contains Python scripts demonstrating asynchronous functions and coroutines.\n" > README.md

# Task 0: The basics of async
cat << 'EOF' > 0-basic_async_syntax.py
#!/usr/bin/env python3
"""
Basic asynchronous syntax module
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
EOF

cat << 'EOF' > 0-main.py
#!/usr/bin/env python3

import asyncio
from 0-basic_async_syntax import wait_random

async def main():
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))

asyncio.run(main())
EOF

# Task 1: Let's execute multiple coroutines at the same time with async
cat << 'EOF' > 1-concurrent_coroutines.py
#!/usr/bin/env python3
"""
Module for executing multiple coroutines concurrently
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> list:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values) in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
EOF

cat << 'EOF' > 1-main.py
#!/usr/bin/env python3

import asyncio
from 1-concurrent_coroutines import wait_n

async def main():
    print(await wait_n(5, 5))
    print(await wait_n(10, 7))
    print(await wait_n(10, 0))

asyncio.run(main())
EOF

# Task 2: Measure the runtime
cat << 'EOF' > 2-measure_runtime.py
#!/usr/bin/env python3
"""
Module for measuring the runtime of asynchronous functions
"""

import asyncio
from time import time
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns total_time / n.
    """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
EOF

cat << 'EOF' > 2-main.py
#!/usr/bin/env python3

from 2-measure_runtime import measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
EOF

# Task 3: Tasks
cat << 'EOF' > 3-tasks.py
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
EOF

cat << 'EOF' > 3-main.py
#!/usr/bin/env python3

import asyncio
from 3-tasks import task_wait_random

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
EOF

# Task 4: Tasks
cat << 'EOF' > 4-tasks.py
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
EOF

cat << 'EOF' > 4-main.py
#!/usr/bin/env python3

import asyncio
from 4-tasks import task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
EOF

# Set executable permissions
chmod +x *.py
