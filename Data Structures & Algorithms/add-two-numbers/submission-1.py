# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (not l1) and l2:
            return l2
        elif (not l2) and l1:
            return l1
        elif not (l1 or l2):
            return None
        
        s1,s2 = 0,0
        i = 1
        while l1 or l2:
            if l1:
                s1 += l1.val * i
                l1 = l1.next
            if l2:
                s2 += l2.val * i
                l2 = l2.next
            
            i*=10

        s3 = s1+s2
        dummy = ListNode()

        node = dummy
        if s3 == 0:
            return ListNode(val=0)
        while s3 > 0:
            d= s3%10
            s3 = s3//10

            node.next = ListNode(val=d)
            node = node.next

        return dummy.next
