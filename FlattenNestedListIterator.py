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

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
    
    def next(self) -> int:
        if self.hasNext():
            if self.nestedList.isIntiger():
                return self.nestedList.getInteger()
            elif self.nestedList.getList != None:
                return self.next(self.nestedList.getList)
        return None
                
        
    def hasNext(self) -> bool: #Returns true if there are still some integers in the nested list and false otherwise
        if self.nestedList.isIntiger() or self.nestedList.getList != None:
            return True
        return False