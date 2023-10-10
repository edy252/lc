class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n

        arr = sorted(list(set(nums)))
        n_arr = len(arr)
        # print(arr)

        def bs(lo, hi, target):
            mid = lo
            while lo <= hi:
                mid = lo + (hi-lo)//2
                # print(lo, mid, hi)

                if arr[mid] < target:
                    lo = mid + 1
                elif arr[mid] > target:
                    hi = mid - 1
                else:
                    return mid+1
            if hi < mid: return mid
            if lo > mid: return lo

        for i in range(len(arr)):
            left = arr[i]
            right = left + n - 1 # If left was the minimum, then right is the maximum
            j = bs(i, n_arr-1, right)
            
            count = j - i
            # print(left, right, j, count)
            ans = min(ans, n-count)


        return ans