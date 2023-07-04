class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[]
        
        for r in range (len(nums)):
            count=0
            for l in range (len(nums)):
                if l!=r and nums[l] < nums[r]:
                    count+=1
            arr.append(count)
            
        return arr