def split_three_digit_number(n):
    hundreds = n // 100 
    tens = (n % 100) // 10  
    units = n % 10  
    return (hundreds, tens, units) 

print(split_three_digit_number())