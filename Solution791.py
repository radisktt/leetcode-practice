from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict = Counter(s)
        ans = ''
        for c in order:
            if dict[c]:
                ans+=c*dict[c]
                del dict[c]
                s = s.replace(c,'')
        return ans+s
