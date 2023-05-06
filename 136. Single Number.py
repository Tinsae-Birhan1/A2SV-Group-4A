class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # for i, count in count.items():
        #     if count ==1:
        #         return i      
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]

        return ans       
