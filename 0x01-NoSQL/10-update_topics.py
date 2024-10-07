#!/usr/bin/env python3

"Update Documents Function"


def update_topics(mongo_collection, name, topics):
    "Update all Document's topics based on name"

    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
