from typing import List
from operator import itemgetter
import collections
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        book = [0]*n
        cnt = [0]*n
        for start, end in sorted(meetings,key=itemgetter(0)):
            freeBooked = False
            nextBooked = [book[0],0]
            for i in range(n):
                if book[i] <= start:
                    book[i] = end
                    cnt[i]+=1
                    freeBooked = True
                    break
                elif book[i] < nextBooked[0]:
                    nextBooked[0] = book[i]
                    nextBooked[1] = i
            if freeBooked == False:
                book[nextBooked[1]] = nextBooked[0] + (end-start)
                cnt[nextBooked[1]] +=1
        return cnt.index(max(cnt))