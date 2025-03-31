def unique_char_strings_average(strings_list):
    list1 = [s for s in strings_list if len(s) == len(set(s))] 
    if not list1: 
        return 0  
    
    list2= sum(len(s) for s in list1)  
    return list2 / len(list1) 

print(unique_char_strings_average()) 