class Solution:
    def curPow(self, x, n):
        if n == 0:
            return 1
        half = self.curPow(x, n//2)
        return half*half * x **(n%2)
    def myPow(self, x: float, n: int) -> float:
        if n >= 0: 
            return self.curPow(x,n)
        return 1/ self.curPow(x,-n)
        
        
        
            