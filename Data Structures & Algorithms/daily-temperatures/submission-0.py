class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pointer1 = 0
        pointer2 = 0
        result = []
        for i in range(len(temperatures)):
            pointer1 = i
            for j in range(i,len(temperatures)):
                pointer2 = j
                if temperatures[j] > temperatures[i]:
                    result.append(j-i)
                    break
                elif j == len(temperatures) -1:
                    result.append(0)
        return result
            
