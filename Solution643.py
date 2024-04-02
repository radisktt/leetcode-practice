from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = sum(nums[:k])
        cursum = maxsum
        for i in range(k,len(nums)):
            cursum = cursum + nums[i] - nums[i-k]
            maxsum = max(maxsum,cursum)
        return maxsum/k