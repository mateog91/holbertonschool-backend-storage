#!/usr/bin/env python3
"""Module for task 11"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school having a specific topic:

    Args:
        mongo_collection: pymongo collection object
        topic (string): will be topic searched
    """
    results = mongo_collection.find({"topics": topic})
    return results
