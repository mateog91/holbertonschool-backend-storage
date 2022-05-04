#!/usr/bin/env python3
"""Module for task 0"""
import redis
from typing import Union
import uuid


class Cache():
    """
    Cache class
    """
    def __init__(self):
        """Class constructor"""
        try:
            self._redis = redis.Redis()
            self._redis.flushdb
        except Exception as e:
            print(e)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store stores data into redis

        Args:
            data (Union[str, bytes, int, float]): data to store

        Returns:
            str: uuid key generated where data was stored
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
