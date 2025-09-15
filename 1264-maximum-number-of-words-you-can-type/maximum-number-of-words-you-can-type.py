class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        words = text.split(' ')
        count = 0
        for word in words :
            flag = True
            for letter in word :
                if letter in broken :
                    flag = False
                    break
                
            if flag :
                count += 1
        
        return count