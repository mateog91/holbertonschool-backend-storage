#!/usr/bin/env python3
""" Module for task 12 """
from pymongo import MongoClient

if __name__ == "__main__":
    # Initialize the database
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Initialize list of methos
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Get total
    number_of_logs = nginx_collection.count_documents({})

    # Get count by methods

    count_by_methods = [nginx_collection.count_documents({"method": method}) for method in methods]

    count_status = nginx_collection.count_documents({"path":"/status"})

    # Prints
    print(f"{number_of_logs} logs")
    print("Methods:")
    # number_of_documents = len(documents)
    for method, count in zip(methods, count_by_methods):
        print(f"    method {method}: {count}")
    print(f"{count_status} status check")
