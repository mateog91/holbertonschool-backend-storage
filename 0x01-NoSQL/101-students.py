#!/usr/bin/env python3
""" Module for task 12 """
from operator import itemgetter


def top_students(mongo_collection):
    """
    top_students function that returns all students sorted by average score:

    Args:
        mongo_collection will be the pymongo collection object

    Returns:
        top_students: List of students sorted by average score
    """

    students = mongo_collection.find()
    l_students = []
    for student in students:
        scores = []
        topics = student.get('topics')
        scores = [topic.get('score')for topic in topics]
        average_score = float(sum(scores) / len(scores))
        student['averageScore'] = average_score
        l_students.append(student)
        print(l_students)

    top_students = sorted(l_students, key=itemgetter(
        'averageScore'), reverse=True)
    return top_students
