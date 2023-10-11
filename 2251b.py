from sortedcontainers import SortedDict 
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Difference tracks the changes in flowers at specific time points. For each interval, take its start time and increment 1 to show that 1 new flower is available at that time point start. Take its end point+1, and decrement endpoint+1 to show that at that time, there is 1 less flower to view.
        difference = SortedDict()
        # At time 0, there are 0 flowers to  view.
        difference[0] = 0
        # Positions just tracks the time point in the difference dict.
        positions = []
        # Prefix tracks the running changes in difference to show how many flowers started to become available at time.
        prefix = []

        for flower in flowers:
            if flower[0] not in difference: difference[flower[0]] = 0
            if flower[1]+1 not in difference: difference[flower[1]+1] = 0
            difference[flower[0]] += 1
            difference[flower[1]+1] -= 1

        # print(difference)
        
        for key, val in difference.items():
            if key == 0: continue
            if prefix:
                prefix.append(val + prefix[-1])
            else:
                prefix.append(val)
            positions.append(key)

        # print(prefix)
        # print(positions)

        # Then need to use binary search to look between positions.
        def bs(lo, hi, time):
            while lo <= hi:
                mid = lo + (hi-lo)//2
                # print(lo, mid, hi)

                if positions[mid] == time:
                    # print(mid)
                    return prefix[mid]
                elif positions[mid] < time:
                    lo = mid + 1
                else:
                    hi = mid - 1
            if lo > mid: 
                # print(mid)
                return prefix[mid]
            if hi < mid: 
                # print(mid-1)
                return prefix[mid-1]

        return [bs(0, len(prefix)-1, time) for time in people]