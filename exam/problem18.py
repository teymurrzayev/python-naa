def chocolateFeast(n, c, m):
    chocolates = n // c        
    wrappers = chocolates      

    while wrappers >= m:
        extra = wrappers // m  
        chocolates += extra
        wrappers = extra + (wrappers % m)  

    return chocolates