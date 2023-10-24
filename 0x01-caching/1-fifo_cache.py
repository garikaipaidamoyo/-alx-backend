#!/usr/bin/python3
""" 1-fifo_cache """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Class FIFOCache that inherits from BaseCaching and is a caching system.
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded = next(iter(self.cache_data))
                print("DISCARD: {}".format(discarded))
                del self.cache_data[discarded]
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
