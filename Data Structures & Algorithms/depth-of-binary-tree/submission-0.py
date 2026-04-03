# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.checkDepth(root,0)
    def checkDepth(self, root, d):
        if not root:
            return d
        
        l = self.checkDepth(root.left, d+1) if root.left else d+1
        r = self.checkDepth(root.right, d+1) if root.right else d+1

        return max(l,r)