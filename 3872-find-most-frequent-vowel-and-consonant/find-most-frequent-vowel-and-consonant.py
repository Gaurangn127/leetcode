class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        v_hash, c_hash = {}, {}
        v_max, c_max = 0, 0

        for char in s :
            if char in vowels :
                v_hash[char] = v_hash.get(char, 0) + 1
                v_max = max(v_hash[char], v_max)
            
            else :
                c_hash[char] = c_hash.get(char, 0) + 1
                c_max = max(c_hash[char], c_max)
        
        return c_max + v_max