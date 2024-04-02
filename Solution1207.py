import typing as List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values())) == len(set(Counter(arr).keys()))
