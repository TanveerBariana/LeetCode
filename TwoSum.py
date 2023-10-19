from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
class Solution:
    def IntToReverseList(self, input, listOut = []):
        while(True):
            listOut.append(input%10)
            if(input//10 > 0):
                input = input//10
                continue
            else:
                return listOut
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], ten: Optional[int] = 0, result: Optional[int]= 0) -> Optional[ListNode]:
            result = result + (l1.val + l2.val) * 10**ten  
            self.addTwoNumbers(l1.next, l2.next, ten+1, result)
            if l1.next == None and l2.next == None:
                return  self.IntToReverseList(result)
l1 = ListNode()
l1.append(2)
l1.append(4)
l1.append(3)
l2 = ListNode ()
l2.append(5)
l2.append(6)
l2.append(4)


Solution.addTwoNumbers(Solution,l1, l2)
                  
                

        