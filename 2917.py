class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        
        if k == 1:
            res = nums[0]
            for i in range(1, len(nums)):
                res |= nums[i]
            return res
        elif k == len(nums):
            res = nums[0]
            for i in range(1, len(nums)):
                res &= nums[i]
            
            return res
                
            
        
        # index: freq
        # freq >= k
        freq = collections.defaultdict(int)
        
        for num in nums:
            rep = bin(num)[2:]
            # print(rep)
            for i in range(len(rep)):
                if rep[len(rep)-i-1] == '1':
                    # print(i)
                    freq[i] += 1
                                        
        res = 0
        for index, freqs in freq.items():
            if freqs >= k:
                res |= (1 << index)
                
            
            
        return res