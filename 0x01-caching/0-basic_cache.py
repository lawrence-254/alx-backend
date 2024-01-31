#!/usr/bin/env python3
'''
basic caching
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    dictionary from the parent class BaseCaching
    This caching system doesn’t have limit
    '''

    def put(self, key, item):
        '''
        assiggns value to a dict for a given key
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        returns cached data key
        '''
        if key is not None:
            return self.cache_data.get(key)
