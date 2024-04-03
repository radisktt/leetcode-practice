#word search
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board); n = len(board[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(s,u,v):
            idx = len(s)
            if idx == len(word):
                return True
            if u < 0 or v < 0 or u >=m or v >=n or vis[u][v] or board[u][v] != word[idx]:
                return False
            if board[u][v] == word[idx]:
                s+=word[idx]
            vis[u][v] = True
            check = dfs(s,u+1,v) or dfs(s,u-1,v) or dfs(s,u,v+1) or dfs(s,u,v-1)
            vis[u][v] = False
            return check
        for i in range(m):
            for j in range(n):
                if dfs("", i,j):
                    return True
        return False