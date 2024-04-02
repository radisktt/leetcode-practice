from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        x = cnt.most_common()[0][1]
        ans = 0
        for i in cnt.most_common():
            if cnt[i] == x:
                cnt+=x
            elif cnt[i] < x:
                break
        return ans