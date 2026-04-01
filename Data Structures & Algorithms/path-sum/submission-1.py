# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.recurse(root, targetSum)

    def recurse(self, node, target):
        new_target = target - node.val

        if node.left and node.right:
            if self.recurse(node.left, new_target):
                return True
            return self.recurse(node.right, new_target)
        elif node.left:
            return self.recurse(node.left, new_target)
        elif node.right:
            return self.recurse(node.right, new_target)
        else:
            return True if new_target == 0 else False
        
