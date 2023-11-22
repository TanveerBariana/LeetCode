class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        resu = []
        strin = []
        ans = 0
        for i in nums:
            strin.append(list(bin(i)[2:].zfill(31)))
        for i in range(len(strin[0])):
            numBits = 0
            for j in range(len(strin)):
                if strin[j][-(i+1)] == '1':
                    numBits += 1
            if numBits >= k :
                resu.append(i)    
        for i in resu:
            ans += 2**i    
        return ans

print(Solution().findKOr([7,12,9,8,9,15], 4))
print(Solution().findKOr([2,12,1,11,4,5], 6))
print(Solution().findKOr([10,8,5,9,11,6,8], 1))