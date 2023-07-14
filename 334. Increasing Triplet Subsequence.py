class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l=float("inf")
        k=float("inf")
        for i in range(len(nums)):
            if nums[i] <= l:
                l = nums[i]
            elif nums[i] <= k:
                k=nums[i]
            else:
                return True 
        return False
