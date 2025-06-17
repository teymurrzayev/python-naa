def icecreamParlor(m, cost):
    seen = {}

    for i, price in enumerate(cost):
        diff = m - price
        if diff in seen:
            return [seen[diff] + 1, i + 1]  
        seen[price] = i
