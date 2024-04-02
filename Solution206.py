from typing import *
import ListNode
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre,nex  = head, ListNode(None),ListNode(None)
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre