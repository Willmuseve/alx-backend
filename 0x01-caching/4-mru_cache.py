#!/usr/bin/env python3

"""
Class MRUCache that inherits from
BaseCaching and is a caching system.
"""


from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    Class itself that uses self.cache_data - dictionary from
    the parent class BaseCaching
    """

    def __init__(self):
        """
         calls the parent init
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
                mostRecently_key = self.order.pop()
                del self.cache_data[mostRecently_key]
                print("DISCARD:", mostRecently_key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is not None:
            if key in self.cache_data:
                self.order.append(key)
                return self.cache_data[key]
        return None
