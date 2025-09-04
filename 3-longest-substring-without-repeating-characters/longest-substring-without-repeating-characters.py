class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hashset = set()
        max_len = 0

        for right in range(len(s)) :
            while s[right] in hashset :
                hashset.remove(s[left])
                left += 1
        
            hashset.add(s[right])
            max_len = max(max_len, right - left + 1)
    
        return max_len