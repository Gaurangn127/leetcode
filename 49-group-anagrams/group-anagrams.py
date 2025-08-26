class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs :
            count = [0] * 26

            for char in s :
                count[ord(char) -  ord("a")] += 1

            key = tuple(count)

            if key not in hashmap :
                hashmap[key] = []
            
            hashmap[key].append(s)

        return list(hashmap.values())