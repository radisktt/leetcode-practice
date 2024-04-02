from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0; left = 0;cur = 1
        for i in range(len(nums)):
            cur *=nums[i]
            if cur < k:
                res+=i-left
            else:
                while cur >= k:
                    cur /=nums[left]
                    left+=1
        return res
