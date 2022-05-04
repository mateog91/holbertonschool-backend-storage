#!/usr/bin/env python3
"""Module for task 0"""
import redis
import uuid
from typing import Union


class Cache():
    """
    Cache class
    """

    def __init__(self):
        """Class constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store stores data into redis

        Args:
            data (Union[str, bytes, int, float]): data to store

        Returns:
            str: uuid key generated where data was stored
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
