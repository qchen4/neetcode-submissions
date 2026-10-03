class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        maxLeft = 0
        maxRight = 0
        area = 0

        while l < r: 
            maxLeft = max(height[l], maxLeft)
            maxRight = max(height[r], maxRight)
            if maxLeft < maxRight: 
                vol = min(maxLeft, maxRight) - height[l]
                area += max(0, vol)
                l += 1
            else:
                vol = min(maxLeft, maxRight) - height[r]
                area += max(0, vol)
                r -= 1


        return area
            


            




        
        