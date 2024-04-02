class Solution:

    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        l,r=0,n-1
        m ='ueoaiUEOAI'
        while l < r:
            if s[l] in m and s[r] in m:
                s[l],s[r] = s[r],s[l]
                l+=1;r-=1
            elif s[l] not in m:
                l+=1
            elif s[r] not in m:
                r-=1
        return ''.join(s)