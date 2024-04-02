from typing import Optional
import ListNode

class Solution:
    def rever(self,head):
        pre, nex = None,None
        while head:
            nex = head.next
            head.next = pre
            pre = head
            head = nex
        return pre
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ans = head
        fast,slow = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = self.rever(slow.next)
        nex1 = None;nex2 = None
        while fast.next:
            nex1 = ans.next
            nex2 = fast.next
            ans.next = fast
            fast.next = nex1

