from typing import Optional

import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) :
        fast , slow = head,head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        return False
