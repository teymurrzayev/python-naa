def average_salary_excluding_min_max(salary: list[int]) -> float:
    min_salary = min(salary)
    max_salary = max(salary)

    total = sum(salary) - min_salary - max_salary
    average = total / (len(salary) - 2)
    
    return average