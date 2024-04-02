from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ans = ''
        for key,val in cnt.most_common():
            ans += key*val
        return ans
