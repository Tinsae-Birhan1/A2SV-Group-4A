class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        maxave = -float("inf")
        res =[]
        while right <= len(nums):
            sums = 0
            for i in range(left, right):
                sums += nums[i]
            
            avesums = sums / k
            maxave = max(avesums, maxave)
            left += 1
            right += 1
        return maxave
        
                
     
        
       