n=int(input())
sum=0
while n or sum>9:
    if n==0:
        n=sum
        sum=0
    d=n%10
    sum=sum+d
    n=n//10
print(sum)
