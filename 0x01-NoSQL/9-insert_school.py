#!/usr/bin/env python3
"""Module for task 9"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs:

    Args:
        mongo_collection: pymongo collection object

    Returns:
        new _id
    """
    new_doc = mongo_collection.insert_one(kwargs)
    _id = new_doc.inserted_id
    return _id
