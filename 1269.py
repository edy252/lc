class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # Already included is all stay
        mod = 10 ** 9 + 7

        @cache
        def dp(cur_steps, arrPos):
            if arrPos < 0 or arrPos >= arrLen: return 0
            if steps == cur_steps:
                if arrPos == 0: return 1
                else: return 0

            # Go left
            ct = 0
            ct += dp(cur_steps + 1, arrPos-1)
            ct += dp(cur_steps + 1, arrPos+1)
            ct += dp(cur_steps + 1, arrPos)

            return ct

        return dp(0, 0) % mod