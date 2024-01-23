#!/usr/bin/env python3
"""
Defines the top_students function
"""


def top_students(mongo_collection):
    """the function selects students by score """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
