class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        count = {0: 1}

        for i in nums:
            max_or |= i
            count_copy = count.copy()
            
            for j in count_copy:
                x = j | i
                count[x] = count.get(x, 0) + count_copy[j]
            
        return count[max_or]