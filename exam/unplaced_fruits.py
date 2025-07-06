def unplaced_fruits(fruits: list[int], baskets: list[int]) -> int:
    unplaced = 0
    baskets_available = baskets.copy()
    
    for fruit in fruits:
        placed = False
        for i in range(len(baskets_available)):
            if baskets_available[i] >= fruit:
                baskets_available[i] = -1  
                placed = True
                break
        if not placed:
            unplaced += 1
    
    return unplaced