# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        x = p.val
        y = q.val

        return self.recurse(root,x,y)
 
    def recurse(self,root,x,y):
        if root.val in [x,y]:
            return root
        elif min(x,y) < root.val < max(x,y):
            return root
        elif root.val < x and root.val < y:
            return self.recurse(root.right,x,y)
        elif root.val > x and root.val > y:
            return self.recurse(root.left,x,y)


        