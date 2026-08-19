def powerfun(x,n):
    if n==0:
        return 1
    elif(n%2==0):
        return powerfun(x,int(n/2))*powerfun(x,int(n/2))
    else:
        return powerfun(x,int(n/2))*powerfun(x,int(n/2))*x

x = 2
n = 8
result = powerfun(x,n)
print(result)