class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for _ in range(len(nums) +1)]

        # algorithm in use: bucket sort 

        hashmap = Counter(nums)
        
        for n, count in hashmap.items() :
            freq[count].append(n)
  
        res = []
  
        for i in range(len(freq)-1, -1, -1) :
            for n in freq[i] :
                res.append(n)
                if len(res) == k :
                    return res