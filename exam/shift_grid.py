def shift_grid(grid, k):
    m, n = len(grid), len(grid[0])
    k %= m * n
    flat = [grid[i][j] for i in range(m) for j in range(n)]
    flat = flat[-k:] + flat[:-k]
    return [flat[i*n:(i+1)*n] for i in range(m)]
