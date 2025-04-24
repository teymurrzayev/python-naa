def generated_pascal(n):
    arr = [] 
    for i in range(n):  
        row = [1] 
        for j in range(1,i): 
                 row.append(row[i-1][j-1]+row[i-1][j])
        row.append(1)  
        arr.append(row)
    return arr
print(generated_pascal(4))
        
