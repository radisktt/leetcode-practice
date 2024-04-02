class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict = {}
        for c in s:
            if c not in dict:
                dict[c]=1
            else: dict[c]+=1
        for c in t:
            if c in dict:
                if dict[c]==1: dict.pop(c)
                else: dict[c]-=1
        return sum(dict.values())