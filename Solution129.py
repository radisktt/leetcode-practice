from typing import Optional

import TreeNode
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0
        def dfs(node,val):
            nonlocal sum
            if not node:
                return
            cur = val*10 + node.val
            if not node.left and not node.right :
                sum += val
                return
            if node.left:
                dfs(node.left,cur)
            if node.right:
                dfs(node.right,cur)
        dfs(root,sum)
        return sum