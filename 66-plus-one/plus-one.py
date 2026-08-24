class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0
            digits[i] = 0
            
        # If all digits were 9 (e.g., [9,9] ->)
        return [1] + digits
