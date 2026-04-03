# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        opt = self.checkDia(root)
        return max(opt[0]-1 , opt[1])
    def checkDia(self, node):
        if node is None:
            return (0,0)

        l = self.checkDia(node.left) if node.left else (0,0) 
        r = self.checkDia(node.right) if node.right else (0,0)

        d = max(l[0],r[0])+1
        dia = l[0]+r[0]

        dia = max(dia,l[1],r[1])
        print(d, dia)
        return (d, dia)



        