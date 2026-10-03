# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointers = set()
        curr = head
        while curr is not None:
            if curr in pointers:
                return True
            pointers.add(curr)
            curr = curr.next
        return False







        