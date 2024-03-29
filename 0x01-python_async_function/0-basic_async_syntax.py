#!/usr/bin/env python3

"""
Ssynchronous coroutine that takes in an integer argument
that waits for a random delay between 0
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay
    (included and float value) seconds
    """
    rand_number = random.uniform(0, max_delay)
    await asyncio.sleep(rand_number)
    return rand_number
