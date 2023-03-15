class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                countiner= ""
                while stack[-1] != "[" :
                    countiner = stack.pop() + countiner
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k)*countiner)
        return "".join(stack)
       

        
             