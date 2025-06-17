def find_destination_city(paths: list[list[str]]) -> str:
    all_cities = set()
    starting_cities = set()
    
    for path in paths:
        starting_cities.add(path[0])
        all_cities.add(path[0])
        all_cities.add(path[1])
    
    for city in all_cities:
        if city not in starting_cities:
            return city
    return ""