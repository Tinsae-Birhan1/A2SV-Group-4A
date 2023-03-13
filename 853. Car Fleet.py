class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pair = [[positions,speeds] for positions, speeds in zip(position, speed)]
        for positions, speeds in sorted(pair)[::-1]:
            stack.append((target-positions)/speeds)
            if len(stack)>= 2 and stack[-1] <=stack[-2]:
                stack.pop()
        return len(stack)
        