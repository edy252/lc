class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # Maintain global min and max values and idxs

        # Iterate thru arr and update min/max if indexdiff is enough
        # As you move to the right, the min/max nums you find will always be spaced apart >= indexdifference, because you
        # are only comparing current num with min/max, which are always >= indexdifference apart.
        
        min_i = None
        min_val = inf
        max_i = None
        max_val = -inf

        for i in range(len(nums)):
            if i >= indexDifference:
                val = nums[i-indexDifference]

                if val > max_val:
                    max_i = i-indexDifference
                    max_val = val
                if val < min_val:
                    min_i = i-indexDifference
                    min_val = val
            # print(min_val, max_val)
            if nums[i] - min_val >= valueDifference:
                return [i, min_i]
            if max_val - nums[i] >= valueDifference:
                return [i, max_i]

        return [-1,-1] 