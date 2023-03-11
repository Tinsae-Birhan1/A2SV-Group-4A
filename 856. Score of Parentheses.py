class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        answer = 0
        result = 0

        for item in s:
            if item == "(":
                stack.append(0)
            else:
                count = stack.pop()
                if count == 0:
                    answer = 1
                else:
                    answer = count *2
                if not stack:
                    result += answer
                else:
                    stack[-1] += answer
        return result
