class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [] 

        for l in s:
            if l == ")":
                reversed = []
                while stack and stack[-1] != "(":
                    reversed.append(stack.pop())
                if stack: 
                    stack.pop()
                stack.extend(reversed)
            else: 
                stack.append(l)
        result = "".join(stack)
        return result 