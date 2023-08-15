#!/usr/bin/env python3
"""
This is a MongoDB Pyhton method that display
all document in a collection
"""


import pymongo
import pprint


def list_all(mongo_collection):
    """
    This function returns the document of a
    collection and if collection is empty, it
    retuns and empty list
    """
    if mongo_collection is None:
        return []

    all_datas = mongo_collection.find()
    return [all_data for all_data in all_datas]

