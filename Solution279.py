from functools import cache


class Solution:
    def numSquares(self, n: int) :
        @cache
        def dfs(n):
            x = int(n**0.5)
            return 1 if x**2 == n else 1+ min(dfs(n-i**2) for i in range(1,x+1))
        return dfs(n)