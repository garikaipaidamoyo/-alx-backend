#!/usr/bin/python3
""" LFU Caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache class """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.usage_frequency = {}  # Dictionary to store frequency of each item
        self.frequency_lists = {}  # Dictionary to store items by frequency

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.usage_frequency.values())
                if min_frequency in self.frequency_lists:
                    lru_key = self.frequency_lists[min_frequency].pop(0)
                    del self.cache_data[lru_key]
                    if len(self.frequency_lists[min_frequency]) == 0:
                        del self.frequency_lists[min_frequency]
                del self.usage_frequency[lru_key]

            self.cache_data[key] = item
            if key in self.usage_frequency:
                self.usage_frequency[key] += 1
            else:
                self.usage_frequency[key] = 1
            frequency = self.usage_frequency[key]
            if frequency not in self.frequency_lists:
                self.frequency_lists[frequency] = [key]
            else:
                self.frequency_lists[frequency].append(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            # Update frequency_lists
            old_frequency = self.usage_frequency[key] - 1
            self.frequency_lists[old_frequency].remove(key)
            if not self.frequency_lists[old_frequency]:
                del self.frequency_lists[old_frequency]
            if self.usage_frequency[key] not in self.frequency_lists:
                self.frequency_lists[self.usage_frequency[key]] = [key]
            else:
                self.frequency_lists[self.usage_frequency[key]].append(key)
        return self.cache_data.get(key)
