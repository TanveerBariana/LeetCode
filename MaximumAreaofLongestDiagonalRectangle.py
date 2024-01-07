class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_diag = 0
        max_area = 0
        for i in range(len(dimensions)):
            x = dimensions[i][0]
            y = dimensions[i][1]
            diag = ((x**2)+(y**2))**0.5
            if(diag > max_diag):
                max_diag = diag
                max_area = x * y
            elif(diag == max_diag):
                max_area = max(max_area, x * y)

            # diag = ((x**2)+(y**2))**0.5
        #print(max_area)
        return max_area

Solution().areaOfMaxDiagonal([[9,3],[8,6]])