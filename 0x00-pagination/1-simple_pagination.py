#!/usr/bin/env python3
'''
a function named index_range that takes two integer arguments
page and page_size
'''
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)

class Server:
    '''
    Server class to paginate a database of popular baby names.
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''
        init
        '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''
        Cached dataset
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        takes two integer arguments page with default value 1
        and page_size with default value 10.
        '''
        assert type(page) == int and type(page_size)==int
        assert page > o and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]