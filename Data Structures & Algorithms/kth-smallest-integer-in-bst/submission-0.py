# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        global ar
        ar = []

        def recurse(node, k):
            global ar
            if node is None:
                return

            if len(ar) == k:
                return
            else:
                recurse(node.left,k)
                if len(ar) == k:
                    return
                ar.append(node.val)
                recurse(node.right,k)

        recurse(root,k)

        return ar[-1]