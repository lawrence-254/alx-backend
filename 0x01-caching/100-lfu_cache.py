#!/usr/bin/python3
""" LFUCache module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
    class LFUCache that inherits from BaseCaching and is a caching system
    '''
    def __init__(self):
        '''
        init method
        '''
        super().__init__()
        self.leastRecent = []

    def put(self, key, item):
        '''
        adds to cache
        '''
        if key is not None or item is not None:
            if self.get(key) is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    del_key = self.leastRecent
                    del_len = len(del_key) - 1
                    del self.cache_data[del_key[del_len]]
                    print("DISCARD: {}".format(leastRecent.pop()))
            else:
                del self.cache_data[key]

            if key in self.leastRecent:
                del_idx = self.search_first(self.leastRecent, key)
                self.leastRecent.pop(del_idx)
                self.leastRecent.insert(0, key)
            else:
                self.leastRecent.insert(0, key)

            self.cache_data[key] = item

    def get(self, key):
        '''
        gets the cache data
        '''
        if self.cache_data.get(key):
            del_idx = self.search_first(self.leastRecent, key)
            self.leastRecent.pop(del_idx)
            self.leastRecent.insert(0, key)

        return self.cache_data.get(key)

    @staticmethod
    def search_first(mrul, key):
        for i in range(0, len(mrul)):
            if mrul[i] == key:
                return i

        return None
