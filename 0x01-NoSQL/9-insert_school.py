#!/usr/bin/env python3
""" Python script that create a function
that inserts a new document in a collection
based on kwargs
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """ A function that inserts a new document in a
    Database colletion
    """
    return mongo_collection.insert(kwargs)
