class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in "([{":
                stack.append(char)
            # We're looking at ), ], or }
            else:
                 # what if stack is empty?
                if (stack == []):
                    return False
            #cases if dont match
                if (char == ")" and stack[-1] != "("):
                    return False
                if (char == "]" and stack[-1] != "["):
                    return False
                if (char == "}" and stack[-1] != "{"):
                    return False
            #case 3: matches
                stack.pop()
        return stack == []
