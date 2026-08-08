class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit signed integer limits
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # Handle the only edge case that causes an overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine the sign of the result
        # Bitwise XOR (^) is True if the signs are different
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values to simplify the logic
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        
        # Subtract the largest shifted divisor from the dividend at each step
        while dvd >= dvs:
            temp = dvs
            multiple = 1
            
            # Keep doubling the temp divisor and multiple until just before it exceeds the dividend
            while dvd >= (temp << 1):
                temp <<= 1
                multiple <<= 1
                
            # Subtract the chunk from dividend and add the multiple to our result
            dvd -= temp
            quotient += multiple
            
        # Apply the original sign
        if negative:
            quotient = -quotient
            
        # Clamp the result within the 32-bit signed integer range (as a safety net)
        if quotient > MAX_INT:
            return MAX_INT
        elif quotient < MIN_INT:
            return MIN_INT
            
        return quotient