class Solution:
    def isValid(self, s: str) -> bool:
        par = 0
        sem = 0
        brak = 0
        input = list(s)
        # for j in input:
        #     if j == '(':
        #         par +=1
        #     elif j == ')':
        #         par -= 1
        #     elif j == '[':
        #         brak += 1
        #     elif j == ']':
        #         brak -= 1
        #     elif j == '{':
        #         sem += 1
        #     elif j == '}':
        #         sem -= 1
        return self.listCheck(input)
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


print(Solution().isValid('()'))
print(Solution().isValid('()[]{}'))
print(Solution().isValid('(]'))
print(Solution().isValid('([)]'))
