class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        # min val up to and excluding i
        prefix = [float('inf')] * n
        suffix = [float('inf')] * n

        min_so_far = nums[0]
        for i in range(1, n):
            prefix[i] = min_so_far
            min_so_far = min(min_so_far, nums[i])
            

        min_so_far = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = min_so_far
            min_so_far = min(min_so_far, nums[i])

        # print(prefix)
        # print(suffix)
            
        min_sum = float('inf')
        for i in range(1, n-1):
            if prefix[i] < nums[i] and suffix[i] < nums[i]:
                # cur_sum = nums[i] + prefix[i] + suffix[i]
                # print(cur_sum)
                min_sum = min(min_sum, nums[i] + prefix[i] + suffix[i])


        return -1 if min_sum == float('inf') else min_sum