class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        xor = x ^ y
        while xor != 0:
            if xor & 1 == 1:
                res += 1
            xor >>= 1
        return res



