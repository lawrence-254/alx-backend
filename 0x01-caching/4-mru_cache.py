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
        if key or item is not None:
            valuecache = self.get(key)
            if valuecache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = self.leastrecent
                    lendel = len(keydel) - 1
                    del self.cache_data[keydel[lendel]]
                    print("DISCARD: {}".format(self.leastrecent.pop()))
                else:
                    del self.cache_data[key]
                    
                if key in self.leastrecent:
                    self.leastrecent.remove(key)
                    self.leastrecent.append(key)
                else:
                    self.leastrecent.append(key)
                    self.cache_data[key] = item
                        
    def get(self, key):
        '''
        fetches data from the cache
        '''
        if key is None or key not in self.cache_data:
            return

        self.cache_data[key] = self.cache_data.pop(key)
        return self.cache_data.pop(key)
