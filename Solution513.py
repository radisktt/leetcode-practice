from typing import Optional
import TreeNode

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = []
        ans = 0
        queue.append(root)
        while queue:
            t = len(queue)
            for i in range(t):
                node = queue.pop(0)
                if i == 0 :
                    ans = node.val
                if node.left : queue.append(node.left)
                if node.right : queue.append(node.right)
        return ans