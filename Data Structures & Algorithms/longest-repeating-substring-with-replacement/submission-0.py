class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        chars = {}
        max_cnt = 0

        for R in range(len(s)) :
            chars[s[R]] = 1 +chars.get(s[R], 0)
            max_cnt = max(max_cnt, chars[s[R]])
            
            # move the left pointer to the right until # of replacement < k
            if (R - L +1 - max_cnt > k):
                chars[s[L]] -= 1
                L += 1
        
        return (R -L +1)
            

                
                






                
            
            




                



        
        
        
        
        