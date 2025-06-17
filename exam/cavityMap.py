def cavityMap(grid: list[str]) -> list[str]:
    n = len(grid)
    if n <= 2:
        return grid.copy() 

    grid = [list(row) for row in grid]
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            current = grid[i][j]
            if (current > grid[i-1][j] and 
                current > grid[i+1][j] and 
                current > grid[i][j-1] and 
                current > grid[i][j+1]):
                grid[i][j] = 'X'

    return [''.join(row) for row in grid]