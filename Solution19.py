from typing import Optional

import ListNode
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast,slow = head,head
        for i in range(n-1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow =slow.next
        slow.next = slow.next.next
        return head