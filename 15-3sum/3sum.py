class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to easily handle duplicates and use two pointers
        nums.sort()
        result = []
        length = len(nums)
        
        for i in range(length - 2):
            # If the current number is greater than 0, a sum of 0 is impossible
            if nums[i] > 0:
                break
                
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Initialize two pointers
            left = i + 1
            right = length - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Need a larger sum
                elif total > 0:
                    right -= 1  # Need a smaller sum
                else:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move both pointers forward after finding a match
                    left += 1
                    right -= 1
                    
        return result
