from collections import Counter
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        d = Counter(s)
        cnt = d[1]
        zero = d[0]
        ans = '1';cnt-=1
        for _ in range(zero):ans = '0'+ans
        for _ in range(cnt):ans = '1'+ans
        return ans