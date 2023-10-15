class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        MOD = 12345
        sol = [[None for _ in range(cols)] for _ in range(rows)]

        pf = [1] * (rows * cols)
        for i in range(1, rows*cols):
            # print(i ,i//rows, i%cols)
            pf[i] = pf[i-1] * grid[(i-1)//cols][(i-1)%cols] % MOD

        sf = [1] * (rows * cols)
        for i in range(rows*cols-2, -1, -1):
            # print(i ,i//rows, i%cols)
            sf[i] = sf[i+1] * grid[(i+1)//cols][(i+1)%cols] % MOD

        for i in range(rows * cols):
            sol[i // cols][i % cols] = pf[i] * sf[i] % MOD

        return sol