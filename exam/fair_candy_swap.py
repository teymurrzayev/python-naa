def fair_candy_swap(alice_sizes, bob_sizes):
    sum_a, sum_b = sum(alice_sizes), sum(bob_sizes)
    target = (sum_a + sum_b) // 2
    set_b = set(bob_sizes)
    
    for x in alice_sizes:
        y = x + (target - sum_a)
        if y in set_b:
            return [x, y]
    return []
