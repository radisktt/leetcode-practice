from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return cnt.most_common(0)[0][0]