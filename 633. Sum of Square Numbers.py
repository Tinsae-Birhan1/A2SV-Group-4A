class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 1
        right = int(sqrt(c))
        
        if right**2 == c:
            return True
        while right >= left:
            squ = (left * left) + (right * right)
            if squ == c:
                return True
            elif squ > c:
                right -= 1
            else:
                left += 1
        return False