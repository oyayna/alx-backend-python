#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Asynchronous generator that yields a random
    number between 0 and 10 after waiting for 1 second.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
