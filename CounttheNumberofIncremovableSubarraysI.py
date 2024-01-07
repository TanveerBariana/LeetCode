class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        resultList = []
        
        for subLen in range(0, len(nums)):
            sublist = []
            dummy = nums
            for trilen in range(0, len(nums)-subLen):
                subLen+= 1

                removeList = nums[trilen:subLen]

                occurrences = None
                for i in range(len(dummy) - len(removeList) + 1):
                    if dummy[i:i+len(removeList)] == removeList:
                        occurrences = i
                        break
                sublist = [dummy[i] for i in range(len(dummy)) if i < occurrences or i > occurrences + len(removeList) - 1]
                if all(sublist[i] <= sublist[i+1] for i in range(len(sublist)-1)):
                    resultList.append(removeList)
        res = list(map(list, set(map(tuple, resultList))))
        print(resultList)
        print(res)

        return len(res)


Solution().incremovableSubarrayCount([9,6,9])
# Solution().incremovableSubarrayCount([6,5,7,8])
# Solution().incremovableSubarrayCount([8,7,6,6])