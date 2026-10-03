class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {')': '(', '}': "{", "]" : "["}
        for c in s: 
            if c not in Map:
                stack.append(c)
            elif ((not stack) or (stack[-1] != Map[c])):
                return False
            else:
                stack.pop()
        if not stack:
            return True
        else:
            return False

