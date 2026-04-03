# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p,q)
    
    def check(self, p, q):
        if not (p or q):
            return True
        if not (p and q) and (p or q) :
            return False
        
        if p.val == q.val:
            if not self.check(p.left,q.left):
                return False
            return self.check(p.right, q.right)
        else:
            return False
        