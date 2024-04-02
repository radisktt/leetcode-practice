from typing import Optional

import ListNode
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head ,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = self.rever(slow.next)
        while slow:
            if head.val != slow.val :
                return False
            head = head.next
            slow = slow.next
        return True
    def rever(self,head):
        pre,next = None,None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
