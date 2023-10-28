class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        result = 0
        j = len(nums)
        for i in range(j):
            j = len(nums)
            while j > i :
                print(nums[i:j])
                unique = set(nums[i:j])
                print(unique)
                result += len(unique)**2 
                print(result)
                j -= 1
                print('next loop')
        return result % ((10**9)+7)






print(Solution().sumCounts([1,2,1]))
print(Solution().sumCounts([1,1]))