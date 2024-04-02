from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 0
        right = -1
        points.sort(key=lambda x:x[0])
        for x,y in points:
            if x <= right:
                1
            else:
                res+=1
                right = y
        return res
