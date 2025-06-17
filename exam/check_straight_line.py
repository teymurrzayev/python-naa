def check_straight_line(coordinates: list[list[int]]) -> bool:
    if len(coordinates) <= 2:
        return True  
    
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    dx = x1 - x0
    dy = y1 - y0
    for i in range(2, len(coordinates)):
        xi, yi = coordinates[i]
        if dy * (xi - x0) != dx * (yi - y0):
            return False
    
    return True