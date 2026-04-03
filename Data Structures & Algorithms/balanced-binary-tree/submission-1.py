# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check(root)[0]

    def check(self,node):
        if node is None:
            return (True,0)

        l = self.check(node.left) if node.left else (True, 0)
        r = self.check(node.right) if node.right else (True, 0)
        
        if l[0] and r[0]:
            flag = True if abs(l[1]-r[1]) <= 1 else False
        else:
            flag = False

        return (flag, max(l[1],r[1])+1)