from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        arr = [0]*n
        deck.sort()
        q = deque()
        for i in range(n):
            q.append(i)
        for card in deck:
            idx = q.popleft()
            arr[idx] = card
            if q:
                arr.append(q.popleft())
        return arr
