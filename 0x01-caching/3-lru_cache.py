#!/usr/bin/env python3
'''
lru module
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    a class LRUCache that inherits from BaseCaching and is a caching system
    '''
    def __init__(self):
        super().__init__()
        self.leastrecentlyused = []

    def put(self, key, item):
        '''
        adds item to cache
        '''
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            recent = self.leastrecentlyused.pop(0)
            del self.cache_data[recent]
            print(f"DISCARD: {recent}")

        self.cache_data[key] = item
        self.leastrecentlyused.append(key)

    def get(self, key):
        '''
        fetch cache items
        '''
        if key is None or key not in self.cache_data:
            return None

        self.leastrecentlyused.remove(key)
        self.leastrecentlyused.append(key)

        return self.cache_data[key]
