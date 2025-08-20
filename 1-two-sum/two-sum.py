class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        #it would be much easier if we could just return the numbers
        #but instead we have to return the indices
        #hence, we make use of the enumerate function
        #enumerate([2,7,11,15]) >>> [(0,2),(1,7),(2,11),(3,15)]

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashmap :
                return [hashmap[diff], i]

            hashmap[n] = i #if we didnt find a complement, we store n in the hashmap
            