# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        global opt
        global max_depth
        
        opt = []
        max_depth = -1

        def recurse(root, depth):
            global opt
            global max_depth

            if root is None:
                return

            if depth > max_depth:
                opt.append(root.val)
                max_depth += 1

            recurse(root.right, depth+1)
            recurse(root.left, depth+1)

        recurse(root,0)

        return opt