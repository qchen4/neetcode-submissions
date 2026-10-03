class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0 
        end = k
        res = []
        while end < (len(nums) +1): 
            res.append(max(nums[start: end]))
            start += 1
            end += 1
        return res