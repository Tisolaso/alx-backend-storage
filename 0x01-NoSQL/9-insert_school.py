#!/usr/bin/env python3

"Inser new Document to a collection"


def insert_school(mongo_collection, **kwargs):
    "Inser a new Document"

    return mongo_collection.insert_one(kwargs).inserted_id
