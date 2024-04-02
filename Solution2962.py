from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        x = max(nums)
        f = 0; left = 0;res = 0
        for right in range(len(nums)):
            if nums[right] == x:
                f+=1
            while f >=k:
                if nums[left] == x:
                    f-=1
            res+= left
        return res