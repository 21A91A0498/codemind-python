n=int(input())
m=int(input())
while n<=m:
    i=1
    temp=n
    count=0
    while i<=temp:
        if temp%i==0:
            count+=1
        i+=1
    if count==2:
        print(n)
    n+=1
        
        