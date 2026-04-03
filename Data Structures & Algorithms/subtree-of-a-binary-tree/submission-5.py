# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.check(root, subRoot)
    
    def check(self, r, s):
        if not r:
            return False
        
        if self.checkSame(r,s):
            return True

        left = self.check(r.left,s)
        right = self.check(r.right,s)
        return left or right

    def checkSame(self, p, q):
        if not (p or q):
            return True
        if not (p and q) and (p or q) :
            return False
        
        if p.val == q.val:
            if not self.checkSame(p.left,q.left):
                return False
            return self.checkSame(p.right, q.right)
        else:
            return False
            
        
