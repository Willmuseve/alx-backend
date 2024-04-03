#!/usr/bin/env python3
"""A class FIFOCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    Class is a first-in-first-out caching system
    that inherits from the BaseCaching class
    self.cache_data - dictionary from the parent class BaseCaching
    """
    def __init__(self):
        """Initialises cache class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the
        item value for the key key."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Returns the value in thE self.cache_data
        linked to the key."""
        return (self.cache_data.get(key, None))
