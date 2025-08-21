class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        l = len(s)

        for i in range(l//2):
            if s[i] != s[l-i-1]:
                return False
        
        return True