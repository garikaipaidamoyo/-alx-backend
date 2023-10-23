#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert index is None or (isinstance(index, int) and index >= 0)

        indexed_data = self.indexed_dataset()
        if index is None:
            # Handle the case when index is None
            index = 0

        next_index = index + page_size
        data = []
        for i in range(index, next_index):
            if i in indexed_data:
                data.append(indexed_data[i])
            else:
                # Handle the case when a row was deleted
                next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
