# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.recurse(root, [])

    def recurse(self, node, ar):
        if not node:
            return 0
        flag = True
        ar = ar.copy()

        for n in ar:
            if node.val < n:
                flag = False
        ar.append(node.val)

        l = self.recurse(node.left, ar)
        r = self.recurse(node.right, ar)

        if flag:
            return l+r+1
        else:
            return l+r 