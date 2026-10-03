# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or (not head.next):
            return None
        cnt = 1 
        tail = head
        while (tail.next):
            tail = tail.next
            cnt += 1
        index = cnt - n
        if index == 0:
            return head.next
        temp = head
        for i in range(index -1):
            temp = temp.next
        temp.next = temp.next.next
        return head

            






