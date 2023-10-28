# Definition for singly-linked list.
#add types
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
     
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = [ListNode()]
        sum = ListNode()
        if l1.next is not None or l2.next is not None:
            print(l1.val)
            print(l2.val)
            print(l1.next)
            print(l2.next)      
            sum.val = l1.val + l2.val
            sum.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            print ("wahoo")
            return sum