from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dict = {}
        res = 0;left = 0
        for i in range(len(nums)):
            x = nums[i]
            dict[x] = dict.get(x,0)+1
            while dict[x] > k and left<=i:
                dict[nums[left]] -=1
                left+=1
            res = i-left+1
        return res