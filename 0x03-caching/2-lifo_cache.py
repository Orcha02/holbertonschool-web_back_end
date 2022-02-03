#!/usr/bin/python3
""" Module for LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.all_keys = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.all_keys.pop()
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]

        self.all_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
