#!/usr/bin/env python3

"""
A  class LRUCache that inherits from
BaseCaching and is a caching system.
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
        self.order = OrderedDict()

    def put(self, key, item):
        """
         assign to the dictionary self.cache_data the item
         value for the key key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item (LRU)
                discarded_key, _ = self.order.popitem(last=False)
                print(f"DISCARD: {discarded_key}")
                if discarded_key in self.cache_data:
                    del self.cache_data[discarded_key]
            self.cache_data[key] = item
            self.order[key] = None

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
