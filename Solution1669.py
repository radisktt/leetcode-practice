import ListNode
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tmpNode = None;head = list1
        i=1
        while list1:
           if i == a:
               tmpNode = list1
           if i == b+1:
               tmpNode.next = list2
               while list2.next:
                   list2 = list2.next
               list2.next = list1.next
               break
           list1 = list1.next
           i+=1
        return head

