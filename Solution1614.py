class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append('(')
            elif s[i] == ")":
                stack.pop()
            res = max(res,len(stack))
        return res