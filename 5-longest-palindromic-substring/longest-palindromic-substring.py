class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        for i in range(len(s)):
            # Odd length palindrome
            left, length = expand(i, i)
            if length > max_len:
                start = left
                max_len = length

            # Even length palindrome
            left, length = expand(i, i + 1)
            if length > max_len:
                start = left
                max_len = length

        return s[start:start + max_len]