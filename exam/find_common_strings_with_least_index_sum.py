def find_common_strings_with_least_index_sum(list1: list[str], list2: list[str]) -> list[str]:
    list1_indices = {string: index for index, string in enumerate(list1)}
    
    min_sum = float('inf')
    result = []
    
    for index2, string in enumerate(list2):
        if string in list1_indices:
            index1 = list1_indices[string]
            current_sum = index1 + index2
            if current_sum < min_sum:
                min_sum = current_sum
                result = [string]
            elif current_sum == min_sum:
                result.append(string)
    
    return result