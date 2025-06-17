def earliest_year_with_maximum_population(logs):
    years = [0] * 101  
    for birth, death in logs:
        years[birth - 1950] += 1
        years[death - 1950] -= 1
    
    max_pop = current_pop = 0
    result_year = 1950
    for year in range(101):
        current_pop += years[year]
        if current_pop > max_pop:
            max_pop = current_pop
            result_year = 1950 + year
    return result_year