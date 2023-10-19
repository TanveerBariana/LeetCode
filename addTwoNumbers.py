# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        reversedL1 = reverse(l1)
        reversedL2 = reverse(l2)
        result = int(''.join(map(str, reversedL1))) + int(''.join(map(str, reversedL2))) 
        print(result)       
        return IntToReverseList(result)
def reverse(self, listOut: ListNode):
        prev = None
        current = listOut.val
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        listOut.val = prev
        return listOut
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