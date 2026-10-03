class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        window = {}
        size = len(s1)
        L = 0 

        if size > len(s2): 
            return False

        for char in s1:
            target[char] = 1 + target.get(char, 0)

        for R in range(len(s2)):
            if R - L +1 > size: 
                if window[s2[L]] == 1:
                    window.pop(s2[L])
                else:
                    window[s2[L]] -=1
                L +=1 
            window[s2[R]] = window.get(s2[R], 0) +1
                
            print(L, R, window)
    
            if window == target:
                return True 
        return False




            
            
            
        
             
                    
            
        
        
        