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
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = list(self.cache_data.keys())[-1]
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

            self.cache_data[key] = item
    def get(self, key):
        '''
        fetches data from the cache
        '''
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end to represent it's the most recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
