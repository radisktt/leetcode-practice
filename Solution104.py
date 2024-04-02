from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], ans=0) -> int:
        if root is None:
            return ans
        return max(self.maxDepth(root.left, ans + 1), self.maxDepth(root.right, ans + 1))
