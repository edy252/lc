class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        
        # i is the painter we are considering. We have to choose to either use this painter or use a free painter
        # When using dp, return value should be the answer (cost)
        # Remain: remaining walls that need to be painted.
        # i: the paid painter i.
        @cache
        def dp(i, remain):
            # If there are 0 walls remaining, we return 0
            if remain <= 0: return 0
            if i == n: return float('inf')

            # Painting means we both use the paid painter and the free painter(s). So we subtract both time[i] and 1. 
            # Free painter will paint 1 wall each turn, ex: a paid painter who takes 3 time will be associated with 3 free painters who paint 3 walls for free. 
            # The -1 is associated with the one wall painted by the paid painter, and the -time[i] represents the time[i] walls painted by the free painters.
            # Not painting will not have any cost, and will not reduce remain.
            
            paint = cost[i] + dp(i + 1, remain - 1 - time[i])
            # print('p', i, remain, paint)
            dontPaint = dp(i+1, remain)
            # print('dp', i, remain, dontPaint)

            return min(paint, dontPaint)

        return dp(0,n)