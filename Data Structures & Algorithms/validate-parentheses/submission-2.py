class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            elif stack:
                if ch == ')':
                    if stack[-1] != '(': return False
                    stack.pop()
                elif ch == ']':
                    if stack[-1] != '[': return False
                    stack.pop()
                elif ch == '}':
                    if stack[-1] != '{': return False
                    stack.pop()
            else:
                return False
        return not stack