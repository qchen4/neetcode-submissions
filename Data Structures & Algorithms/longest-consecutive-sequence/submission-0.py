class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        length = 1
        arr_sorted = sorted(nums)
        print(arr_sorted)
        curr = 1
        for i in range(len(nums)-1):
            if arr_sorted[i] == arr_sorted[i+1] - 1:
                curr +=1
            elif arr_sorted[i] == arr_sorted[i+1]:
                curr = curr
            else:
                curr = 1
            length = max(length, curr)
        
        return length

        