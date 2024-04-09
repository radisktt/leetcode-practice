from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(0,k+1):
            ans += tickets[i] if tickets[i] < tickets[k] else tickets[k]
        for i in range(k+1,len(tickets)):
            ans += tickets[i] if tickets[i] < tickets[k] - 1 else tickets[k]-1
        return ans
