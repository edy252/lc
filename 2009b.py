class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
    
        unique_nums =sorted(set(nums))
        #unique_nums
        
        min_ops = n  
        start, end = 0, 0

        print(unique_nums)
        
        while end < len(unique_nums) and start < len(unique_nums):
            print(start, end)
            # If this windows's difference is small enough to maybe eventually satisfy n-1, then update min operations and expand the window. 
            if unique_nums[end] - unique_nums[start] <= n - 1:
                min_ops = min(min_ops, n - (end - start + 1))
                print(n - (end - start + 1))
                end += 1
            # If the window's difference is too large, then no use in expanding the window. Move the start ptr. 
            else:
                start += 1

        return min_ops