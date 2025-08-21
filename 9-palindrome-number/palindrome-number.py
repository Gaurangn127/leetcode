class Solution:
    def isPalindrome(self, x: int) -> bool:
        s= f"{x}"
        l = len(s)
        for i in range(len(s)//2) :
            if s[i] != s[l-i-1]:
                return False
        return True