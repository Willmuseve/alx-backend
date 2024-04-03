#!/usr/bin/env python3

"""
A class LRUCache that inherits from
BaseCaching and is a caching system
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    the class itself uses self.cache_data - dictionary
    from the parent class BaseCaching.
    """

    def __init__(self):
        """
        Initialize a BasicCache object.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
         assign to the dictionary self.cache_data the item
         value for the key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                leastRecently_key = self.order.pop(0)
                del self.cache_data[leastRecently_key]
                print("DISCARD:", leastRecently_key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
