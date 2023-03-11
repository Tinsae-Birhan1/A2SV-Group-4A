class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == '+':
                stack.append(stack.pop() + stack.pop())
            elif item == "*":
                stack.append(stack.pop() * stack.pop())
            elif item == "-":
                item1 = stack.pop()
                item2 = stack.pop()
                stack.append(item2 - item1)
            elif item == "/":
                item1 = stack.pop()
                item2 = stack.pop()
                stack.append(int(item2 / item1))
            else:
                stack.append(int(item))
        
        return stack[0]

         
                
        