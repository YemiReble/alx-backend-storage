#!/usr/bin/env python3
""" A python Cache """


import uuid
import redis


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
