class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        ans = high 
        while high >= low:
            mid = (low + high) // 2
            hour = 0
            for i in piles:
                hour += math.ceil(i/mid)
            
            if hour <= h:
                ans = min(ans, mid)
                high = mid-1
            elif hour > h:
                low = mid +1
        
        return ans
