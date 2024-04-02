from typing import Optional

import TreeNode
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q : return True
        elif not p or not q : return False
        if q.val != p.val : return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)