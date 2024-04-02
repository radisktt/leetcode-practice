from typing import List


class Solution1:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.slidew(nums,goal) - self.slidew(nums,goal-1)
        # total sub arr with sum <= goal - subarr sum <= goal-1
    def slidew(self,nums,goal):
        res, cur, left = 0, 0, 0
        for right in range(len(nums)):
            cur += nums[right]
            while left <= right and cur > goal:
                cur -= nums[left]
                left += 1
            res += right - left + 1
        return res



