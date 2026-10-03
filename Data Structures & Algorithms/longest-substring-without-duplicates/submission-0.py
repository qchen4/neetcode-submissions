class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        maxLength = 0
        current = {}
        for i in range(len(s)):
            if s[i] not in current:
                current[s[i]] = 1
            else:
                while s[i] in current:
                    current.pop(s[start])
                    start += 1
                current[s[i]] = 1                
            maxLength = max(maxLength, len(current))
        return maxLength
        
            

        

            

        