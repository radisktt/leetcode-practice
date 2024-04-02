from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        cur = 0
        for i in range(1,n+1):
            cur ^= i
        return cur