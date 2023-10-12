# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        # Find peak
        lo = 1
        hi = n - 1
        mid = lo + (hi-lo)//2
        # print(lo, mid, hi)

        while lo < hi:
            val = mountain_arr.get(mid)
            next = mountain_arr.get(mid+1)

            if val < next:
                lo = mid + 1
            else: # val >= next
                hi = mid

            mid = lo + (hi-lo)//2
            # print(lo, mid, hi)
        peak = mid
        # print(peak)
        

        # Search in increasing side
        lo = 0
        hi = peak
        
        while lo <= hi:
            mid = lo + (hi-lo)//2
            val = mountain_arr.get(mid)
            
            if target == val: return mid
            elif target > val: 
                lo = mid + 1
            else:
                hi = mid - 1
        # At this point, the number was not found

        # Search in decreasing side
        lo = peak + 1
        hi = n-1
        
        while lo <= hi:
            mid = lo + (hi-lo)//2

            val = mountain_arr.get(mid)

            if target == val: return mid
            elif target > val:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1