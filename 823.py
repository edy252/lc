class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        factors = collections.defaultdict(list)
        comb = collections.defaultdict(lambda: 1)

        arr.sort()

        # Compute factors of arr, going from arr[i] to arr[i-1], checking if the other factor also exists from arr[i] to arr[i-1]
        for i in range(len(arr)):
            this_num = arr[i]

            for j in range(0, i):
                
                if this_num / arr[j] % 1 == 0:
                    factor2 = int(this_num / arr[j])
                
                    if factor2 in arr[:i]:
                        factors[this_num].append([arr[j], factor2])            
        
        for this_num, comblist in sorted(factors.items()):
            for pair in comblist:
                comb[this_num] += comb[pair[0]] * comb[pair[1]]

        n = len(arr)
        factors_n = len(comb)

        return (sum(comb.values()) + (n - factors_n)) % MOD