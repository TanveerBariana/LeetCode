class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        k= 0
        l= 1
        for i in nums:
            for j in nums[l:]:
                if i + j == target:
                    return k,l
                l = l+1
            k = k+1
            l= k+1