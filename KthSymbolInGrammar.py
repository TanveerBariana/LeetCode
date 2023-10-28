class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
      evenList = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
      oddList =  [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
      j = k-1 
      if n == 1:
         return 0
      elif (j//16)%2 == 1:
        return oddList[j%16]
      elif (j//16)%2 == 0:
         return evenList[j%16]