from typing import List
from collections import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        y = max(cnt.values())
        t = len(list(filter(lambda x : cnt[x]==y,cnt)))
        res = (n+1)*y-(n+1-t)
        return res if res > len(tasks) else len(tasks)
