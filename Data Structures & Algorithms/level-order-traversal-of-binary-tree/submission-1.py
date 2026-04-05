# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.recurse(root)
    def recurse(self, node):
        if node is None:
            return []

        opts = [[node.val]]
        left = self.recurse(node.left)
        right = self.recurse(node.right)

        l = len(left)
        r = len(right)

        for i in range(min(l,r)):
            opts.append(left[i]+right[i])
        
        if l<r:
            opts.extend(right[l:])
        elif r<l:
            opts.extend(left[r:])

        return opts
            
           