#!/usr/bin/env python3
"""A class basuccache that inherits from BaseCaching class
and is a cashing system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class is a caching system that inherits
    from BaseCaching class. Used self.cache_data dictionnary from
    the parent class BaseCaching
    """
    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the item
        value for the key key."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value in the dictionary linked to the key."""
        return (self.cache_data.get(key, None))
