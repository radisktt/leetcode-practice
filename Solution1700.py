from typing import List
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        res = len(students)
        for i in range(len(sandwiches)):
            if cnt[sandwiches[i]] == 0:
                break
            cnt[sandwiches[i]] -=1
            res -=1
        return res