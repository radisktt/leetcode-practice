class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        arr1 = []
        arr2 = []
        def dfs(root:TreeNode,arr:list)->list:
            if(root.left is None and root.right is None):
                arr.append(root.val)
            if(root.left is not None):
                dfs(root.left,arr)
            if(root.right is not None):
                dfs(root.right,arr)
        arr1 = dfs(root1,arr1)
        arr2 = dfs(root2,arr2)

