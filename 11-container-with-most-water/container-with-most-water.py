class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # 1. Calculate the distance between lines
            width = right - left
            
            # 2. Water height is limited by the shorter line
            current_height = min(height[left], height[right])
            
            # 3. Update the maximum area tracked so far
            current_water = width * current_height
            max_water = max(max_water, current_water)
            
            # 4. Always shift the pointer pointing to the shorter vertical line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
