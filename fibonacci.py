n=int(input())
i=1
a=0
b=1
while i<=n:
    c=a+b
    print(a,end=' ')
    a=b
    b=c
    i+=1
    