def odd_cells(m: int, n: int, indices: list[list[int]]) -> int:
    row_counts = [0] * m
    col_counts = [0] * n
    
    for r, c in indices:
        row_counts[r] += 1
        col_counts[c] += 1
    
    odd = 0
    for i in range(m):
        for j in range(n):
            if (row_counts[i] + col_counts[j]) % 2 != 0:
                odd += 1
    return odd