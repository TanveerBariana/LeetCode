# Definition for singly-linked list.
from typing import Optional 
class ListNode(object):
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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev    
    
class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode] , l2: Optional[ListNode]):
        reversedL1 = l1.reverse()
        reversedL2 = l2.reverse()
        result = int(''.join(map(str, reversedL1))) + int(''.join(map(str, reversedL2))) 
        print(result)       
        #return IntToReverseList(result)
        return result
    # def reverse(self, listOut: ListNode):
    #         prev = None
    #         current = listOut.val
    #         while current:
    #             next_node = current.next
    #             current.next = prev
    #             prev = current
    #             current = next_node
    #         listOut.val = prev
    #         return listOut
    def IntToReverseList(input, listOut = []):
            while(True):
                listOut.append(input%10)
                if(input//10 > 0):
                    input = input//10
                    continue
                else:
                    return listOut
l1 = [2,4,3]
l2 = [5,6,4]

Solution.addTwoNumbers(l1, l2)