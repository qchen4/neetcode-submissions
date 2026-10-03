# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head

        while curr and curr.next: 
            #self.print_out(head)
            temp = curr
            while temp.next.next:
                temp = temp.next
            end = temp.next
            temp.next = None

            temp = curr.next 
            curr.next = end
            end.next = temp

            curr = curr.next.next
   

    # def print_out(self, head):
    #     curr = head
    #     arr = []
    #     while curr:
    #         arr.append(curr.val)
    #         curr = curr.next
    #     print(arr)
            



        