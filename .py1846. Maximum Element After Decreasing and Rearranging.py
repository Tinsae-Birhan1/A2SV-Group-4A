class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        count =1
        for i in range(len(arr)):
            arr[i]=min(arr[i], count)
            count = arr[i] + 1
        return count-1