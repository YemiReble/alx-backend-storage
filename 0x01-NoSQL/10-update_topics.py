#!/usr/bin/env python3
"""
This is a script that changes all topics
of a school document based on the name
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """ A Function that updates topics """
    change = mongo_collection.update(name)
    return change.insert(topics)
