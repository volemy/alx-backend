#!/usr/bin/env python3
"""
Task 2 For Hypermedia pagination
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    index_range that takes two integer
    Args:
        int(page)
        int(page_size)
    Returns:
        tuple(start index, end index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the page of data.

        Args:
            self: The CSV file name.
            page: The page number.
            page_size: The number of items per page.
        Returns:
            A list of lists.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index > len(data):
            return []
        return data[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get the page of data.

        Args:
            self: The CSV file name.
            page: The page number.
            page_size: The number of items per page.
        Returns:
            A dictionary.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        page_size = len(self.get_page(page, page_size))
        data = self.get_page(page, page_size)
        total_pages = math.floor(len(self.dataset()) / page_size)
        next_page = page + 1 if page + 1 < total_pages else None
        prev_page = page - 1 if page > 1 else None

        metadata = {
                "page_size": page_size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
            }

        return metadata
