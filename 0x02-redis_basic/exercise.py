#!/usr/bin/env python3
""" A python Cache """


import uuid
import redis
from typing import Callable
# from collections.abc import Callable


class Cache():
    """ A Cache Class """
    def __init__(self):
        """ Instantiate the class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str) -> str:
        """ Store the data in Redis using a key """
        key = uuid.uuid4().hex
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[], str]) -> str:
        """ Get method """
        self._redis.get(key)

    def get_str(self, key: str) -> str:
        """ For getting cache strings """
        self.get(key, str)

    def get_int(self, key: int) -> int:
        """ For geting cache integer """
        self.get(key, int)
