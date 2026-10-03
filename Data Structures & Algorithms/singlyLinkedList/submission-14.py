class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def get(self, index: int) -> int:
        print(self.getValues())
        cur = self.head
        for i in range (index +1):
            if i == index:
                if cur:
                    return cur.val
            if cur and cur.next:
                cur = cur.next 
            else: return -1
        return -1

    def insertHead(self, val: int) -> None:
        temp = self.head
        self.head = ListNode(val)
        self.head.next = temp
        self.length +=1
        

    def insertTail(self, val: int) -> None:
        cur = self.head
        
        if cur:
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)
        else:
            self.head = ListNode(val)
        self.length +=1
        

    def remove(self, index: int) -> bool:
        print("remove", index, self.getValues())
        curr_index = 0
        curr = self.head

        if index == 0:
            if self.head:
                self.head = self.head.next
                return True
            else:
                return False

        while curr:
            if curr_index + 1 == index:
                if curr.next:
                    curr.next = curr.next.next
                    return True
                else:
                    return False
            curr = curr.next
            curr_index +=1
        self.length -= 1
      
        return False

        

    def getValues(self) -> List[int]:
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr

class ListNode:
        
    def __init__(self, val):
        self.val = val
        self.next = None
        
