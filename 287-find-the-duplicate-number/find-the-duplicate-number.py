class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #i hate this questions :/

        #remember: 2*slow = fast
        # slow = P + (C - x)
        # fast = P + C + (C - x) 
        # => P = x


        slow, fast = 0, 0

        while True :
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast :
                break

        slow2 = 0

        while True :
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2 :
                return slow

