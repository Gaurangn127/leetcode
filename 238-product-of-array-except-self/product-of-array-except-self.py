class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #the idea is to iterate through the array twice
        #1st iteration from left of the array: product of all elements to the left
        #2nd iteration from right of the array: product of all elements to the right 
        #if you multiply product of all nos. to the left and right, you have the req. product

        answer = [1] * len(nums)

        product = 1
        for i in range(len(nums)):
            answer[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= product
            product *= nums[i]
        
        return answer
