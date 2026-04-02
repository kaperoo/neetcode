# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root: self.recurse(root)
        return root
    def recurse(self, root):
        if root.left:
            self.recurse(root.left)
        if root.right:
            self.recurse(root.right)
        root.left, root.right = root.right, root.left

