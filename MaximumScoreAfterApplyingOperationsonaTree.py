class Solution:
    def maximumScoreAfterOperations(self, edges: list[list[int]], values: list[int]) -> int:

        subset = [lst for lst in edges if lst[0]== i]
        return 0
    


# pick the parent node to add in instead of the children if the parents value is greater than the sum of the children 
# else pick all of the children. 
# if they are equal do both.  

