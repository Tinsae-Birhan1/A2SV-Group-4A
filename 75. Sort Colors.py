class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            small = i
            for j in range(i + 1 , len(nums)):
                if nums[small] > nums[j]:
                    small = j
            
            nums[small], nums[i] = nums[i], nums[small]