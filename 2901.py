class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def checkValid(x, y):
            if groups[x] == groups[y]: return False
            if len(words[x]) != len(words[y]): return False
            # Calc hamming dist
            hdist = 0
            for i in range(len(words[x])):
                if words[x][i] != words[y][i]:
                    hdist += 1
                    if hdist > 1: return False

            return hdist == 1
        
        # Best length of subsequence up til and including i
        dp = []
        # For this subsequence, find the rightmost index j that gave you this subsequence
        back = []
        best_length = 0
        # Store index i of best subsequence
        best_index = 0
        
        for i in range(n):
            # The default case is when we don't combine any words, and just use this word at i
            best_i_length = 1
            # The j index that was responsible for leading to a better subsequence than 1.
            best_i_index = None
            
            # First pass does not run this block
            for j in range(i):
                # Updating best length and best index
                if checkValid(i, j) and best_i_length < 1 + dp[j]:
                    best_i_length = 1 + dp[j]
                    best_i_index = j
            
            dp.append(best_i_length)
            back.append(best_i_index)

            if best_i_length > best_length:
                best_length = best_i_length
                best_index = i

        # print(dp)
        # print(back)
        # print(best_length)
        # print(best_index)

        ret = []
        cur = best_index

        while cur is not None:
            ret.append(words[cur])
            cur = back[cur]

        return ret[::-1]