class Solution:
    def minChanges(self, s: str) -> int:
        result = 0
        binary = list(s)
        if len(set(s)) == 2:
            if len(s) ==2:
                # print('we down here')
                # print(s)
                return 1
            half = len(s)//2
            # print
            return self.minChanges(''.join(binary[:half])) + self.minChanges(''.join(binary[half:]))
        # print("its pretty now ")
        # print(s)    
        return result 
    
    def makeChanges(self, listy: list) -> list:
        if not self.isBeuty(listy):
            if listy.count('0') > listy.count('1'):
                for i in listy:
                    print()
        return listy

    def isBeuty(self, listy: list) -> bool:
        return len(set(listy))== 1









print(Solution().minChanges("111111111110010001"))
print(Solution().minChanges("10"))
# print(Solution().minChanges("0000"))
