class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if "-" in s:
            s=s[::-1]
            s=s[:-1]
            s="-" + s
            s=int(s)
            if not (-2147483648 <= s <= 2147483647):
                return 0
            else:
                return s
        else:
            s=s[::-1]
            s=int(s)
            if not (-2147483648 <= s <= 2147483647):
                return 0
            else:
                return s