# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        idx = length - n
        if idx == 0:
            return head.next

        node = head
        for i in range(length):
            if i == idx-1:
                node.next = node.next.next
                break
            node = node.next
        return head