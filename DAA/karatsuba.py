def karatsuba(x,y):
    if (x <= 10 or y <= 10):
        return x*y
    n = max(len(str(x)),len(str(y)))
    m = n//2
    
    A = x // (10**m)
    B = x % (10**m)
    C = y // (10**m)
    D = y % (10**m)
    
    ac = karatsuba(A,C)
    bd = karatsuba(B,D)
    abcd = karatsuba((A+B),(C+D)) - ac - bd
    return(ac*(10**(2*m))+bd+abcd*(10**m)) 

x = 1234
y = 5678
print(karatsuba(x,y))