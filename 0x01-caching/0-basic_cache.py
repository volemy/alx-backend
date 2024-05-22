#!/usr/bin/python3
"""BasicCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines:
    """
    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None and item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """
        (Get and item in cache)Must return the value in self.cache_data
        linked to key.If key is None or if the key doesn’t exist
        in self.cache_data, return None.
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
