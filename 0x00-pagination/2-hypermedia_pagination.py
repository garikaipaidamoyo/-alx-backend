#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
from typing import List


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_pages = len(dataset) // page_size
        if len(dataset) % page_size != 0:
            total_pages += 1

        start = (page - 1) * page_size
        end = start + page_size
        data = dataset[start:end]

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
