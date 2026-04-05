# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        node = head
        prev = None
        for i in range(length):
            if i == length//2 + length%2 - 1:
                next_node = node.next
                node.next = None
                node = next_node
                continue
            if i >= length//2 + length%2:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            else:
                node = node.next

        while prev:
            next_node = head.next
            head.next = prev

            prev = prev.next
            head.next.next = next_node
            head = next_node

            
