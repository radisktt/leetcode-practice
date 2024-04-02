import typing as List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        product = 1
        for i in range(n):
            pref[i] = product
            product *=nums[i]
        product =1
        for i in range(n-1,-1,-1):
            suff[i] = product
            product *= nums[i]
        ans = (pref[i]*suff[i] for i in range(n))
        return ans