class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7

        arrLen = min(arrLen, steps)

        # y is arrLen
        # x is steps
        # dp[curr][remain]
        dp = [[0] * (steps+1) for _ in range(arrLen)]
        dp[0][0] = 1

        # remain: is remaining steps available  to use
        # curr is position in array
        for remain in range(1, steps + 1):
            for curr in range(arrLen-1, -1, -1):
                # base case is staying
                ans = dp[curr][remain-1]
                
                # Move to the left
                if curr > 0:
                    ans = (ans + dp[curr-1][remain-1]) % mod
                # Move to the right
                if curr < arrLen - 1:
                    ans = (ans + dp[curr+1][remain-1]) % mod
                
                # This is sum of ways from moving from left to here or right to here.
                dp[curr][remain] = ans

                # for row in dp:
                #     print(row)
                # print()

        
        return dp[0][steps]


          
# arrLen  [1, 0, 0, 0]
#         [0, 0, 0, 0]