#!/usr/bin/env python3
"""Redis module for cache"""

import uuid
from typing import Union

import redis


class Cache:
    """Cache base class for redis DB"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data into redis db"""
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key
