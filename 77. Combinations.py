class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = []

        def help(left, count):
            if k == len(count):
                stack.append(count.copy())
                return 
            
            for i in range(left, n+1):
                count.append(i)
                help(i+1, count)
                count.pop()
        
        help(1, [])
        return stack