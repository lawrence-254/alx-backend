#!/usr/bin/env python3
'''
lifo caching
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    dictionary from the parent class BaseCaching
    LIFO caching system with a maximum number of items.
    '''
    def __init__(self):
        '''init'''
        super().__init__()

    def put(self, key, item):
        '''
        assiggns value to a dict for a given key
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_item = list(self.cache_data.keys())[-1]
                del self.cache_data[last_item]
                print(f"DISCARD: {last_item}")
            self.cache_data[key] = item

    def get(self, key):
        '''
        returns cached data key
        '''
        if key is not None:
            return self.cache_data.get(key)
