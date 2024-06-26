from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict = {0,-1}
        s = 0;ans = 0
        for i in range(len(nums)):
            s += 1 if nums[i] == 1 else -1
            if s in dict:
                ans = max(ans,i - dict[s])
            else: dict[s] = i
        return ans


