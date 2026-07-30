class Solution:
    def maxArea(self, heights: List[int]) -> int:
        product = 0
        length = len(heights)
        left, right = 0, length - 1
        while left < right:
            product = max(product, (right - left) * min(heights[left], heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return product