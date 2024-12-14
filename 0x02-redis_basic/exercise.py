#!/usr/bin/env python3
"""Redis module for cache"""

import uuid
from typing import Union, Callable

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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """get data from redis db"""

        data = self._redis.get(key)
        if not fn:
            if type(data) is str:
                return self.get_str(key)
            if type(data) is int:
                return self.get_int(key)

        return fn(data)

    def get_str(self, key: str) -> str:
        """get string data"""
        data = self._redis.get(key)
        return str(data)

    def get_int(self, key: str) -> int:
        """get integer data"""
        data = self._redis.get(key)
        return int(data)
