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
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''
        fetches data from the cache
        '''
        if key is None or key not in self.cache_data:
            return

        self.cache_data[key] = self.cache_data.pop(key)
        return self.cache_data.pop(key)
