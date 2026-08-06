class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit signed integer boundaries
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        # If string is empty or contains only spaces
        if i == n:
            return 0
            
        # 2. Check for sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Convert digits and handle overflow
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            i += 1
            
        # Apply sign
        res *= sign
        
        # 4. Clamping to 32-bit signed integer range
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res
