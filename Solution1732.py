from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0;ans = 0
        for i in gain:
            cur += i
            ans = max(ans,cur)
        return ans