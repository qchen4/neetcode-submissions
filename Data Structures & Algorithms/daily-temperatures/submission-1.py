class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = []
        for i in range(len(temperatures)):

            for j in range(i,len(temperatures)):
     
                if temperatures[j] > temperatures[i]:
                    result.append(j-i)
                    break
                elif j == len(temperatures) -1:
                    result.append(0)
        return result
            
