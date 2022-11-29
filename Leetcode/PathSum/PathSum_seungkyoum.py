from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum, curr):
            if root:
                curr += root.val
                if curr == targetSum and root.left == None and root.right == None:
                    return True
                return dfs(root.left, targetSum, curr) or dfs(root.right, targetSum, curr)
        return dfs(root, targetSum, 0)