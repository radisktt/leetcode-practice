from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0;right = len(tokens) -1
        ans = 0;cnt = 0
        while left <= right:
            if power >= tokens[left]:
                power-=tokens[left]
                left+=1
                cnt+=1;ans = max(ans,cnt)
            elif cnt > 0:
                power += tokens[right]
                right-=1
            else: break
        return ans