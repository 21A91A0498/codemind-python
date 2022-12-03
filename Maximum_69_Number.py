def max(n):
    p=n
    c=0
    i=0
    while n:
        d=n%10
        if d==6:
            c=i
        n=n//10
        i+=1
    m=p+3*(pow(10,c))
    return m
    
    
n=int(input())
if n==9999:
    print(n)
elif max(n):
    print(max(n))