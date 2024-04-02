class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        def check(s):
            if len(s) == 1: return True
            return s == s[::-1]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                if check(s[i:j]): ans+=1
        return ans