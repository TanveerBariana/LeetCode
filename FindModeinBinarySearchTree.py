class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root:[TreeNode]) -> list[int]:
        valList = self.makeValList(root, [])
        #print(valList)
        return self.getModeList(valList)

    
    def makeValList(self, inputTree:[TreeNode], inputList:[int]) -> list[int]:
        inputList.append(inputTree.val)
        if inputTree.left != None:
            self.makeValList(inputTree.left, inputList)
        if inputTree.right != None:
            self.makeValList(inputTree.right, inputList)
        return(inputList)
    
    def getModeList(self, my_list:[int]) -> list[int]:
        # Initialize variables
        max_frequency = 0
        modes = []
        # Count occurrences manually
        count_dict = {}
        for num in my_list:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] > max_frequency:
                max_frequency = count_dict[num]
                modes = [num]
            elif count_dict[num] == max_frequency and num not in modes:
                modes.append(num)
        return modes

# class Solution:
#     def findMode(self, root:[TreeNode]) -> list[int]:
#         print(root)
#         # print(root.right)
#         # print(root.val)
#         # print(root.right.val)
#         return [1]
    


s = TreeNode(1,left=None, right=TreeNode(2, left=TreeNode(2, left=None, right=None)))
Solution().findMode([s])