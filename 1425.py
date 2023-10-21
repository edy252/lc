from heapq import heappush, heappop
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Maintain a maxheap of the k items before current item. 
        heap = []
        heappush(heap, (-1 * nums[0], 0))
        ans = nums[0]
        

        for i in range(1, n):
            # Use this to remove possible maxitems from maxheap that exceed i-j <= k rule.
            # This doesn't remove all items that do not follow this rule from the maxheap, we only care about the max item. 
            while i - (heap[0][1]) > k:
                heappop(heap)

            # We only take the previous number if it is > 0.
            curr = max(0, -1 * heap[0][0]) + nums[i]
            heappush(heap, (-1 * curr, i))

            ans = max(ans, curr)

        return ans