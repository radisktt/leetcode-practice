import math
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n = min(len(word1),len(word2))
        for i in range (n) :
            ans +=word1[i]
            ans +=word2[i]
        if len(word1) > n:
            for i in range (n,len(word1)):
                ans +=word1[i]
        if(len(word2) > n):
            for i in range (n,len(word2)):
                ans +=word2[i]
        return ans