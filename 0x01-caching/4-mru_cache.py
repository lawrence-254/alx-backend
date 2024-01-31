#!/usr/bin/env python3
""" MRUCache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    class MRUCache that inherits from BaseCaching and is a caching system
    '''
    def __init__(self):
        '''
        init
        '''
        super().__init__()

    def put(self, key, item):
        '''
        adds to cache
        '''
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recently_used = list(self.cache_data.keys())[-1]
            del self.cache_data[most_recently_used]
            print("DISCARD: {most_recently_used}")

        self.cache_data[key] = item

    def get(self, key):
        '''
        fetches data from the cache
        '''
        if key is None or key not in self.cache_data:
            return

        self.cache_data[key] = self.cache_data.pop(key)
        return self.cache_data.pop(key)
