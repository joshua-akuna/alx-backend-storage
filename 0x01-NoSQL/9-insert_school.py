#!/usr/bin/env python3
"""
The module defines the insert_school function
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserts a document into a collection
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
