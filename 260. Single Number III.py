class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # count = Counter(nums)
        # stack = []
        # for i , count in count.items():
        #     if count == 1:
        #         stack.append(i)
        # return stack
        num1 = 0
        num2 = 0
        for i in nums:
            num1 = num1 ^ i
        for i in nums:
            if (num1 & (-num1)) & i == 0:
                num2 = num2 ^ i
        return [num1^num2, num2]

        