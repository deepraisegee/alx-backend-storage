#!/usr/bin/python3
"""A python coroutine file"""
import asyncio
import random


async def wait_random(max_delay=10):
    """perform some calculations"""
    wait_second = random.uniform(0, max_delay)
    await asyncio.sleep(wait_second)
    return wait_second


if __name__ == "__main__":
    asyncio.run(wait_random())