from typing import List
from collections import Counter

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        s = ''
        ans = [0]  # Use a list to store ans so that it can be modified in the recursive function

        def backtrack(arr, s, i):
            nonlocal ans
            if i == len(arr):
                return
            k = len(arr[i])
            for char in arr[i]:
                if char in s:
                    return
            cnt = Counter(arr[i])
            #print(cnt.most_common()[0][1])
            if cnt.most_common()[0][1] > 1: return
            s += arr[i]
            ans[0] = max(ans[0], len(s))
            print(s)
            backtrack(arr, s, i + 1)  # Include the current string
            s = s[:-k]  # Remove the last added string
            backtrack(arr, s, i + 1)  # Exclude the current string

        backtrack(arr, s, 0)
        return ans[0]