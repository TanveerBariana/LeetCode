class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        val = 1
        while val < n:
            val *= 4
        return (val == n)
    
print(Solution().isPowerOfFour(13))