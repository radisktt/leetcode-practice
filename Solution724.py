class Solution:
    def pivotIndex(self, nums) -> int:
        ans = -1
        pref = 0
        total = sum(nums)
        for i in range(len(nums)):
            if total - pref -nums[i] == pref:
                ans = i
            pref +=nums[i]
        return ans
