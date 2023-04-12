class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        count =[]
        def dfs(x):
            if x >= len(nums):
                stack.append(count.copy())
                return
            
            count.append(nums[x])
            dfs(x+1)
            count.pop()
            dfs(x+1)
        
        dfs(0)
        return stack