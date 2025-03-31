def calculate_average(lst):
    if not lst:
        return None 
    
    else:
        return sum(lst)/len(lst)
    
print(calculate_average())