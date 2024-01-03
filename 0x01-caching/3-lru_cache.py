#!/usr/bin/env python3
""" module represent first in first out """
from base_caching import BaseCaching
import time


class LRUCache(BaseCaching):
    """ class represent how cash work
        with least recently used concept
    """

    def __init__(self):
        """ init magic method """
        self.order = {}
        super().__init__()

    def put(self, key, item):
        """ method to add new item to dict of cache """
        if key is None or item is None:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            min_val = min(self.order.values())
            li_keys = [k for k, v in self.order.items() if v == min_val]
            print(f'DISCARD: {li_keys[0]}')
            del self.cache_data[li_keys[0]]
            del self.order[li_keys[0]]
        self.cache_data[key] = item
        self.order[key] = time.time()

    def get(self, key):
        """ method to get item from cache
            params:
                key: key of new item
        """
        if key in self.order:
            self.order[key] = time.time()
        return self.cache_data.get(key, None)
