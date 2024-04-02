from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0]*(len(nums)+1)
        for i in nums:
            if arr[i] == 0 :
                arr[i]=1
            else: return i
        return -1