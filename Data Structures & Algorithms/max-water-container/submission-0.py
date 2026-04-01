class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        max_height = 0
        while l < r:
            
            h = (r-l)*min(heights[l], heights[r])

            if h > max_height:
                max_height = h

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_height