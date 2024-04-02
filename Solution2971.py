from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        cur = nums[0]+nums[1]
        ans = -1
        for i in range(2,len(nums)):
            if cur > nums[i]:
                ans = cur +nums[i]
            cur+= nums[i]
        return ans