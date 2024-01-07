class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # min_Moves = 0
        #print(min(self.minMovesRook(a, b, c, d, e, f), self.minMovesBish(a, b, c, d, e, f)))
        return min(self.minMovesRook(a, b, c, d, e, f), self.minMovesBish(a, b, c, d, e, f))
    
    def minMovesRook(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        moves = 0
        if (a == e or b == f):
            if(self.noCollideRook(a, b, c, d, e, f)):
               return 1     
        return 2
    
    def minMovesBish(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        x = abs(c-e)
        y = abs(d-f)
        Ncolide = self.noCollideBish(a, b, c, d, e, f) 
        if(x== y and Ncolide):
            return 1
        return(3)
    
    def noCollideBish(self, a: int, b: int, c: int, d: int, e: int, f: int) -> bool:
        x = abs(c-a)
        y = abs(d-b)
        if (e > c and f > d):
            if((a > c and b > d) and (e > a and f > b)):
                if(x== y):
                    return False
        elif(e < c and f> d):
            if((a < c and b > d) and (e < a and f > b)):
                if(x== y):
                    return False
        elif(e < c and f< d):
            if((a < c and b < d) and (e < a and f < b)):
                if(x== y):
                    return False
        elif(e > c and f< d):
            if((a > c and b < d) and (e > a and f < b)):
                if(x== y):
                    return False
        return True
    
    def noCollideRook(self, a: int, b: int, c: int, d: int, e: int, f: int) -> bool:
        if(e == a and f > b):
            if((c == a and d > b)and (f > d)):
                return False
        elif(e == a and f < b):
            if((c == a and d < b)and (f < d)):
                return False
        elif(e > a and f == b):
            if((c > a and d == b)and (e > c)):
                return False
        elif(e < a and f == b):
            if((c < a and d == b)and (e < c)):
                return False
        return True

#Solution().minMovesToCaptureTheQueen(a = 5, b = 3, c = 3, d = 4, e = 5, f = 2)
#Solution().minMovesToCaptureTheQueen(a = 4, b = 3, c = 3, d = 4, e = 5, f = 2)
Solution().minMovesToCaptureTheQueen(a = 1, b = 1, c = 1, d = 4, e = 1, f = 8)
