from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        ans = []
        for l,r in intervals:
            if r < new[0]:
                ans.append(intervals)
            elif l > new[1]:
                ans.append(new)
                new = [l,r]
            elif l < new[1] or r > new[0]:
                new[0] = min(l,new[0])
                new[1] = max(r,new[1])
        ans.append(new)
        return ans
