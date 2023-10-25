class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # n num of rows left
        # A leaf node has n = 1
        def dfs(n, k, rootVal):
            if n == 1: return rootVal

            totalNodes = 2 ** (n-1)

            # Move left
            # If 0, the left will be 0 and the right will be 1.
            if k <= totalNodes / 2:
                if rootVal == 0:
                    return dfs(n-1, k, 0)
                else:
                    return dfs(n-1, k, 1)
            else:
                if rootVal == 0:
                    return dfs(n-1, k - (totalNodes/2), 1)
                else:
                    return dfs(n-1, k - (totalNodes/2), 0)
        
        return dfs(n, k, 0)
