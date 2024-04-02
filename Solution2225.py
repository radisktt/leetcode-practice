import typing as List
from collections import Counter


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [set(),set()]
        lose = set()
        for i in range(len(matches)):
            win,los = matches[i]
            if win not in lose:
                ans[0].add(win)
            if los not in ans[1] and los not in lose:
                ans[1].add(los)
                lose.add(los)
            elif los in ans[1]:
                ans[1].remove(los)
            if los in ans[0]:
                ans[0].remove(los)
        return [sorted(ans[0]),sorted(ans[1])]
