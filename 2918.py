class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        zero1s = nums1.count(0)
        zero2s = nums2.count(0)
        
       
        
        min1 = sum1 + zero1s
        min2 = sum2 + zero2s
        
        # print('sum', sum1, sum2)
        # print('zero', zero1s, zero2s)
        # print('min', min1, min2)
        
        # min1 < min2 and min1 has a zero OK
        # min2 < min1 and min2 has a zero OK
        # min1 = min2, neither has a zero OK
        # min1 = min2, only one has a zero NOT OK
        if min1 < min2 and zero1s > 0:
            return min2
        elif min2 < min1 and zero2s > 0:
            return min1
        elif min1 == min2:
            return min1
        # elif min1 == min2 and ((zero1s == 0 and zero2s > 0) or (zero2s == 0 and zero1s > 0)):
        #     return -1
            
        
        return -1