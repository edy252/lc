class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        letters = ['a','e','i','o','u']

        @cache
        def dp(letter, remain):
            if remain == 0: 
                return 1

            ways = 0
            if letter == 'a':
                for option in ['e']:
                    ways += dp(option, remain-1)
            elif letter == 'e':
                for option in ['a','i']:
                    ways += dp(option, remain-1)
            elif letter == 'i':
                for option in ['a','e', 'o', 'u']:
                    ways += dp(option, remain-1)
            elif letter == 'o':
                for option in ['i', 'u']:
                    ways += dp(option, remain-1)
            elif letter =='u':
                for option in ['a']:
                    ways += dp(option, remain-1)

            return ways % MOD


        res = 0
        for letter in letters:
            res += dp(letter, n-1) % MOD


        return res % MOD