class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def a_includes_b(a: dict, b: dict):
            for key in b.keys():
                if key not in a.keys():
                    return False
                if a[key] < b[key]:
                    return False
            return True
        

                


        t_dict = {}
        for each in t:
            if each not in t_dict:
                t_dict[each] = 1
            else:
                t_dict[each] += 1
        print(t_dict)
        
        
        substring = ""
        length = 1000000

        for left in range(len(s)):
            for right in range(left, len(s)+1):
                sub_dict = {}
                sub_s = s[left: right]
                
                for each in sub_s:
                    if each not in sub_dict:
                        sub_dict[each] = 1
                    else:
                        sub_dict[each] += 1
                print(sub_s, sub_dict)
                if a_includes_b(sub_dict, t_dict):
                    print(sub_dict, t_dict)
                    if len(sub_s) < length:
                        length = len(sub_s)
                        substring = sub_s
                
        return substring
                    
                

    
        
        
        
        