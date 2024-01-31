#!/usr/bin/env python3
'''
fifo caching
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    dictionary from the parent class BaseCaching
    FIFO caching system with a maximum number of items.
    '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''
        assiggns value to a dict for a given key
        '''
        if key is not None and item is not None:
            #if (self.get(key)) is None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                firt_item = self.cache_data.popitem(last=False)
                print(f"DISCARD: {firt_item}\n")

    def get(self, key):
        '''
        returns cached data key
        '''
        if key is not None:
            return self.cache_data.get(key)
