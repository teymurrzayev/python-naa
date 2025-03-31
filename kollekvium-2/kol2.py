def find_anagram_group_number(word_list):
    list1 = set()  

    for word in word_list:
        word1 = "".join(sorted(word)) 
        list1.add(word1)  

    return len(list1) 

print(find_anagram_group_number()) 

