class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)): 
            char = s[i]
            print(stack)
            if char == '(' or char =='{' or char =='[':
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    pop = stack.pop()
                    if ((pop == '(' and char != ')' )or 
                        (pop == '{' and char != "}" ) or 
                        (pop == '[' and char != ']')):
                        return False

        if not stack:
            return True
        else:
            return False