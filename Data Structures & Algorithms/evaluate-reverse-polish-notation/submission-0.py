class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        #if token is a number: push it
        #if token is a operator: 
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(int(i))

            else:
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    stack.append(a+b)
            
                if i == "-":
                    stack.append(a-b)
            
                if i == "*":
                    stack.append(a * b)
            
                if i == "/":
                    stack.append(int(a/b))
        
        return stack[0]





        