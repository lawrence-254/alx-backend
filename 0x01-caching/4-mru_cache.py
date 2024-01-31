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
            mru_key = next(iter(self.cache_data))
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item

    def get(self, key):
        '''
        fetches data from the cache
        '''
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
