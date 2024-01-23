#!/usr/bin/env python3
"""
The module defines the update_topics function
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    updates a document with an attribute and value
    """
    return mongo_collection.update_many({
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })
