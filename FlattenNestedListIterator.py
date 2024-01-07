class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList() -> list:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger] = None):
        self.nestedList = nestedList

    def next(self) -> int:
        # if self.nestedList[0].isInteger():
        #     print(self.nestedList[0].getInteger())
        #     return self.nestedList[0].getInteger()
        # else:
        #     self.nestedList = self.nestedList[0].getList()
        #     print(self.nestedList)
        #     return self.next()
        return self.nestedList[0].getList()

                
        
    def hasNext(self) -> bool: #Returns true if there are still some integers in the nested list and false otherwise
        # if self.nestedList[0].isInteger() or self.nestedList[0].getList() != None:
        #     return True
        # return False
        print(self)
        return False

nestedList = [[1,1],2,[1,1]] 
i, v = NestedIterator(nestedList), []

while i.hasNext(): v.append(i.next())