# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recurse(pre, ino):

            if len(ino) == 0:
                return None

            curr = pre[0]
            for i in range(len(ino)):
                if ino[i] == curr:
                    break
            

            left = recurse(pre[1:],ino[:i])
            right = recurse(pre[i+1:],ino[i+1:])

            return TreeNode(val=curr,left=left,right=right)

        return recurse(preorder, inorder)