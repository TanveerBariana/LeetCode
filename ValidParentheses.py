class Solution:
    def isValid(self, s: str) -> bool:
        par = 0
        sem = 0
        brak = 0
        flag = False
        input = list(s)
        rightStack = []
        righVal = None
        while input.__len__()  > 0:
            curVal = input.pop()
            if curVal in ['}', ']', ')']:
                rightStack.append(curVal)
            elif curVal in ['{', '[', '(']:
                if rightStack.__len__() > 0:
                    rightVal = rightStack.pop()
                    flag = self.parCheck(curVal, rightVal)
                    if not flag:
                        return flag
                else:
                    return False
            

            
        return (
            flag
        )
    
    def parCheck(self, curVal, rightVal):
        if curVal =='{' and rightVal == '}':
            return True
        elif curVal =='[' and rightVal == ']':
            return True
        elif curVal =='(' and rightVal == ')':
            return True
        else:
            return False

    def listCheck(self, l:list ) -> bool:
        if len(l) > 2:
            if l[0] == '(' and l[-1] ==')':
                return(True and self.listCheck(l[1:-2]))
            elif l[0] == '[' and l[-1] ==']':
                return(True and self.listCheck(l[1:-2]))
            elif l[0] == '{' and l[-1] =='}':
                return(True and self.listCheck(l[1:-2]))
            else :
                return False
            # return(
            #     (l[0] == l[-1]) 
            #     and 
            #     self.listCheck(l[0:-1])
            # )
        else:
            if l[0] == '(' and l[-1] ==')':
                return(True)
            elif l[0] == '[' and l[-1] ==']':
                return(True)
            elif l[0] == '{' and l[-1] =='}':
                return(True)
            else:
                return False


print(Solution().isValid(')(){}'))
# print(Solution().isValid('()[]{}'))
# print(Solution().isValid('(]'))
# print(Solution().isValid('([)]'))
