class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x-1
        if x==1 or x==0:
            return x

        while high >= low:
            mid = (low + high)//2
            mult = mid *mid
            if mult == x:
                return mid
            elif mult < x:
                low = mid + 1
            else:
                high = mid -1
        return low-1