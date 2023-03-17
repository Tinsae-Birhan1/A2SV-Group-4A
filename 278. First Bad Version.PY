# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        count = -1
        while high >= low:
            mid = (low + high)//2
            if isBadVersion(mid):
                count = mid
                high = mid -1
            elif isBadVersion(mid) == False:
                low = mid + 1 
        return count