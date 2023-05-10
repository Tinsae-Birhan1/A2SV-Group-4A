class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i-1
            while j >= 0 and key <nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key

        index = []
        for i in range(len(nums)):
            if nums[i] == target:
                index.append(i)
        return index
        