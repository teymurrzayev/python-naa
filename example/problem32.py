def find_common_strings_with_least_index_sum(list1, list2):
    index_map = {word: i for i, word in enumerate(list1)}
    min_sum = float('inf')
    result = []

    for j, word in enumerate(list2):
        if word in index_map:
            total_index = j + index_map[word]
            if total_index < min_sum:
                min_sum = total_index
                result = [word]
            elif total_index == min_sum:
                result.append(word)

    return result