from typing import Optional
import ListNode
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, node , total = None,head,0
        dict = {0:prev}
        while node:
            total+= node.val
            if total in dict:
                pre_remove = dict[total]
                if not pre_remove:
                    head = head.next
                else:
                    pre_remove = node.next
                return self.removeZeroSumSublists(head) 
            prev = node
            node = node.next
            dict[total] = prev
        return head