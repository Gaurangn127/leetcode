class Solution:
    def reverse(self, x: int) -> int:
        new = 0
        copy = x

        if x < 0 :
            x *= -1

        while x > 0 :
            new = (new * 10) + (x % 10) 
            x = x // 10

        if new > (2**31) - 1:
            return 0

        return -new if copy < 0 else new