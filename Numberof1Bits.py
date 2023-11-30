class Solution:
    def hammingWeight(self, n: int) -> int:
        n = list(bin(n))
        print(str(n.count('1')))
        return n.count('1')
    

Solution().hammingWeight(0b0000000000000000000000000001011)