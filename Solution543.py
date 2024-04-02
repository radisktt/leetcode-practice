from typing import Optional
import TreeNode
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) :
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root: return 0
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            ans = max(ans,left+right)
            #return max(left,right)
        return ans
