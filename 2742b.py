class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1, n+1):
            dp[n][i] = float('inf')

        for row in dp:
            # print(row)

        for i in range(n-1, -1, -1):
            for remain in range(1, n+1):
                paint = cost[i] + dp[i+1][max(0, remain - 1 - time[i])]
                dontPaint = dp[i+1][remain]
                dp[i][remain] = min(paint, dontPaint)


        return dp[0][n]