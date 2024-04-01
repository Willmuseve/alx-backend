#!/usr/bin/env python3


"""A function that returns a tuple based on the given parameters
"""

import math
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start index and end index
    for the given pagination parameters.
    """
    start = (page - 1) * page_size
    end = page * page_size

    return start, end


class Server:
    """database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        page of the dataset based on pagination parameters.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        # Return an empty list if the indexes are out of range
        if start >= len(dataset):
            return []

        return dataset[start:end]
