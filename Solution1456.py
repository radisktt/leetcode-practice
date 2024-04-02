class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'ueoai'
        x = sum(1 for i in s[:k] if i in vowels)
        ans = x
        for i in range(k,len(s)):
            if s[i] in vowels : x+=1
            if s[i-k] in vowels : x-=1
            ans = max(ans,x)
        return ans