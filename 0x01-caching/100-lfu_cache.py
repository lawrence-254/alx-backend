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

