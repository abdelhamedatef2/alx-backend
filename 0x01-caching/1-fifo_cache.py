#!/usr/bin/env python3
""" module represent first in first out """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ class represent how cash work
        with first in first out concept
    """

    def __init__(self):
        """ init magic method """
        super().__init__()

    def put(self, key, item):
        """ method to add new item to dict of cache """
        if key is None or item is None:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            first = next(iter(self.cache_data))
            print(f'DISCARD: {first}')
            del self.cache_data[first]
        self.cache_data[key] = item

    def get(self, key):
        """ method to get item from cache
            params:
                key: key of new item
        """
        return self.cache_data.get(key, None)
