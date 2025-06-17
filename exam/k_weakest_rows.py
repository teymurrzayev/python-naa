def k_weakest_rows(mat, k):
    return sorted(range(len(mat)), key=lambda x: (sum(mat[x]), x))[:k]
