class Solution:
   
    def invert(self, s):
        s = list(s)
        for i in range(len(s)):
            if s[i] == "0":
                s[i] = "1"
            else:
                s[i] = "0"
        return "".join(s)

    def kBit(self, n):
        if n == 1 :
            return "0"
        prev = self.kBit(n-1)
        return prev + "1" + self.invert(prev)[::-1]
    def findKthBit(self, n: int, k: int) -> str:
        return self.kBit(n)[k-1]

        