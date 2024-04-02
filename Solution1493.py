from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left,right,cnt = 0,0,0
        ans = -1
        for right in range(n):
            if nums[right] == 0:
                cnt+=1
            while cnt > 1:
                if nums[left] ==0:
                    cnt -=1
                left+=1
            ans = max(ans,right - left+1 -cnt)
        return ans - 1 if ans == n else ans