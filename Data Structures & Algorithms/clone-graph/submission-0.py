"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        elif node.neighbors is None:
            return Node(val=node.val)

        self.seen = dict()

        return self.recurse(node)

    def recurse(self,node):
        new_node = Node(val=node.val)
        self.seen[node] = new_node

        for n in node.neighbors:
            if n in self.seen:
                new_node.neighbors.append(self.seen[n])
            else:
                new_node.neighbors.append(self.recurse(n))

        return new_node
