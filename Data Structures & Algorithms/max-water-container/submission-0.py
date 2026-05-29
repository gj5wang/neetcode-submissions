class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #formula: min(left, right) * (right - left)
        #using greedy, assume every each is the maximum, compare the previous one with the next posibility
        #keep the one larger
        left = 0
        right = len(heights) - 1 
        max_area = 0 

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height

            max_area = max(max_area, area)

            #move the shorter side(greedy)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area