class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x1, x2 = 0, len(numbers) -1

        while x1 < x2 :
            temp = numbers[x1] + numbers[x2]

            if temp == target :
                return [x1+1, x2+1]

            if temp > target :
                x2 -= 1
            
            if temp < target :
                x1 += 1