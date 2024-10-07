#!/usr/bin/env python3

"Find all documents with a topic"


def schools_by_topic(mongo_collection, topic):
    "Find all documents that has a specific topic"

    return mongo_collection.find({"topics": topic})
