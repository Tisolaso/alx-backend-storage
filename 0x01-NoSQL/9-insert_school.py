#!/usr/bin/env python3

"Inser new Document to a collection"


def insert_school(mongo_collection, **kwargs):
    return mongo_collection.insert_one(kwargs)._id
