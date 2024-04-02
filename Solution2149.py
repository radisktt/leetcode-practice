from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [];neg = []
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        if not pos or not neg: return nums
        ans = []
        i = 0
        while i < n/2 :
            ans.append(pos[i])
            ans.append(neg[i])
            i+=1
        return ans
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 0;j =1
        n = len(nums)
        ans = [0]*n
        for k in range(n):
            if nums[k] > 0:
                ans[i] = nums[k]
                i+=2
            else:
                ans[j] = nums[k]
                j+=2
        return ans
