class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            i = t.find(c) # tim char, neu k co = false, neu co t = substr i+1:end
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True