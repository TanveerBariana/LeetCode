class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        compet = [0] * n
        for i in edges:
            compet[i[1]] += 1
        min_indix = [i for i, value in enumerate(compet) if value == min(compet)]
        if len(min_indix) == 1:
            return(compet.index(min(compet)))
        else:
            return -1

print(Solution().findChampion(3,[[0,1],[1,2]]))
print(Solution().findChampion(4,[[0,2],[1,3],[1,2]]))

# print(Solution().findChampion( [[0,0,1],[1,0,1],[0,0,0]]))
# print(Solution().findChampion( [[0,0],[1,0]]))