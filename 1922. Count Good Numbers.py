class Solution:
    def GoodNumbers(self, x, n):
        mod = 10**9 + 7
        if n == 0:
            return 1
        
        half = self.GoodNumbers(x, n//2)
        return (half*half*x**(n%2)) % mod
        
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        odd = n//2
        even = odd + n%2
        
        return (self.GoodNumbers(4, odd) * self.GoodNumbers(5 , even))%mod
    
        
