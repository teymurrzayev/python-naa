def min_path_cost(grid, moveCost):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    dp = [[float('inf')] * n for _ in range(m)]
    
    for j in range(n):
        dp[0][j] = grid[0][j]
    
    for i in range(m - 1):
        for j in range(n):
            current_val = grid[i][j]
            for k in range(n):
                next_cost = dp[i][j] + grid[i+1][k] + moveCost[current_val][k]
                if next_cost < dp[i+1][k]:
                    dp[i+1][k] = next_cost
    
    return min(dp[-1])