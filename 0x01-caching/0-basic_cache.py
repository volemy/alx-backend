#!/usr/bin/python3
"""Task 0 For BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache;
    """
    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()

    def put(self, key, item):
        """Adding item in cache."""
        if key is None and item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
       """return the value in self.cache_data linked to key

        Args:
                key (_type_): _description_
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
