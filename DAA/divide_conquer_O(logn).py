def powerfun(x,n):
    if n==0:
        return 1
    temp = powerfun(x,int(n/2))
    if(n%2==0):
        return temp*temp
    else:
        return x*temp*temp

x = 2
n = 8
result = powerfun(x,n)
print(result)