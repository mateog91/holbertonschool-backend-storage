#!/usr/bin/env python3
""" Module for task 102 """
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

    count_by_methods = [nginx_collection.count_documents(
        {"method": method}) for method in methods]

    count_status = nginx_collection.count_documents({"path": "/status"})

    # Prints
    print("{} logs".format(number_of_logs))
    print("Methods:")
    # number_of_documents = len(documents)
    for method, count in zip(methods, count_by_methods):
        print("\tmethod {}: {}".format(method, count))
    print("{} status check".format(count_status))

    # ADVANCED

    # Get all logs
    all_logs = nginx_collection.find()

    # Create a dictionary wit {ip: count} structure
    ips_dict = {}
    for log in all_logs:
        current_ip = log.get('ip')
        if current_ip:
            if current_ip not in ips_dict:
                ips_dict[current_ip] = 1
            else:
                ips_dict[current_ip] += 1

    # Create list of tupple [(ip, count)] structure
    ips_tupple = list(ips_dict.items())
    # Sort list by counts
    ips_tupple.sort(key=lambda x: x[1], reverse=True)

    # Print
    print("IPs:")
    for i in range(10):
        current_ip = ips_tupple[i]
        ip, count = current_ip[0], current_ip[1]
        print("\t{}: {}".format(ip, count))
