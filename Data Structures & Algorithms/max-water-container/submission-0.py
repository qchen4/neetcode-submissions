class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        total_area = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            total_area = max(area, total_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return total_area

        