# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        reverse_head = head
        while (reverse_head.next != None):
            reverse_head = reverse_head.next

        while(head.next != None):
            temp = head
            while (temp.next.next != None):
                temp = temp.next
            temp_reverse = temp.next
            temp_reverse.next = temp
            temp.next = None



        return reverse_head
