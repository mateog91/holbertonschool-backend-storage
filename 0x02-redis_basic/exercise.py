#!/usr/bin/env python3
"""Module for task 0"""
import redis
from typing import Union
import uuid
redis_host = 'localhost'
redis_port = 6379


class Cache():
    def __init__(self):
        try:
            self._redis = redis.Redis(
                host=redis_host, port=redis_port, decode_responses=True)
            self._redis.flushdb
        except Exception as e:
            print(e)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
