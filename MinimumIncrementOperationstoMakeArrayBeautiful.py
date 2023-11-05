class Solution:
    def minIncrementOperations(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(0,len(nums)-2,1):
            lis = nums[i:i+3]
            max_value = max(lis)
            if max_value < k:
                dif = self.chargeUp(lis,k)
                ans += dif
                inx = 0
                for indec in range(len(lis)):
                    if lis[indec] == max_value:
                        inx = indec
                nums[inx+i] = nums[inx+i] + dif
        return ans 

    def chargeUp(self, lis: list[int], k: int) -> int:
        ans = 0
        ma = max(lis)
        while ma < k:
            ans += 1
            ma += 1  
        return ans   
# print(Solution().minIncrementOperations([2,3,0,0,2],4))
# print(Solution().minIncrementOperations([0,1,3,3],5))
# print(Solution().minIncrementOperations([1,1,2],1))
print(Solution().minIncrementOperations([43,31,14,4],73))
#print(Solution().minIncrementOperations([10,2,0,2],6))
#print(Solution().minIncrementOperations([2,3,0,0,2],4))
# print(Solution().minIncrementOperations([7,7,2,7],9))



# lis = [7,7,2,7]
# lis.index(max(lis), len(lis)-1)