class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        # Loop from back to front until both strings and carry are exhausted
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # Append the remainder (0 or 1) and calculate the new carry
            result.append(str(total % 2))
            carry = total // 2

        # Reverse the result to get the final binary string
        return "".join(reversed(result))
