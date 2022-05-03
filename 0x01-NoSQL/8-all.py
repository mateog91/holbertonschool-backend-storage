#!/usr/bin/env python3
"""Module for task 8"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    list_all lists all documents in a collection:

    Args:
        mongo_collection: a collection in mongo database

    Returns:
        Return a list with all documents in a collection.
        Return an empty list if no document in the collection
    """
    lst = list(mongo_collection.find())
    if not lst:
        return []

    return lst
