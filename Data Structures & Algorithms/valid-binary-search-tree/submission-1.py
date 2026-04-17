# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        _,opt = self.recurse(root)

        return opt

    def recurse(self,node):

        left = True
        right = True
        l,r = None, None
        if node.left:
            l,left = self.recurse(node.left)
        if node.right:
            r,right = self.recurse(node.right)

        if l and r:
            if (left and right) and l[1]<node.val<r[0]:
                return ([l[0],r[1]], True)
            return ([-1,-1], False)
        elif l:
            if left and l[1]<node.val:
                return ([l[0],node.val], True)
            return ([-1,-1], False)
        elif r:
            if right and node.val<r[0]:
                return ([node.val,r[1]], True)
            return ([-1,-1], False)
        else:
            return ([node.val,node.val], True)
            


