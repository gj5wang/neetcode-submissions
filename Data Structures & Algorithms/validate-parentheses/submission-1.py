class Solution:
    def isValid(self, s: str) -> bool:
        #using stack
        #ummm
        #logic here is that
        stack = []

        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in "[{(":
                stack.append(char)
            else:
                if not stack:
                    return False
                elif stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0