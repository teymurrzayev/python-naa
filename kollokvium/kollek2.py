def find_anagram_group_number(word_list):
    n = len(word_list)
    list1 = set() 
    a = 0
    for i in range(n):
        if i in list1:
            continue  
        a += 1  
        for j in range(i + 1, n): 
            if sorted(word_list[i]) == sorted(word_list[j]):  
                list1.add(j)  
    return a
print(find_anagram_group_number(["abaa", "teym", "yetm"]))