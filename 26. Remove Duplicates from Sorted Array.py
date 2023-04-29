class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # r=1
        l=0
        r=1
        while r < len(nums):
            if nums[r]==nums[l]:
                nums.remove(nums[r])
            else:
                r+=1
                l+=1
        return len(nums)
           
       
                