class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0
        two = 0 
        for i in nums:
            one = (one ^ i) & ~two
            two = (two ^ i) & ~one
        return one

       
       
        # count = Counter(nums)
        # for i, count  in count.items():
        #     if count == 1:
        #         return i