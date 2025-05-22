def unique_paths_with_obstacles(grid):
    m = len(grid)
    n = len(grid[0])

    if grid[0][0] == 0 or grid[m-1][n-1] == 0:
        return 0

    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1

    for i in range(1, m):
        if grid[i][0] != 0 and dp[i-1][0] == 1:
            dp[i][0] = 1

    for j in range(1, n):
        if grid[0][j] != 0 and dp[0][j-1] == 1:
            dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] != 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]
