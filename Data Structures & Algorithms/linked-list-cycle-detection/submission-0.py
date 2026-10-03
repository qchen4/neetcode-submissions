# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointers = {}
        curr = head
        while curr is not None:
            if curr not in pointers:
                pointers[curr] = 1
                print(curr.val)
                curr = curr.next
            else:
                return True
        return False







        