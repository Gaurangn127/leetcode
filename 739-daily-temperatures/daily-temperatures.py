class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = []

        for i in range(len(temperatures)) :
            currTemp = temperatures[i]
            
            while stack and currTemp > temperatures[stack[-1]] :
                prevIndex = stack.pop()
                res[prevIndex] = i - prevIndex
            
            stack.append(i)

        return res