"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head

        if not head:
            return None

        nodes = {}
        n_nodes = []
        i = 0
        while node:
            nodes[node] = i
            i+=1            
            n_node = Node(x=node.val)
            n_nodes.append(n_node)
            node= node.next

        node = head
        for i,n in enumerate(n_nodes):
            if i < len(n_nodes)-1:
                n.next = n_nodes[i+1]
            
            n.random = n_nodes[nodes[node.random]] if node.random else None

            node = node.next
            

        return n_nodes[0]

        
