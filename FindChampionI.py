class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        winner = 0
        flagWin = False
        for i in range(len(grid)):
            winner = 0
            for j in range(len(grid)):
                if not(i == j):
                    if grid[i][j] == 1:
                        winner += 1
            if winner == (len(grid) - 1):
                return i

        return winner
    
print(Solution().findChampion([[0,1],[0,0]]))
print(Solution().findChampion( [[0,0,1],[1,0,1],[0,0,0]]))
print(Solution().findChampion( [[0,0],[1,0]]))