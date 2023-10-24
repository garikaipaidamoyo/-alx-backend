#!/usr/bin/python3
""" MRU Caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache class """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                most_recent_key = self.mru_order.pop()
                print(f"DISCARD: {most_recent_key}")
                del self.cache_data[most_recent_key]
            self.cache_data[key] = item
            self.mru_order.insert(0, key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key in self.cache_data:
            self.mru_order.remove(key)
            self.mru_order.insert(0, key)
        return self.cache_data.get(key)
