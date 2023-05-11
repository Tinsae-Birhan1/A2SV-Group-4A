class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            a_i = ord(a[i]) - ord("0")  if i< len(a) else 0
            b_i = ord(b[i]) - ord("0")  if i< len(b) else 0

            y = b_i +a_i +carry
            carry = y //2
            x = str(y % 2)
            ans = x + ans 
        if carry:
            ans = "1" + ans
        return ans 
