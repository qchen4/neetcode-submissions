class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        newNum = numbers
        front = 0
        back = len(numbers) -1

        while (newNum[front] + newNum[back] != target):
            if newNum[front] + newNum[back] > target: 
                back -= 1
            elif newNum[front] + newNum[back] < target:
                front += 1
        return [front +1, back +1]
           
        