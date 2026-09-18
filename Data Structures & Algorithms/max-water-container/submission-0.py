class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_area = 0
        while right > left:
            x = min(heights[left], heights[right])
            y = right - left
            area = x * y
            max_area = max(area, max_area)
            if heights[left] >= heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
        return max_area
    