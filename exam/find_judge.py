def find_judge(n: int, trust: list[list[int]]) -> int:
    if n == 1:
        return 1
    
    trusted_by = [0] * (n + 1)
    trusts = [0] * (n + 1)
    
    for a, b in trust:
        trusts[a] += 1
        trusted_by[b] += 1
    
    for i in range(1, n + 1):
        if trusted_by[i] == n - 1 and trusts[i] == 0:
            return i
    return -1