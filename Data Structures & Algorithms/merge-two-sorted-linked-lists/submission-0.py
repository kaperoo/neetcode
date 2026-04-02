# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        i = dummy
        while list1 or list2:
            if (list1.val if list1 else 101) <= (list2.val if list2 else 101):
                i.next = list1
                list1 = list1.next
            else:
                i.next = list2
                list2 = list2.next

            i = i.next

        return dummy.next